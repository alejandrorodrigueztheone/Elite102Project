import mysql.connector

def connect_db():
  return mysql.connector.connect{
    host='localhost',
    user = 'root',
    password = 'Ale30Ari13',
    database = 'ace_banking',
  }

try:

     con = mysql.connector.connect(**db_config)
     print("Connected to MySQL database")
     c = con.cursor()
  
  except mysql.connector.Error as err:
  print(f"Error: {err}")


if __name__=='__main__':
  conection=connect_to_db()
  print(conection)
  cursor=conection.cursor()
  cursor.execute("Select * FROM account_info")
  for x in cursor.fetchall():print(x)
