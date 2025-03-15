#import socket module
from socket import *
import sys

serverSocket = socket(AF_INET, SOCK_STREAM)
serverPort = 6789   #C
#Prepare a sever socket
serverSocket.bind(('0.0.0.0', serverPort))  #C
#Fill in start
#Fill in end
print(f"Server is running on port {serverPort}...")

serverSocket.listen(1)  




while True:
    #Establish the connection
    print('Ready to serve...')
    connectionSocket, addr = serverSocket.accept()  #Fill in start            #Fill in end 
             
    try:
            # 3.3DONE
        message = connectionSocket.recv(1024).decode("UTF-8")   #Fill in start          #Fill in end               
        filename = message.split()[1]                 
        with open(filename[1:], "r", encoding="utf-8") as f:                        
            outputdata =  f.read() #Fill in start       #Fill in end 
            #  3.4
        #Send one HTTP header line into socket
        connectionSocket.send("HTTP/1.1 200 OK\r\nContent-Type: text/html\r\n\r\n".encode()) 

        #Fill in start
        #Fill in end       
        # 
        if not message:  
            raise ConnectionAbortedError("Client disconnected unexpectedly.")         
        
        #Send the content of the requested file to the client
        for i in range(0, len(outputdata)):           
            connectionSocket.send(outputdata[i].encode())
        
        connectionSocket.send("\r\n".encode())
           
           
           # connectionSocket.close()

    except (ConnectionResetError, ConnectionAbortedError) as e:
        print(f"Connection error: {e}")
        connectionSocket.close()
        continue
    
    except IOError:
        #Send response message for file not found
        
        connectionSocket.send("HTTP/1.1 404 Not Found\r\nContent-Type: text/html\r\n\r\n".encode()) 
        #connectionSocket.send("<html><body><h1>404 Not Found </h1></body></html>".encode()) 


        connectionSocket.send(
                      b"<html><body><h1>404 Not Found</h1>"
                      b"<pre>"
                      b"       ,___          .-;'                       \n"
                      b"       `\"-.`\\_...._/`.`   ___________                    \n"
                      b"    ,      \\        /    /            \       \n"
                      b" .-' ',    / ()   ()\\   |  Pika Pika! |        \n"
                      b"`'._   \\  /()    .  (|   \____________/                 \n"
                      b"    > .' ;,     -'-  /  __ /                         \n"
                      b"   / <   |;,     __.;  \n"
                      b"   '-.'-.|  , \\    , \\  \n"
                      b"      `>.|;, \\_)    \\_)  \n"
                      b"       `-;     ,    /  \n"
                      b"          \\    /   <  \n"
                      b"           '. <`'-,_)  \n"
                      b"            '._)  \n"
                      b"</pre>"
                      b"</body></html>")

        connectionSocket.close() 
        #Fill in start        
        
        #Fill in end
        #Close client socket
        
        #Fill in start 
        #Fill in end 
                   

    #GOT RID OF THESE TWO LINES TO MAKE IT RUN INDEFINITELY
    #serverSocket.close()   
    #sys.exit()#Terminate the program after sending the corresponding data                                    
