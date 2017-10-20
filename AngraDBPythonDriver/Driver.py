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
        response = self.__send_to_server(request)
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
        response = self.__send_to_server(request)
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
        response = self.__send_to_server(request)
        # This is required because the id comes from the server with quotes
        response = self.__remove_quote_and_new_line(response)
        return response

    def lookup_document(self, doc_id):
        r"""Method that receives as input a id for a document and
            returns it

            Parameters
            ----------
            doc_id : string
                The variable `doc_id` stands for the id of the document
                to be looked up
            Returns
            -------
            response : string
                `response` gets the id of the document.
        """
        request = "lookup " + doc_id
        response = self.__send_to_server(request)
        return response

    def update_document(self, doc_id, document):
        r"""Method that receives as input a id for a document, a document
            and updates its value

            Parameters
            ----------
            doc_id : string
                The variable `doc_id` stands for the id of the document
                to be looked up
            document : string
                The variable `document` stands for the document witch is
                going to replace the current document

            Returns
            -------
            response : string
                `response` gets the server response.
        """
        request = "update " + doc_id + " " + document
        response = self.__send_to_server(request)
        return response

    # Private methods

    def __remove_quote_and_new_line(self, string):
        r"""Method that receives as input a string and returns a version
        of it without quotes

            Parameters
            ----------
            string : string
                The variable `string` stands for the text to be formated
            Returns
            -------
            response : string
                `response` gets string without quotes.
        """
        return string.replace('"', "").replace('\n', "")

    def __send_to_server(self, request):
        r"""Method that receives as input a request to be sent to
            the angra db server and returns its response

            Parameters
            ----------
            request : string
                The variable `request` stands for the text to be sent
                to the angra db server
            Returns
            -------
            response : string
                `response` gets the server response.
        """
        self.__session.send(request)
        response = self.__session.recv(Driver.BUFFER_SIZE)
        return response

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



