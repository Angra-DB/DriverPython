import socket


class Driver:
    """
        Array with associated photographic information.
        ...
        Attributes
        ----------
        __ip_address : string
                    ip address for connection with AngraDB.
        __ip_port : int
                    port for connection with AngraDB
        __session : Socket
                    Exposure in seconds.

        Methods
        -------
        connect_to_data_base(db_name)
        __open_tcp_connection()
        __close_tcp_connection()
    """

    """
    Constant that defines the size of the buffer on the tcp
    connection 
    """
    BUFFER_SIZE = 1024


    def __init__(self, ip_address, ip_port):
        self.__ip_address = ip_address
        self.__ip_port = ip_port
        self.__session = None
        self.__open_tcp_connection()

    def __del__(self):
        self.__close_tcp_connection()

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

            Raises
            ------
            BadException
                Because there has been a problem connecting to AngraDB
        """
        self.__session = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.__session.connect((self.__ip_address, self.__ip_port))
        # self.__session.send(message)
        # data = self.__session.recv(buffer_size)
        # print "received data:", data

    def __close_tcp_connection(self):
        r"""Method that destroys a tcp connection with AngraDB


            Raises
            ------
            BadException
                Because there has been a problem closing the connection
                to AngraDB
        """
        self.__session.close()



