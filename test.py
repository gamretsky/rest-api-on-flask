import sqlite3
# import hmac
## And instead of using it like this:
# if user and safe_str_cmp(user.password, password):
## We should do this:
# if user and hmac.compare_digest(user.password, password):
connection = sqlite3.connect('database.db')

cursor = connection.cursor()
create_table = "CREATE TABLE users (id int, username text, password text)"
cursor.execute(create_table)

insert_user = "INSERT INTO users VALUES (?, ?, ?)"

users = [
    (1, 'jose', '1q2w3e'),
    (2, 'rolf', '1q2w3e'),
    (3, 'anne', '1q2w3e')
]
connection.executemany(insert_user, users)

connection.commit()
connection.close()
