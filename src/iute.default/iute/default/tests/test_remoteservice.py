from Products.PloneTestCase.PloneTestCase import PloneTestCase
from zope.testing import doctestunit
from zope.component import testing
from Testing import ZopeTestCase as ztc
from iute.default.tests.base import IUTEDefaultTestCase
from zope.configuration.xmlconfig import xmlconfig, XMLConfig
import iute.default.tests
from cStringIO import StringIO
import zope.app.publisher.browser
from Products.Five.testbrowser import Browser

class TestRemoteService(IUTEDefaultTestCase):
    """
    Not sure how to test because an actual server never gets started up
    and urllib can't can data that way...
    """

    def afterSetUp(self):
        self.setRoles(('Manager',))
        XMLConfig('meta.zcml', zope.app.publisher.browser)()
        
def test_suite():
    from unittest import TestSuite, makeSuite
    suite = TestSuite()
    suite.addTest(makeSuite(TestRemoteService))
    
    suite.addTest(doctestunit.DocTestSuite(
        module='uwosh.core.utils',
        setUp=testing.setUp, tearDown=testing.tearDown)
    )
    
    suite.addTest(ztc.ZopeDocFileSuite(
        'README.txt', package='uwosh.core.utils',
        test_class=TestRemoteService)
    )
    
    return suite
