import os
import sqlite3
path = '/Users/somahisai/Desktop/ec_system/example.db'
if not (os.path.isfile(path)):
  con = sqlite3.connect('example.db')
  c = con.cursor()
  c.execute("""
    CREATE TABLE users (
      id INTEGER PRIMARY KEY AUTOINCREMENT,
      name STRING,
      email STRING,
      age INTEGER
    )
  """)# create users table
  c.execute("""
    CREATE TABLE items (
      id INTEGER PRIMARY KEY AUTOINCREMENT,
      code STRING,
      name STRING,
      price INTEGER
    )
  """)# create items table
  c.execute("""
    CREATE TABLE purchase_histories(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INTEGER,
    item_id INTEGER
    )
  """)# create purchase_histories table


con = sqlite3.connect('example.db')
c = con.cursor()

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

  #05. User List page.
  if num == '4':
    print('\n=== USER LIST PAGE ===\n')
    c.execute("SELECT * FROM users")
    for row in c:
      print('ID {}, name {}, email {}, age {}.'.format(str(row[0]),str(row[1]), str(row[2]), str(row[3])))

  #06. Item Create page.
  if num == '5':
    print('\n=== ITEM CRAETE PAGE ===\n')
    name = input("input - name: ?")
    code = input("input - code: ?")
    price = input("input - price: ?")
    print('\nCREATE ITEM name {}, code {}, price {}.\n'.format(name,code,price))
    c.execute("INSERT INTO items(name, code, price) VALUES(?, ?, ?)",(name , code, price))
    con.commit()

  #07. Item Edit page.
  if num == '6':
    print('\n=== ITEM EDIT PAGE ===\n')
    id = input("EDIT ITEM ID: ?")
    c.execute("SELECT * FROM items WHERE id = ?", id)
    for row in c:
      print('\nEDIT TARGET ITEM INFO: name {}, code {}, price {}.\n'.format(str(row[1]), str(row[2]), str(row[3])))
    name = input("edit - name: ?")
    code = input("edit - code: ?")
    price = input("edit - price: ?")
    print('\nEDIT ITEM name {}, code {}, price {}.\n'.format(name,code,price))
    c.execute("UPDATE items SET name=?,code=?,price=? WHERE id = ?",(name , code, price, id))
    con.commit()

  #08. Item Delete page.
  if num == '7':
    print('\n=== ITEM DELETE PAGE ===\n')
    id = input("DELETE ITEM ID: ?")
    c.execute("SELECT * FROM items WHERE id = ?", id)
    for row in c:
      print('\nDELETE TARGET ITEM INFO: name {}, code {}, price {}.\n'.format(str(row[1]), str(row[2]), str(row[3])))
    c.execute("DELETE FROM items WHERE id = ?",(id))
    con.commit()

  #09. Item List page.
  if num == '8':
    print('\n=== ITEM LIST PAGE ===\n')
    c.execute("SELECT * FROM items")
    for row in c:
      print('ID {}, name {}, code {}, price {}.'.format(str(row[0]),str(row[1]), str(row[2]), str(row[3])))

  #10. Item Buy Mode page.
  if num == '9':
    print('\n === ITEM BUY MODE PAGE ===\n')
    user_id = input("USER ID: ?")
    c.execute("SELECT * FROM users WHERE id = ?", user_id)
    user = c.fetchone()
    item_code = input("BUY ITEM CODE: ?")
    c.execute("SELECT * FROM items WHERE code = ?", (item_code,))
    item = c.fetchone()
    print('\nUSER INFO: NAME {}, EMAIL {}, AGE {}.'.format(str(user[1]), str(user[2]), str(user[3])))
    print('ITEM INFO: NAME {}, CODE {}, PRICE {}.'.format(str(item[2]), str(item[1]), str(item[3])))
    flag = input("\nCONFIRM BUY (Y/n):?\n")
    if flag == 'N' or flag == 'n':
      print('no')
    else:
      c.execute("INSERT INTO purchase_histories(user_id, item_id) values (?, ?)",(user[0],item[0]))
      con.commit()
      c.execute("SELECT id FROM purchase_histories ORDER BY id DESC LIMIT 1")
      purchase_history = c.fetchone()
      print('ITEM PURCHASE ID {} USER_ID {} ITEM_ID {}'.format(str(purchase_history[0]), str(user[0]), str(item[0])))

  #13. Exit page.
  if num == '12':
    print("""
    close database and EC System.
    bye.
    """)
    break