
class MockMailHost:
    
    def __init__(self):
        self.messages = []
        self.smtp_host = "mail.cenditel.gob.ve"
        
    def secureSend(self, message, to, mfrom, subject):
        self.messages.append({
            'message': message,
            'to': to,
            'from': mfrom,
            'subject': subject            
        })
        
        
