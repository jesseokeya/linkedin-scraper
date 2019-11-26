class Helper:
    def __init__(self, url: str):
        self.url = url
    
    def handle_error(self, e: Exception, message: str = 'Error Occured'):
        print(e, message)