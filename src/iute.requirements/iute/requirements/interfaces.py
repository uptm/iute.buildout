from zope.interface import Interface, Attribute
from zope import schema

from plone.theme.interfaces import IDefaultPloneLayer

from iute.requirements.utils import IuteRequirementsMF as _

class IIUTERequirementsLayer(Interface):
    """Marker interface that defines a browser layer
    """


class IGoLiveCheck(Interface):
    
    name = Attribute(_(u"The name of the check"))
    description = Attribute(_(u"articulated description of the check"))
    fixinginfo = Attribute(_(u"information on how to fix the problem"))
    
    def passes(self):
        """
        returns boolean on if it passes
        """
        
    def use(self):
        """
        defines if the check should be used or not
        """
