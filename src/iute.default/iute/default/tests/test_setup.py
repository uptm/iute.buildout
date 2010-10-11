import unittest
from iute.default.tests.base import UWOshDefaultTestCase
from Products.CMFCore.utils import getToolByName

class TestSetup(UWOshDefaultTestCase):
    """
    
    """
    
    def test_mail_host_set(self):
        self.assertEquals('mail.cenditel.gob.ve', self.portal.MailHost.smtp_host)
        
    def test_email_from_name(self):
        self.assertEquals('IUTE WebSite', self.portal.email_from_name)
    
    def test_site_map_enabled(self):
        pprops = getToolByName(self.portal, 'portal_properties')
        self.assertEquals(True, pprops.site_properties.enable_sitemap)

    def test_iute_requirements_installed(self):
        qi = getToolByName(self.portal, 'portal_quickinstaller')
        
        self.assertEquals(True, qi.isProductInstalled('uwosh.requirements'))
        

    def test_iute_theme_installed(self):
        qi = getToolByName(self.portal, 'portal_quickinstaller')

def test_suite():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(TestSetup))
    return suite
