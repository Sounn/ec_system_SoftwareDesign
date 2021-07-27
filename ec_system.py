import sqlite3
con = sqlite3.connect('ec.db')
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

#create seed db
for i in range(3):
  name = 'name{}'.format(str(i))
  email = 'email{}'.format(str(i))
  age = i + 10
  code = 'code{}'.format(str(i))
  price = i + 100
  c.execute("INSERT INTO users(name, email, age) VALUES(?, ?, ?)",(name , email, age))
  c.execute("INSERT INTO items(name, code, price) VALUES(?, ?, ?)",(name , code, price))
  c.execute("INSERT INTO purchase_histories(user_id, item_id) values (?, ?)",(i+1,i+1))
  con.commit()

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
  elif num == '2':
    print('\n=== USER EDIT PAGE ===\n')
    id = input("EDIT USER ID: ?")
    c.execute("SELECT * FROM users WHERE id = ?", id)
    user = c.fetchone()
    print('\nEDIT TARGET USER INFO: name {}, email {}, age {}.\n'.format(str(user[1]), str(user[2]), str(user[3])))
    name = input("edit - name: ?")
    email = input("edit - email: ?")
    age = input("edit - age: ?")
    print('\nEDIT USER name {}, email {}, age {}.\n'.format(name,email,age))
    c.execute("UPDATE users SET name=?,email=?,age=? WHERE id = ?",(name , email, age, id))
    con.commit()

  #04. User Delete page.
  elif num == '3':
    print('\n=== USER DELETE PAGE ===\n')
    id = input("DELETE USER ID: ?")
    c.execute("SELECT * FROM users WHERE id = ?", id)
    user = c.fetchone()
    print('\nDELETE TARGET USER INFO: name {}, email {}, age {}.\n'.format(str(user[1]), str(user[2]), str(user[3])))
    c.execute("DELETE FROM users WHERE id = ?",(id))
    c.execute("DELETE FROM purchase_histories WHERE user_id = ?",(id))
    con.commit()

  #05. User List page.
  elif num == '4':
    print('\n=== USER LIST PAGE ===\n')
    c.execute("SELECT * FROM users")
    for user in c:
      print('ID {}, name {}, email {}, age {}.'.format(str(user[0]),str(user[1]), str(user[2]), str(user[3])))

  #06. Item Create page.
  elif num == '5':
    print('\n=== ITEM CRAETE PAGE ===\n')
    name = input("input - name: ?")
    code = input("input - code: ?")
    price = input("input - price: ?")
    print('\nCREATE ITEM name {}, code {}, price {}.\n'.format(name,code,price))
    c.execute("INSERT INTO items(name, code, price) VALUES(?, ?, ?)",(name , code, price))
    con.commit()

  #07. Item Edit page.
  elif num == '6':
    print('\n=== ITEM EDIT PAGE ===\n')
    id = input("EDIT ITEM ID: ?")
    c.execute("SELECT * FROM items WHERE id = ?", id)
    item = c.fetchone()
    print('ITEM INFO: NAME {}, CODE {}, PRICE {}.'.format(str(item[2]), str(item[1]), str(item[3])))
    name = input("edit - name: ?")
    code = input("edit - code: ?")
    price = input("edit - price: ?")
    print('\nEDIT ITEM name {}, code {}, price {}.\n'.format(name,code,price))
    c.execute("UPDATE items SET name=?,code=?,price=? WHERE id = ?",(name , code, price, id))
    con.commit()

  #08. Item Delete page.
  elif num == '7':
    print('\n=== ITEM DELETE PAGE ===\n')
    id = input("DELETE ITEM ID: ?")
    c.execute("SELECT * FROM items WHERE id = ?", id)
    item = c.fetchone()
    print('ITEM DELETE: NAME {}, CODE {}, PRICE {}.'.format(str(item[2]), str(item[1]), str(item[3])))
    c.execute("DELETE FROM items WHERE id = ?",(id))
    c.execute("DELETE FROM purchase_histories WHERE item_id = ?",(id))
    con.commit()

  #09. Item List page.
  elif num == '8':
    print('\n=== ITEM LIST PAGE ===\n')
    c.execute("SELECT * FROM items")
    for item in c:
      print('ID {}, name {}, code {}, price {}.'.format(str(item[0]),str(item[1]), str(item[2]), str(item[3])))

  #10. Item Buy Mode page.
  elif num == '9':
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
      print('\nNOT BUY\n')
    else:
      c.execute("INSERT INTO purchase_histories(user_id, item_id) values (?, ?)",(user[0],item[0]))
      con.commit()
      c.execute("SELECT id FROM purchase_histories ORDER BY id DESC LIMIT 1")
      purchase_history = c.fetchone()
      print('ITEM PURCHASE ID {} USER_ID {} ITEM_ID {}'.format(str(purchase_history[0]), str(user[0]), str(item[0])))

  #11. Item Buy Histories Mode page.
  elif num == '10':
    print('\n=== ITEM BUY HISTORIES MODE PAGE ===\n')
    c.execute("SELECT * FROM (SELECT * FROM purchase_histories ORDER BY id DESC LIMIT 10) ORDER BY id ASC")
    histories = c.fetchall()
    print('PURCHASE HISTORY INFO {} RECORDS.\n'.format(len(histories)))
    for purchase in histories:
      c.execute("SELECT * FROM users WHERE id = ?", (purchase[1],))
      user = c.fetchone()
      c.execute("SELECT * FROM items WHERE id = ?", (purchase[2],))
      item = c.fetchone()
      print('ID:{} USER_NAME:{} USER_EMAIL:{} ITEM_NAME{} ITEM_PRICE {}'
      .format(str(purchase[0]), str(user[1]), str(user[2]), str(item[1]), str(item[3])))

  #12. Total Amount Aggregation Mode page.
  elif(num == '11'):
    print('\n=== TOTAL AMOUNT AGGREGATION MODE PAGE ===\n')
    c.execute("SELECT * FROM purchase_histories")
    histories = c.fetchall()
    total_amount = 0
    for purchase in histories:
      c.execute("SELECT * FROM items WHERE id = ?", (purchase[2],))
      item = c.fetchone()
      total_amount += item[3]
    print('TOTAL AMOUNT: {} yen.'.format(str(total_amount)))

  #13. Exit page.
  elif num == '12':
    print("""
    close database and EC System.
    bye.
    """)
    break