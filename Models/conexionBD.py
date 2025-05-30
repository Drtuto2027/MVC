import mariadb as sql

class ConexionDB():
    def __init__(self):
        self.__host = "localhost"
        self.__port = 3307
        self.__user = "root"
        self.__password = ""
        self.__database = "ejemplo"
        self.__conecction = None

    def getConnection(self):
        return self.__conecction
    
    def crearConexion(self):
        self.__conecction = sql.connect(
            host = self.__host,
            user = self.__user,
            password = self.__password,
            port = self.__port,
            database = self.__database
        )

    def cerrarConexion(self):
        if self.__conecction:
            self.__conecction.close()
            self.__conecction = None