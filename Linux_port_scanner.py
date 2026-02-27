#Beginners locally ports scanner, check the range you want by changing the code range
import socket 
from _datetime import datetime  #given library can be replace with system datetime

ip = input("Enter target IP address: ")

def port_scan(target):
    try:
        print(f"time started",datetime.now())
        for port in range(20, 90):
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)# Creates a TCP socket (IPv4 + TCP)
            sock.settimeout(1)# set timer for packet
            result = sock.connect_ex((ip, port)) # connect to that port. Returns 0 if 
                           open, otherwise a non-zero error code.

            if result == 0:
                print("Port {}: Open".format(port))
            sock.close()#connection termination (security important issue)
                               sockets).
    except socket.error: #connection error 
        print("could not connect to the server")

port_scan(target)
