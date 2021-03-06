import socket
import sys

msg = ['','']
flag = [0, 0]

def listen_thread(IP,index):
# Create a TCP/IP socket
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Bind the socket to the port
    #server_address = ('localhost', 10000)
    print ('starting up on %s port %s' % IP)
    sock.bind(IP)

    # Listen for incoming connections
    sock.listen(1)

    while True:
        # Wait for a connection
        print ( 'waiting for a connection')
        connection, client_address = sock.accept()
        msg[index] = ''
        flag[index] = 0
        try:
            print('connection from', client_address)

            # Receive the data in small chunks and retransmit it
            while True:
                data = connection.recv(16)
                print ('received "%s"' % data)
                if data:
                    flag[index] = 1
                    msg[index] += data
                    print ('sending data back to the client')
                    #connection.sendall(data)
                else:
                    print('no more data from', client_address)
                    break
                
        finally:
            # Clean up the connection
            connection.close()
