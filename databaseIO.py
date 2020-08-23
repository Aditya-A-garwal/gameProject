import sqlite3

class DBIO:
    conn = 'a'

    # Constructor
    def __init__(self, target):
        self.name = target + '.db'
        try:
            self.conn = sqlite3.connect(self.name)
            c = self.conn.cursor()

            # Create Table
            c.execute('''CREATE TABLE terrain(keys INTEGER NOT NULL PRIMARY KEY, binry TEXT)''')
            self.conn.commit()

        except:
            pass

    # Save/Update function
    def save(self, key, binary):
        """Saves/Updates the string at a particular key location.

        Requires the key as an int and the UTF-8 string.
        """
        c = self.conn.cursor()
        try:    # Save string at new key location
            c.execute('''INSERT INTO terrain VALUES (?,?)''', (key, binary))
            conn.commit()

        except: # Update string at existing key
            c.execute('UPDATE terrain SET binry =?  WHERE keys=?', (binary, key))
            self.conn.commit()

    # Load function
    def load(self, key):
        """Retrieves the string stored at a particular key location.

        Requires the key as an int.
        Returns the string at the key's location (if key is present) or None
        """

        c = self.conn.cursor()
        c.execute('''SELECT binry FROM terrain WHERE keys=?''', (key,))
        res = c.fetchone()
        self.conn.commit()

        try:
            return res[0]
        except:
            return res

    # Close the connection
    def stop(self):
        self.conn.close()

# Testing
a = DBIO('world')
a.save(-188888, 'hi')
print(a.load(-188888))
a.stop()
