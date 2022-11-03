from server import *
from client import *
def main():
    server = Server(1234)
    server.run()

if __name__ == "__main__":
    main()
