import unittest

from zope.testing import doctestunit
from zope.component import testing
from Testing import ZopeTestCase as ztc

from Products.Five import zcml
from Products.Five import fiveconfigure
from Products.PloneTestCase import PloneTestCase as ptc
from Products.PloneTestCase.layer import PloneSite
from Products.PloneTestCase.layer import onsetup

import iute.default

from zope.app import zapi
from zope.configuration import xmlconfig


ztc.installProduct('iute.default')
ztc.installProduct('uwosh.requirements')
ptc.setupPloneSite(products=('iute.default', 'uwosh.requirements'))


class IUTEDefaultTestCase(ptc.PloneTestCase):
    """
    """
