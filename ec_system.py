import os
import sqlite3
con = sqlite3.connect('example.db')
c = con.cursor()

path = '/Users/somahisai/Desktop/ec_system/example.db'
if not (os.path.isfile(path)):
  c.execute("""
    CREATE TABLE users (
      id INTEGER PRIMARY KEY AUTOINCREMENT,
      name STRING,
      email STRING,
      age INTEGER
    )
  """)


while(True):
  #01 Exec page
  print("""
    === EXEC PAGE ===
    exec list:
    1. User Create.
    2. User Edit.
    3. User Delete.
    4. User List.
    5. Item Create.
    6. Item Edit.
    7. Item Delete.
    8. Item List.
    9. To Item Buy Mode.
    10. To Item Buy Histories Mode.
    11. To Total Amount Aggregation Mode.
    12. System Exit.
    exec:
  """)

  num = input('exec:?')

  #02. User Create page.
  if num == '1':
    print('\n=== USER CRAETE PAGE ===\n')
    name = input("input - name: ?")
    email = input("input - email: ?")
    age = input("input - age:")
    print('\nCREATE USER name {}, email {}, age {}.\n'.format(name,email,age))
    c.execute("INSERT INTO users(name, email, age) VALUES(?, ?, ?)",(name , email, age))
    con.commit()

  #03. User Edit page. 
  if num == '2':
    print('\n=== USER EDIT PAGE ===\n')
    id = input("EDIT USER ID: ?")
    c.execute("SELECT * FROM users WHERE id = ?", id)
    for row in c:
      print('\nEDIT TARGET USER INFO: name {}, email {}, age {}.\n'.format(str(row[1]), str(row[2]), str(row[3])))
    name = input("edit - name: ?")
    email = input("edit - email: ?")
    age = input("edit - age: ?")
    print('\nEDIT USER name {}, email {}, age {}.\n'.format(name,email,age))
    c.execute("UPDATE users SET name=?,email=?,age=? WHERE id = ?",(name , email, age, id))
    con.commit()

  #04. User Delete page.
  if num == '3':
    print('\n=== USER DELETE PAGE ===\n')
    id = input("DELETE USER ID: ?")
    c.execute("SELECT * FROM users WHERE id = ?", id)
    for row in c:
      print('\nDELETE TARGET USER INFO: name {}, email {}, age {}.\n'.format(str(row[1]), str(row[2]), str(row[3])))
    c.execute("DELETE FROM users WHERE id = ?",(id))
    con.commit()

  #13. Exit page.
  if num == '12':
    print("""
    close database and EC System.
    bye.
    """)
    break