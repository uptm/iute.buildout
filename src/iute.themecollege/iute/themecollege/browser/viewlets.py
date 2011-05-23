from zope.app.component.hooks import getSite
from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile
from plone.app.layout.viewlets.common import ViewletBase
from Products.CMFCore.utils import getToolByName

class SiteTitle(ViewletBase):
    render = ViewPageTemplateFile('sitetitle.pt')

    def update(self):
        portal_url = getToolByName(self.context, "portal_url")
        portal = portal_url.getPortalObject()
        
        self.title = portal.title
        
