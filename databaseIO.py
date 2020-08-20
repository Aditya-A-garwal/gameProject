import sqlite3

# Initialization (To be run only once)
try:
    conn = sqlite3.connect('world.db')
    c = conn.cursor()

    # Create Table
    c.execute('''CREATE TABLE terrain(keys INTEGER NOT NULL PRIMARY KEY, binry TEXT)''')
    conn.commit()
    conn.close()
except:
    pass

# Save/Update function
def save(key, binary):

    """Saves/Updates the string at a particular key location.

    Requires the key as an int and the UTF-8 string.
    """
    conn = sqlite3.connect('world.db')  # Connect to the DB (if not present then create a new DB)
    c = conn.cursor()
    try:    # Save string at new key location
        c.execute('''INSERT INTO terrain VALUES (?,?)''', (key, binary))
        conn.commit()

    except: # Update string at existing key
        c.execute('UPDATE terrain SET binry =?  WHERE keys=?', (binary, key))
        conn.commit()
    conn.close()

# Load function
def load(key):
    """Retrieves the string stored at a particular key location.

    Requires the key as an int.
    Returns the string at the key's location (if key is present) or None
    """
    conn = sqlite3.connect('world.db')  # Connect to DB (if not present then create a new DB)

    c = conn.cursor()
    c.execute('''SELECT binry FROM terrain WHERE keys=?''', (key,))
    res = c.fetchone()
    conn.commit()
    conn.close()
    try:
        return res[0]
    except:
        return res

# Testing
for i in range(-3,4,1): save(i, b'\x80\x04\x95\x0b\x00\x00\x00\x00\x00\x00\x00]\x94(K\x01K\x02K\x03e.')

for i in range(-1,5): print(retrieve(i))
