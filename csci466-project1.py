from socket import *

msg = "\r\n I love computer networks!"
endmsg = "\r\n.\r\n"

mailserver = ('list.winthrop.edu', 25)

clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect(mailserver)

recv = clientSocket.recv(1024).decode()
print(recv)
if recv[:3] != '220':
    print('220 reply not received from server.')

helloCommand = 'HELLO \r\n'
clientSocket.send(helloCommand.encode())
recv1 = clientSocket.recv(1024).decode()
print(recv1)
if recv1[:3] != '250':
    print('250 reply not received from server.')

mailFrom = "MAIL FROM: <woodm15@winthrop.edu> \r\n"
clientSocket.send(mailFrom.encode())
recv2 = clientSocket.recv(1024).decode()
print (recv2)
if recv2[:3] != '250':
    print('250 reply not received from server.')

rcptTo = 'RCPT TO: <woodm15@winthrop.edu \r\n'
clientSocket.send(rcptTo.encode())
recv3 = clientSocket.recv(1024).decode()
print(recv3)
if recv3[:3] != '250':
    print('250 reply not received from server.')

data = "DATA\r\n"
clientSocket.send(data.encode())
recv4 = clientSocket.recv(1024) 
if recv4[:3] != '250':
    print('250 reply not received from server.')

subject = "SMTP mail client program"
clientSocket.send(subject.encode())
message = ("Test123 \r\n")
clientSocket.send(message.encode())
clientSocket.send(endmsg.encode())
recv5 = clientSocket.recv(1024)
if recv5[:3] != '250':
    print('250 reply not received from server after sending message.')

quit = "QUIT\r\n"
clientSocket.send(quit.encode())
recv6 = clientSocket.recv(1024)
print (recv6)
clientSocket.close()