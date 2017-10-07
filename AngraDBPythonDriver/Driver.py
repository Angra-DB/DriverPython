import socket


class Driver:
    """
        Python Library to interface with angraDB
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

            Parameters
            ----------
            db_name : string
                The variable `db_name` stands for the name of the db witch is to
                be connected
            Returns
            -------
            response : string
                `response` gets the server response whenever the connection occurs
                in a successful way.
        """
        request = "connect " + db_name
        self.__session.send(request)
        response = self.__session.recv(Driver.BUFFER_SIZE)
        return response

    def create_data_base(self, db_name):
        r"""Method that receives as input a name and creates a db on AngraDB

            Parameters
            ----------
            db_name : string
                The variable `db_name` stands for the name of the new db to be
                created
            Returns
            -------
            response : string
                `response` gets the server response whenever the connection occurs
                in a successful way.
        """
        request = "create_db " + db_name
        self.__session.send(request)
        response = self.__session.recv(Driver.BUFFER_SIZE)
        return response

    def save_document(self, document):
        r"""Method that receives as input a document and saves it on a
            AngraDB db

            Parameters
            ----------
            document : string
                The variable `document` stands for the document to be saved on the
                db
            Returns
            -------
            response : string
                `response` gets the server response.
        """
        request = "save " + document
        self.__session.send(request)
        response = self.__session.recv(Driver.BUFFER_SIZE)
        return response

    def lookup_document(self, id):
        r"""Method that receives as input a id for a document and
            returns it

            Parameters
            ----------
            id : string
                The variable `id` stands for the id of the document
                to be looked up
            Returns
            -------
            response : string
                `response` gets the server response.
        """
        request = "lookup " + id
        self.__session.send(request)
        response = self.__session.recv(Driver.BUFFER_SIZE)
        return response

    # Private methods

    def __open_tcp_connection(self):
        r"""Method that creates a tcp connection with AngraDB

            Raises
            ------
            BadException
                Because there has been a problem connecting to AngraDB
        """
        self.__session = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        try:
            self.__session.connect((self.__ip_address, self.__ip_port))
        except socket.error, msg:
            print "Couldnt connect with the socket-server: %s\nTerminating program" % msg
            exit(1)

    def __close_tcp_connection(self):
        r"""Method that destroys a tcp connection with AngraDB

            Raises
            ------
            BadException
                Because there has been a problem closing the connection
                to AngraDB
        """
        try:
            self.__session.close()
        except socket.error, msg:
            print "Couldnt close the connection with the socket-server: %s\nTerminating program" % msg
            exit(1)



