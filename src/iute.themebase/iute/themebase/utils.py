from zope.app.component.hooks import getSite
from Products.CMFCore.utils import getToolByName
from uwosh.core.utils import *
from zope.i18nmessageid import MessageFactory
mf = MessageFactory('iute.themebase')

def getProperties():
    return retrieve('iute_theme_properties').properties
