# Example 11.18 SQLite3
import sqlite3
# Create and Connect to the SQLite3 Database  
conn = sqlite3.connect('test.db')
print ("Opened database successfully")

# Insert a Table ===========================================
conn.execute('''CREATE TABLE IF NOT EXISTS COURSE 
         (ID INT PRIMARY KEY     NOT NULL,
         NAME            TEXT    NOT NULL,
         STUDENT_NO      INT     NOT NULL,
         ADDRESS         CHAR(50),
         MARK            REAL);''')
print ("Table created successfully")

# Insert an record =========================================
conn.execute("INSERT INTO COURSE (ID,NAME,STUDENT_NO,ADDRESS,MARK) \
      VALUES (1, 'Billy', 202119, '103 Borough Road, London', 75.00 )");

#conn.commit()
print ("Records created successfully")

# Search the Table =========================================
cursor = conn.execute("SELECT id, name, address, mark from COURSE")
for row in cursor:
   print ("ID = ", row[0])
   print ("NAME = ", row[1])
   print ("ADDRESS = ", row[2])
   print ("MARK = ", row[3], "\n")

print ("Operation done successfully")
conn.close()
