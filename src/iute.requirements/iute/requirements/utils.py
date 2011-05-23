from zope.app.component.hooks import getSite
from Products.CMFCore.utils import getToolByName
from uwosh.core.utils import *

from zope.i18nmessageid import MessageFactory
IuteRequirementsMF = MessageFactory('iute.requirements')
#from iute.requirements.utils import IuteRequirementsMF as _

def getProperties():
    return retrieve('iute_requirements_properties').properties
