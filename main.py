import MySQLdb

db = MySQLdb.connect(user="root", passwd="1234",db="treinaweb_clientes", host="localhost",port=3306)


cursor = db.cursor()

cursor.execute("SELECT * FROM cliente")

print(cursor.fetchall())


print("CONEXÃO REALIZADA COM SUCESSO")

db.close()
