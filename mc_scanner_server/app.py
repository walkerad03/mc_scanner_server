"""
server_module.py - A simple server module for handling client
connections.

This module provides a basic implementation of a server using sockets.
It allows clients to connect to the server and sends a "Response"
message back to the client once the connection is established.

Example:
    >>> server = Server()
    >>> server.start()
    Connected by ('127.0.0.1', 54321)
"""

import socket


class Server:
    """
    Simple server class using sockets to handle client connections.

    This class provides a basic server implementation with the ability
    to listen for incoming client connections on a specified host and
    port. When a client connects, the server will send a "Response"
    message back to the client.

    Attributes:
        HOST (str): The IP address of the server.
        PORT (int): The port number the server will listen on.
    """
    def __init__(self) -> None:
        """
        Initialize the Server class.

        This constructor sets the server's host and port attributes.

        Attributes:
            HOST (str): The IP address of the server.
            PORT (int): The port number the server will listen on.
        """
        self.HOST = "127.0.0.1"
        self.PORT = 9797

    def start(self):
        """
        Start the server and listen for incoming connections.

        This method creates a socket, binds it to the server's host and
        port, and listens for incoming connections. When a connection is
        established, it sends a "Response" message to the client. After
        responding, the server goes back into listening mode until a
        KeyboardInterrupt breaks the loop.

        Note:
            This method will block until a connection is received.

        Raises:
            OSError: If there is an issue with creating or binding the
            socket.

        Example:
            >>> server = Server()
            >>> server.start()
            Connected by ('127.0.0.1', 54321)
        """
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
            s.bind((self.HOST, self.PORT))
            s.listen()
            try:
                while True:
                    conn, addr = s.accept()
                    with conn:
                        print(f"Connected by {addr}")
                        data = b"Response"
                        conn.sendall(data)
            except KeyboardInterrupt:
                s.close()


if __name__ == "__main__":
    server = Server()
    server.start()
