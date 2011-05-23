from zope.interface import Interface

class IIUTETools(Interface):
    """A view that gives access to common tools
    """
    
    def get_last_modified_header():
        """
        """
    
    def set_last_modified_header():
        """
        
        """
        
    def get_copyright_holder():
        """
        
        """
        
    def get_current_year():
        """
        """
        
    def iute_login_url():
        """"""
        
    def iute_login_without_ssl():
        """"""
        
    def iute_home_url():
        """"""
        
    
