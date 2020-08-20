import sqlite3

## This part has to be written in the main program and run only once,
## though it wont't give an error if run more than once
try:
    conn = sqlite3.connect('world.db')
    c = conn.cursor()
    # Create Table
    c.execute('''CREATE TABLE terrain(keys INTEGER NOT NULL PRIMARY KEY, binry TEXT)''')
    conn.commit()
    conn.close()
except:
    pass
## End of part

## This part is the functions for DB_io
def save(key, binary):  ## Saving/Updating
    '''Saves or Updates a string at a particular key location.

    Requires the key as an int and the binary string.
    '''
    conn = sqlite3.connect('world.db')  ## Connects to the DB, Creates a new DB if DB is not present
        ## in the same folder as this program
    c = conn.cursor()
    try:    ## Saving strings at a new key location
        c.execute('''INSERT INTO terrain VALUES (?,?)''', (key, binary))
        conn.commit()
        
    except: ## Updating a string at key which is already present
        c.execute('UPDATE terrain SET binry =?  WHERE keys=?', (binary, key))
        conn.commit()
    conn.close()    ## Closes the connection to DB

def retrieve(key):  ## Retrieving the string stored at a particular key
    '''Retrieves the string stored at a particular key location.

    Requires the key as an int.
    Returns the string at the key location or None if key is not present.
    '''
    conn = sqlite3.connect('world.db')  ## Connects to the DB, Creates a new DB if DB is not present
        ## in the same folder as this program
    c = conn.cursor()
    c.execute('''SELECT binry FROM terrain WHERE keys=?''', (key, ))
    res = c.fetchone()
    conn.commit()
    conn.close()    ## Closes the connection to DB
    try:
        return res[0]
    except:
        return res
## End of part

## Testing
for i in range(-3,4,1):
    save(i, b'\x80\x04\x95\x0b\x00\x00\x00\x00\x00\x00\x00]\x94(K\x01K\x02K\x03e.')
for i in range(-1,5):
    print(retrieve(i))
