import socket


class Driver:
    def __init__(self, ip_address, ip_port):
        self.__ip_address = ip_address
        self.__ip_port = ip_port
        self.__open_tcp_connection()

    def connect_to_data_base(self, db_name):
        r"""Method that receives as input a name for a Angra DB db and makes
            connection to it

            Several sentences providing an extended description. Refer to
            variables using back-ticks, e.g. `var`.
            Parameters
            ----------
            db_name : string
                The variable `db_name` stands for the name of the db witch is to
                be connected
            Returns
            -------
            boolean
                ``boolean`` can only be true or false
            success : boolean
                `success` gets true whenever the connection occurs in a successful
                way, if it fails `success`.
        """

    def __open_tcp_connection(self):
        r"""Method that creates a tcp connection with AngraDB

            Several sentences providing an extended description. Refer to
            variables using back-ticks, e.g. `var`.
            Parameters
            ----------
            db_name : string
                The variable `db_name` stands for the name of the db witch is to
                be connected
            Raises
            ------
            BadException
                Because there has been a problem connecting to AngraDB
        """
        BUFFER_SIZE = 1024
        MESSAGE = "Hello, World!"
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((self.__ip_address, self.__ip_port))
        s.send(MESSAGE)
        data = s.recv(BUFFER_SIZE)
        s.close()
        print "received data:", data




