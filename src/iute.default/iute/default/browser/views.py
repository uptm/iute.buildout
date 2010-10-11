from Products.Five.browser import BrowserView
from urllib import urlencode

class IUTEErrorsView(BrowserView):
    """
    a view to display all the recorded errors.
    """
    
    def assemble_url(self, url):
        return self.context.absolute_url() + '/@@reported-errors?' + urlencode({'view' : url})
    
    def get_errors(self):
        from iute.default import monkey
        return [(k, error) for k, error in monkey.ERRORS.items()]
        
    def error_to_view(self):
        return self.request.get('view', False)
        
    def get_error(self):
        from iute.default import monkey
        if monkey.ERRORS.has_key(self.request.get('view', None)):
            return monkey.ERRORS[self.request.get('view')]
