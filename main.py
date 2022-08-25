from pydoc import cli
import MySQLdb, cliente

db = MySQLdb.connect(user="root", passwd="1234",db="treinaweb_clientes", host="localhost",port=3306, autocommit=True)


cursor = db.cursor()

def listar_cliente():
    cursor.execute("SELECT * FROM cliente")
    print(cursor.fetchall)


def inserir_cliente(cliente):
    cursor.execute("INSERT INTO cliente (nome, idade) values (%s, %s)", (cliente.nome, cliente.idade))
    

def editar_cliente(id_cliente, cliente):
    cursor.execute("UPDATE cliente SET nome=%(nome)s, idade=%(idade)s WHERE idcliente=%(id_cliente)s",
                   ({'nome':cliente.nome,'idade': cliente.idade, 'id_cliente': id_cliente}))
    
def remover_cliente(id_cliente):
    cursor.execute("DELETE FROM cliente WHERE idcliente=%s", (id_cliente, ))
    
cliente = cliente.Cliente("Joana",34)

listar_cliente()
inserir_cliente(cliente)
editar_cliente(1, cliente)
remover_cliente(7)



db.close()



