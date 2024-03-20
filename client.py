
#Client.py
import threading
import socket
import sys
import time
import getpass
import ssl

cert_path=r"C:\Users\rishi\chatsproj.com.crt"
alias=""
ctxt=ssl.SSLContext(ssl.PROTOCOL_TLS_CLIENT)
ctxt.load_verify_locations(cert_path)
ctxt.check_hostname= False 
ctxt.verify_mode=ssl.CERT_NONE
soc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#wrapping of socket with SSL/TLS
client=ctxt.wrap_socket(soc,server_hostname='192.168.170.182')
client.connect(('192.168.29.141', 60000))
exit_flag=True

def client_receive():
    global exit_flag
    global alias
    while exit_flag:
        try:
            message = client.recv(1024).decode('utf-8')
            #The first three cases are for handling CLIENTS joining the SERVER
            if message == "Password?":
                #Getpass doesnt display the password typed
                password=getpass.getpass('Enter the Password >>> ');
                client.send(password.encode('utf-8'))
                continue
            elif message == "alias?":
                alias = input('Choose an alias >>> ')
                client.send(alias.encode('utf-8'))
                continue
            #The EXIT command is also handled here
            elif message == "Incorrect Password" or message ==":Exit":
                if message == "Incorrect Password":
                    print("You entered the incorrect password")
                print("Exiting the program")
                exit_flag=False
                client.close();
                continue
            elif message[0:5]==":File":
                #This handles recieving files from the server
                fname="2"+message[6:]
                with open(fname,'wb') as f:
                    while True:
                        data=client.recv(2048)
                        if data=="***END***".encode("utf-8"):
                            break
                        f.write(data)
            #connection confimed and send function started
            elif message=="ALIAS ACCEPTED":
                send_thread.start()
            #else prints normal messages
            else:
                print(message)
        except:
            print('Error!')
            exit_flag=False
            client.close()
            break

def client_send():
    global exit_flag
    while exit_flag:
        message = input("")
        #checks exit flag to pevent sending messages after closing connection
        if exit_flag:
            if message[0:5]==':File':
                print("Sending File");
                fname=message[6:]
                #The below is a loop to send the file to the server
                try:
                    #This is to check for the existance of a file before we begin sending it
                    with open(fname,'rb') as f:
                        pass
                    client.send(message.encode('utf-8'))
                    time.sleep(0.1)
                    with open(fname,'rb') as f:
                        while True:
                            data=f.read(2048)
                            #print(data)
                            if not data:
                                break
                            client.send(data)
                    #This signals the server to exit the recieving loop
                    time.sleep(1)
                    client.send("***END***".encode('utf-8'));
                    print("File sent")
                except FileNotFoundError:
                    print("File Not Found")
                except Exception as e:
                    print("An error occured")
                    print(e)
            #handles sending normal messages
            else:
                client.send(message.encode('utf-8'))
          
#We create two threads one for recieving messages from the server          
receive_thread = threading.Thread(target=client_receive)
receive_thread.start()
#And another to send messages to the server
send_thread = threading.Thread(target=client_send)
