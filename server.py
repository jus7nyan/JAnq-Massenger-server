
import socket
import selectors
import mh
from time import time
class Server:
    def __init__(self, port, msize):
        self.m_handler =mh.MH()
        
        self.port = port
        self.msize = msize

        self.selector = selectors.DefaultSelector()

        self.server_socet = socket.socket()
        self.server_socet.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEPORT, 1)
        self.server_socet.bind(("",self.port))
        self.server_socet.listen()
    
        self.selector.register(self.server_socet, selectors.EVENT_READ, data=self.accept_connect)
        
    def accept_connect(self, server_socet):
        client_socket, addr = server_socet.accept()
        print(f"{addr} connected!")
        client_socket.send("Enter room key and nick: ".encode())
        
        self.selector.register(client_socket, selectors.EVENT_READ, data=self.get_message)
    
    def get_message(self,client_socket):
        request = client_socket.recv(self.msize)
        if request:
            
            addr = client_socket.getpeername()
            msg = mh.Message(request, addr, time())

            self.m_handler.handle(msg, self)

    def send_message(self, msg:mh.Message):
        print(msg.text, msg.from_, msg.to_)
    
    def main_loop(self):
        while True:
            events = self.selector.select()
            
            for key, _ in events:
                callback = key.data
                callback(key.fileobj)

if __name__ == "__main__":
    s = Server(5001, 4096)
    s.main_loop()