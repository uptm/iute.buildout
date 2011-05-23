from zope.app.component.hooks import getSite
from Products.CMFCore.utils import getToolByName
from zope.component import queryUtility

class product:
    """
    
    >>> from iute.core.utils import has
    >>> has.product('iute.default').installed()
    False
    
    >>> has.product('iute.default').available()
    True
    >>> has.product('iute.default').installable()
    True
    
    >>> from iute.core.utils import install
    >>> install.these(['iute.default']).dependencies()
    
    >>> has.product('iute.core').installed()
    True
    
    """
    def __init__(self, product):
        self.product = product
        site = getSite()
        self.qi = getToolByName(site, 'portal_quickinstaller')
        
    def installed(self):
        return self.qi.isProductInstalled(self.product)
        
    def installable(self):
        return self.qi.isProductInstallable(self.product)
        
    def available(self):
        return self.qi.isProductAvailable(self.product)
        
        
class viewlet:
    """
    These aren't implemented yet, but would be nice to have.
    """
    def __init__(self, viewlet, manager):
        self.viewlet = viewlet
        self.manager = manager
        
    def hidden(self):
        pass
        
    def shown(self):
        pass
