from interfaces import IGoLiveCheck
from zope.app.component.hooks import getSite
from plone.app.viewletmanager.interfaces import IViewletSettingsStorage
from zope.interface import implements
from zope.component import getUtility
from Products.Five.testbrowser import Browser
from Products.CMFCore.utils import getToolByName
from iute.core.utils import *
from iute.requirements.utils import IuteRequirementsMF as _

CHECKS = []

def registerCheck(check):
    
    if check not in CHECKS:
        CHECKS.append(check)

class CheckEmail:
    
    implements(IGoLiveCheck)
    
    name = _(u"Email")
    description = _(u"Must set site from address in Mail Settings")
    fixinginfo = _(u"""Go to <a href='@@mail-controlpanel'>Mail Settings</a> and set the required information.""")
    
    def use(self):
        """
        always use
        """
        return True
    
    def passes(self):
        site = getSite()
        
        from_address = site.email_from_address
        
        return len(from_address) > 0
        
registerCheck(CheckEmail)

class CheckShouldShowUWBanner:
    implements(IGoLiveCheck)
    
    name = _(u"Show Banner")
    description = _(u"Must show IUTE Banner")
    fixinginfo = _(u""" Go to <a href='@@iute.theme.configuration'>iute theme configuration</a> and show the banner. """)
    
    def use(self):
        return has.product("iute.themebase").installed()
    
    def passes(self):
                    
        site = getSite()
        
        viewlet = "iute.theme.base.banner"
        manager = "plone.portaltop"

        storage = getUtility(IViewletSettingsStorage)
        skinname = site.getCurrentSkinName()
        hidden = storage.getHidden(manager, skinname)

        return viewlet not in hidden

#registerCheck(CheckShouldShowUWBanner)

class CheckShouldShowSearchBox:
    implements(IGoLiveCheck)
    
    name = _(u"Show Search Box")
    description = _(u"Must show search box")
    fixinginfo = _(u""" Go to <a href='@@manage-viewlets'>manage viewlets</a> and show the search box. """)
    
    def use(self):
        return True
    
    def passes(self):
        site = getSite()
        
        viewlet = "plone.searchbox"
        manager = "plone.portalheader"

        storage = getUtility(IViewletSettingsStorage)
        skinname = site.getCurrentSkinName()
        hidden = storage.getHidden(manager, skinname)

        return viewlet not in hidden

#depreciated since the search is now in the banner viewlet
#registerCheck(CheckShouldShowSearchBox)

class CheckShouldShowIUTEFooter:
    implements(IGoLiveCheck)
    
    name = _(u"Show IUTE Footer")
    description = _(u"Must show IUTE footer")
    fixinginfo = _(u""" Go to <a href='@@manage-viewlets'>manage viewlets</a> and show the iute.theme.base.footer viewlet. """)
    
    def use(self):
        return has.product("iute.themebase").installed()
    
    def passes(self):
        site = getSite()
        
        viewlet = "iute.theme.base.footer"
        manager = "plone.portalfooter"

        storage = getUtility(IViewletSettingsStorage)
        skinname = site.getCurrentSkinName()
        hidden = storage.getHidden(manager, skinname)

        return viewlet not in hidden

#registerCheck(CheckShouldShowIUTEFooter)

class CheckNeedsClickableLinkInFooter:
    implements(IGoLiveCheck)
    
    name = _(u"Clickable Link In Footer")
    description = _(u"Must have clickable link in footer")
    fixinginfo = _(u""" Go to <a href='@@iute.theme.configuration'>iute theme configuration</a> and add link to www.iute.tec.ve in the footer. """)
    
    def use(self):
        return has.product("iute.theme").installed()
    
    def passes(self):
        site = getSite()
        
        #in case iute theme isn't installed
        props = retrieve('iute_theme_properties').properties
        footer = None
        if props:
            footer = props.footer

        if not footer or len(footer) == 0:
            return False

        if footer.find('href=') >= 0 and footer.find('www.iute.tec.ve') >= 0:
            return True
        else:
            return False

#depreciated since there is no longer needed a link in the footer
#registerCheck(CheckNeedsClickableLinkInFooter)

class CheckNeedsSiteMapAccessiblityAndContactLinks:
    implements(IGoLiveCheck)
    
    name = _(u"Missing Required Links")
    description = _(u"Must show site map, accessiblity, and contact links on page")
    fixinginfo = _(u""" Go to <a href='portal_actions/manage_main'>ZMI</a> and the links back in portal_actions. """)
    
    def use(self):
        return True
    
    def passes(self):
        site = getSite()
        atool = getToolByName(site, 'portal_actions')
        actions = atool.listFilteredActionsFor(site)['site_actions']
        
        foundSiteMap = False
        foundAccessiblity = False
        foundContact = False
        
        for action in actions:
            if action['title'] == u"Site Map" and action['visible']:
                foundSiteMap = True
            elif action['title'] == u'Accessibility' and action['visible']:
                foundAccessibility = True
            elif action['title'] == u'Contact' and action['visible']:
                foundContact = True
            
        return foundSiteMap and foundAccessibility and foundContact

registerCheck(CheckNeedsSiteMapAccessiblityAndContactLinks)

class CheckViewAbout:
    implements(IGoLiveCheck)
    
    name = _(u"View About")
    description = _(u"Anyone must be allowed to view about information")
    fixinginfo = _(u""" Go to <a href='@@security-controlpanel'>security settings</a> and check 'Allow anyone to view 'about' information'. """)
    
    def use(self):
        return True
    
    def passes(self):
        site = getSite()
        pprops = getToolByName(site, 'portal_properties')
        
        return pprops.site_properties.allowAnonymousViewAbout

registerCheck(CheckViewAbout)

class CheckExposeSiteMap:
    implements(IGoLiveCheck)
    
    name = _(u"Expose sitemap.xml.gz")
    description = _(u"Must expose site map")
    fixinginfo = _(u""" Go to <a href='@@site-controlpanel'>site settings</a> and check 'Expose sitemap.xml.gz in the portal root'. """)
    
    def use(self):
        return True
    
    def passes(self):
        site = getSite()
        pprops = getToolByName(site, 'portal_properties')
        
        return pprops.site_properties.enable_sitemap

registerCheck(CheckExposeSiteMap)

class CheckSiteDescription:
    implements(IGoLiveCheck)
    
    name = _(u"Site Description")
    description = _(u"Must have a site description")
    fixinginfo = _(u""" Go to <a href='@@site-controlpanel'>site settings</a> and fill in a site description. """)
    
    def use(self):
        return True
    
    def passes(self):
        site = getSite()
        return len(site.description) > 0

registerCheck(CheckSiteDescription)

class CheckCSSDebugging:
    implements(IGoLiveCheck)

    name = _(u"CSS Debugging")
    description = _(u"Must have CSS debugging turned off")
    fixinginfo = _(u""" Go to <a href='portal_css/manage_cssForm'>ZMI</a> -> portal_css and uncheck 'Debug/development mode'. """)

    def use(self):
        return True

    def passes(self):
        site = getSite()
        pcss = getToolByName(site, 'portal_css')
        return not pcss.getDebugMode()

registerCheck(CheckCSSDebugging)

class CheckJSDebugging:
    implements(IGoLiveCheck)

    name = _(u"JS Debugging")
    description = _(u"Must have JS debugging turned off")
    fixinginfo = _(u""" Go to <a href='portal_javascripts/manage_jsForm'>ZMI</a> -> portal_javascripts and uncheck 'Debug/development mode'. """)

    def use(self):
        return True

    def passes(self):
        site = getSite()
        pjs = getToolByName(site, 'portal_javascripts')
        return not pjs.getDebugMode()

registerCheck(CheckJSDebugging)

class CheckCacheSetupInstalled:
    implements(IGoLiveCheck)

    name = _(u"CacheSetup Installed")
    description = _(u"Must have CacheSetup installed")
    fixinginfo = _(u""" Go to <a href='prefs_install_products_form'>Add-On Products</a> -> install CacheSetup. """)

    def use(self):
        return True

    def passes(self):
        site = getSite()
        pq = getToolByName(site, 'portal_quickinstaller')
        return pq.isProductInstalled("CacheSetup")

registerCheck(CheckCacheSetupInstalled)

class CheckCacheFuEnabled:
    implements(IGoLiveCheck)

    name = _(u"CacheFu Enabled")
    description = _(u"Must have CacheFu enabled")
    fixinginfo = _(u""" Go to the <a href='portal_cache_settings'>Cache Configuration Tool</a> -> and check 'Enable CacheFu'. """)
    


    def use(self):
        site = getSite()
        pq = getToolByName(site, 'portal_quickinstaller')
        return pq.isProductInstalled("CacheSetup")

    def passes(self):
        site = getSite()
        pcs = getToolByName(site, 'portal_cache_settings')
        return pcs.getEnabled()

registerCheck(CheckCacheFuEnabled)

class CheckNotLetUsersSelectOwnPasswords:
    implements(IGoLiveCheck)

    name = _(u"Let Users Select Passwords")
    description = _(u"Must not let users select their own password")
    fixinginfo = _(u""" Go to <a href='@@security-controlpanel'>site security</a> and uncheck the box labled 'Let users select their own passwords'. """)

    def use(self):
        return True

    def passes(self):
        site = getSite()

        return site.validate_email

registerCheck(CheckNotLetUsersSelectOwnPasswords)

class CheckMailHostMustBeSet:
    implements(IGoLiveCheck)

    name = _(u"Mail Server")
    description = _(u"Mail Server host must be set to smtp.iute.tec.ve")
    fixinginfo = _(u""" Go to <a href='@@mail-controlpanel'>mail settings</a> enter 'smtp.iute.tec.ve' as the mail host. """)

    def use(self):
        return True

    def passes(self):
        site = getSite()

        return site.MailHost.smtp_host == "smtp.iute.tec.ve"

registerCheck(CheckMailHostMustBeSet)

class CheckLoginFormInCustom:
    implements(IGoLiveCheck)
    
    name = _(u"Use Campus Login Form")
    description = _(u"Must use the campus login form")
    fixinginfo = _(u""" Go to <a href='portal_skins/custom/manage_main'>the custom folder</a> and delete login_form. """)
    
    def use(self):
        return has.product("iute.themebase").installed()
    
    def passes(self):   
        site = getSite()
        ps = getToolByName(site, 'portal_skins')
        custom = ps['custom']
        return 'login_form' not in custom.objectIds()

registerCheck(CheckLoginFormInCustom)

class CheckMustClickReadyToGoLive:
    implements(IGoLiveCheck)

    name = _(u"Go Live")
    description = _(u"Notify iute staff you are ready to go live")
    fixinginfo = _(u""" Go to <a href='@@iute-requirements'>iute requirements</a>, enter the plone project url and click 'ready to go live'. """)

    def use(self):
        return True

    def passes(self):
        site = getSite()

        viewlet = "iute.allowedlive"
        manager = "plone.portaltop"

        storage = getUtility(IViewletSettingsStorage)
        skinname = site.getCurrentSkinName()
        hidden = storage.getHidden(manager, skinname)

        return viewlet in hidden

registerCheck(CheckMustClickReadyToGoLive)

