import mysql.connector
db = mysql.connector.connect(
    host="localhost",
    user="usuario",
    passwd="senha"
)
print(db)
# <mysql.connector.connection.MySQLConnection object at 0x7f66da2a7550>
