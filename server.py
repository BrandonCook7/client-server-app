import socket

class Server():
    def __init__(self, port):
        self.port = port
        self.host = ""
    def run(self):
        sock = socket.socket()
        self.host = socket.gethostname()
        print("Socket Created")
        sock.bind((self.host, self.port))
        #Have 1 client listen to the server
        sock.listen(1)
         
        conn, address = sock.accept()
        while True:
            rec_data = conn.recv(4096).decode()
            if not rec_data:
                break
            print("Client: ", str(rec_data))
            print("To Client: ", end = " ")
            send_data = input()
            #Check to see if user inputted data
            if send_data:
                conn.send(send_data.encode())

        conn.close()

