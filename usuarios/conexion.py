import mysql.connector

def connectar():
    database = mysql.connector.connect(
        host="localhost",
        user = "root",
        passwd = "burr0510",
        database = "db_notas",
        port = 3306
    )
    cursor = database.cursor(buffered = True)

    return [database, cursor]
