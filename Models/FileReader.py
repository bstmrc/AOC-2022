class FileReader:
    def __init__(self, route, content):
        self.route = route
        self.content = content
    
    def read_file(self):
        file = open(self.route, "r")
        self.content = file.read()
        file.close()