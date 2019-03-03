import mysql.connector
from mysql.connector import errorcode
from getpass import getpass

hostname = input("Enter hostname:")
username = input("Enter username:")
password = getpass("Enter password:", stream=None)

try:
    mydb = mysql.connector.connect(host=hostname,
				    user=username,
				passwd=password)

    print("CONNECTED.")
    mycursor = mydb.cursor()
    try:
        mycursor.execute("SHOW DATABASES")
        result = mycursor.fetchall()
        print("All Database:")
        for x in result:
            print(x[0])
        database = input("Enter database to connect:")
        mydb.close()
        mydb = mysql.connector.connect(host=hostname,
				    user=username,
				passwd=password,
                                database=database)
        mycursor = mydb.cursor()
        mycursor.execute("SHOW TABLES")
        print("All Tables:")
        for x in mycursor.fetchall():
            print(x[0])
    except mysql.connector.Error as err:
        print(err)
except mysql.connector.Error as err:
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
    	print("ACCESS DENIED. Check username and password")
    else:
    	print("ERROR {}".format(err))
else:
	mydb.close()
	print("DISCONNECTED.")
