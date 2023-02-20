class Message:
    def __init__(self, request, from_, time):
        self.text = request.decode()
        self.from_ = from_
        self.time = time

    def __str__(self):
        return self.text

    def add_to_(self, to_):
        self.to_ = to_
        
    
class MH:
    def __init__(self):
        self.users = {}
        self.rooms = {}
        # preps
        #   rm - message to room
        #   sm - settings message to server (new room, etc.)
        #   im - info req message to server (info about room, info about server)

    def handle(self, msg:Message, server):
        prep = str(msg)[0]+str(msg)[1]
        msg.add_to_("hahaha")
        server.send_message(msg)
        
