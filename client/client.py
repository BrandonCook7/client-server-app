import socket

choice_strings = ['m', 'f', 'quit']


class Client():
    def __init__(self, port):
        self.port = port
        self.host = ""

    def send(self, sock, send_data):
        choice = ""
        while(choice.lower() not in choice_strings):
            print("Send a message or file (M/F)?: ")
            choice = input()
        if choice.lower() == "m":
            print("To Server: ", end = "")
            send_data = input()
            if send_data.lower() == "quit":
                print("Shutting Down...")
                return -1
            else:
                sock.send(send_data.encode())
            
        elif choice.lower() == "f":
            print("Enter File Name -> ", end = "")
            send_data = input()
            
            file_loc = send_data
            f = open(file_loc, 'rb')
            modded_data = "$" + f.name
            sock.send(modded_data.encode())

            read = f.read(1024)
            while(read):
                print("Sending Data...")
                sock.send(read)
                read = f.read(1024)
            f.close()
            print("Sent " + f.name + " to server")
        elif choice.lower() == "quit":
            print("Shutting Down...")
            return -1

    def recieve(self, sock):
        rec_data = sock.recv(1024).decode()
        if rec_data[0] == "$":
            #Client is sending a file
            file_name = rec_data[1:]
            print("Writing to " + file_name)
            f = open(file_name, 'w')
            rec_data = sock.recv(1024).decode()
            while rec_data != "":
                f.write(rec_data)
                print("Writing Data...")
                if len(rec_data) == 1024:
                    rec_data = sock.recv(1024).decode()
                else:
                    rec_data = ""
            f.close()
            print("Completed downloading file")
        else:
            print("Server: " + str(rec_data))

    def run(self):
        sock = socket.socket()
        self.host = socket.gethostname()
        print("Socket Created")
        sock.connect((self.host, self.port))
        #print("If you want to send a file type $ and then the file's location")
        # print("To Server: ", end = " ")
        #send_data = input()
        send_data = ""
        while send_data.lower() != "quit":
            if self.send(sock, send_data) == -1:
                break
            self.recieve(sock)
        sock.close()

def main():
    client = Client(1234)
    client.run()

if __name__ == "__main__":
    main()
