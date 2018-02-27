# -*- coding: utf-8 -*-
import time
import socket
from CMDSupport import *

class Server(object):
    sock=None
    connect=None

    def __init__(self):
        pass

    def check_tcp_status(self,ip="127.0.0.1", port=12345):
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server_address = (ip, port)
        print ('Connecting to %s:%s.' % server_address)
        self.sock.connect(server_address)
        message = "I'm TCP client self"
        print ('Sending "%s".' % message)
        self.sock.sendall(message.encode("utf-8"))      
        pass
    
    def close(self): 
        print ('Closing socket.')
        if self.sock is not None:
            self.sock.close()
        self.sock=None
        pass

    def send(self,msg):
        self.sock.sendall(msg.encode("utf-8"))
        pass

    def recv(self):
        data = self.sock.recv(1024).decode("utf-8")
        print ("Receive \n'%s'" % data)
        return data        
        pass


        
        
cmddemo = CMDSupport()
while True:
    try:
        
        demo = Server()
        demo.check_tcp_status()
        while True:
            try:
                str_cmd=demo.recv()
                print("cmd:",str_cmd)
                rtn = cmddemo.excute_cmd(str_cmd)
                rtn = "\n-----输出begin-----\n\n" + rtn + "\n-----输出end-----\n"
                print("rtn",rtn)
                demo.send(rtn)
            except:
                break
    except:
        pass
    finally:
        demo.close()
        time.sleep(1)
    pass
