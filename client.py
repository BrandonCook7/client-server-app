import socket

class Client():
    def __init__(self, port):
        self.port = port
        self.host = ""
    def run(self):
        sock = socket.socket()
        self.host = socket.gethostname()
        print("Socket Created")
        sock.connect((self.host, self.port))

        print("To Server: ", end = " ")
        send_data = input()
        check_exit = send_data.lower()
        while check_exit != "quit" or check_exit != "q":
            sock.send(send_data.encode())
            rec_data = sock.recv(4096).decode()
            print("Server: ", str(rec_data))
            print("To Server: ", end = " ")
            send_data = input()
            check_exit = send_data.lower()

        sock.close()
