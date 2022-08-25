import MySQLdb

class FabricaConexao():
    
    @staticmethod
    def conectar():
        db = MySQLdb.connect(user="root", passwd="1234",db="treinaweb_clientes", host="localhost",port=3306, autocommit=True)
        return db