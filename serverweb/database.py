import sqlite3

def init_db():
    conn = sqlite3.connect('database.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS users (username TEXT PRIMARY KEY, password TEXT, coins INTEGER,usedvoucher TEXT)''')
    c.execute('''CREATE TABLE IF NOT EXISTS vouchers (code TEXT, coins INTEGER, used INTEGER)''')
    conn.commit()
    conn.close()

def get_user(username, password):
    conn = sqlite3.connect('database.db')
    c = conn.cursor()
    c.execute('SELECT * FROM users WHERE username = ? AND password = ?', (username, password))
    user = c.fetchone()
    conn.close()
    return user

def create_user(username, password):
    try:
        conn = sqlite3.connect('database.db')
        c = conn.cursor()
        use = 'no'
        c.execute('INSERT INTO users (username, password, coins,usedvoucher) VALUES (?, ?, ?,?)', (username, password, 0,use))
        conn.commit()
        conn.close()
        return True
    except sqlite3.IntegrityError:
        return False

def add_coins(username, coins):
    conn = sqlite3.connect('database.db')
    c = conn.cursor()
    c.execute('UPDATE users SET coins = coins + ? WHERE username = ?', (coins, username,))
    conn.commit()
    conn.close()
    
def delete_coins(username,coins):
    conn = sqlite3.connect('database.db')
    c = conn.cursor()
    c.execute('UPDATE users SET coins = coins - ? WHERE username = ?', (coins, username,))
    conn.commit()
    conn.close()

def get_coins(username):
    conn = sqlite3.connect('database.db')
    c = conn.cursor()
    c.execute('SELECT coins FROM users WHERE username = ?', (username,))
    coins = c.fetchone()[0]
    conn.close()
    return coins

def create_voucher(username, code, coins):
    conn = sqlite3.connect('database.db')
    c = conn.cursor()
    c.execute('INSERT INTO vouchers (code, coins, used) VALUES (?, ?, 0)', (code, coins,))
    c.execute('UPDATE users SET usedvoucher = ? WHERE username = ?',("yes",username))
    conn.commit()
    conn.close()

def alreadyvouched(username):
    conn = sqlite3.connect('database.db')
    c = conn.cursor()
    c.execute('SELECT usedvoucher FROM users WHERE username = ?', (username,))
    used = c.fetchone()
    print(used[0])
    if used[0] == "no":
        return False
    return True


def used_voucher(username, code):
    conn = sqlite3.connect('database.db')
    c = conn.cursor()
    c.execute('SELECT * FROM vouchers WHERE code = ? AND used = 0', (code,))
    voucher = c.fetchone()
    if voucher:
        add_coins(username, voucher[1])
        c.execute('UPDATE vouchers SET used = 1 WHERE code = ?', (code,))
        conn.commit()
        conn.close()
        return True
    conn.close()
    return False

