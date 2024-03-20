# Chat-Room
Chatroom for real time messageing and file transfer

STEPS:

1. Run the SERVER program
2. Run the CLIENT program in another terminal on the same system
3. The first CLIENT to join a SERVER can set a PASSWORD for the SERVER
4. All other CLIENTS joining the same SERVER must enter the right PASSWORD
5. Multiple CLIENTS can join the same SERVER (room) and group chat with one another
6. Each CLIENT must choose an ALIAS
7. Mechanism to PREVENT DUPLICATE ALIASES 
8. To send a MESSAGE, type it in normally
9.  Do NOT BEGIN with the ':' character
10. To EXIT the room enter ':Exit'
11. To send a FILE enter ':File <FILENAME>'
12. Ensure the FILE is in the SAME DIRECTORY or a DAUGHTER DIRECTORY to the CLIENT program sending it
13. Only use '/' and NOT '\' for PATH SEPERATORS
14. Ensure CLIENTS are present in DIFFERENT DIRECTORIES to prevent reading and writing the same file
15. Switch between messaging EVERYONE ':Dm All' and a SINGLE CLIENT ':Dm <ALIAS>'
16. Enter :Aliases to get a list of aliases connected to the server

The recieved file name is appended with 2 and the buffered file name is appended with 1
Done to ensure that testing is easier. we can execute all the programs in the same directory
Prevents read to and write from the same file simultaneously

The program is configured to use a signed certificate and a private key to implement ssl. 
Generate the necessary certificate and files
Ensure the naming of the files before running the program

Steps to generate a self signed certificate

1. openssl genrsa -aes256 -out private.key 2048
2. openssl rsa -in private.key -out private.key
3. openssl req -new -x509 -nodes -sha1 -key private.key -out certificate.crt -days 36500 -addext "subjectAltName=IP:<SERVER HOST IPV4>"
4. openssl req -x509 -new -nodes -key private.key -sha1 -days 36500 -out signedcert.pem -addext "subjectAltName=IP:<SERVER HOST IPV4>" 

Choose the desired length of the rsa key you want to generate. 4098 or 2048 or whatever
Choose the validity of the certificate. here we do so in days
Enter the IPV4 address on which the server is to run
Add the certificate.crt file generate onto the Trusted Root Certification Authorities\Certificates directory
The server requires the .pem and the .key files both
The client requires the .pem file
Ensure they are in the same directories as the server and client programs
Alternatively modify client ans server programs to reflect the locations of the .key and .pem files

REFERENCES:

1. TCP chat application
https://dev.to/bekbrace/network-programming-in-python-2-projects-34nk

2. SSL implementation
https://www.youtube.com/watch?v=N4utwloVeOE
