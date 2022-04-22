
class MessagesGet():
    def __init__(self,name):
        self.name = name
        
    
    def cal(self):
        if self.msg in ("hi","hello"):
            return f"hello {self.name}"
        else:
            return ''

class MessagesAndName(MessagesGet):
    def __init__(self,name,msg):
        self.msg = msg

        MessagesGet.__init__(self,name)

    def calling(self):
        if self.msg in ("hi","hello"):
            return f"hello {self.name}, your message is: {self.msg}"
        else:
            return "invalid input"

