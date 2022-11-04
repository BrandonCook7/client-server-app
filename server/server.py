import socket

class Server():
    def __init__(self, port):
        self.port = port
        self.host = ""
    def run(self):
        sock = socket.socket()
        sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.host = socket.gethostname()
        print("Socket Created")
        sock.bind((self.host, self.port))
        #Have 1 client listen to the server
        sock.listen(1)
        
        conn, address = sock.accept()
        while True:
            
            rec_data = conn.recv(1024).decode()
            if not rec_data:
                break
            if rec_data[0] == "$":
                #Client is sending a file
                file_name = rec_data[1:]
                print("Writing to " + file_name)
                f = open(file_name, 'w')
                rec_data = conn.recv(1024).decode()
                while rec_data != "":
                    f.write(rec_data)
                    print("Writing Data...")
                    if len(rec_data) == 1024:
                        rec_data = conn.recv(1024).decode()
                    else:
                        rec_data = ""
                f.close()
                print("Completed downloading file")
            else:
                print("Client: " + str(rec_data))

            print("To Client: ", end = "")
            send_data = input()
            if send_data:
                conn.send(send_data.encode())

        conn.close()

def main():
    server = Server(1234)
    server.run()

if __name__ == "__main__":
    main()
