import random
import secrets
import re
import sqlite3



def password_generator():
    lower_case = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    upper_case = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'p', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y' ,'Z'] 
    digits = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['@', '#', '$', '%', '=', ':', '?', '.', '/', '|', '~', '>', '*', '(', ')', '{', '}', '!',]
    cset = lower_case + upper_case + digits + symbols

    passlen = random.randint(8, 10)

    password = ""
    password = password + random.choice(lower_case) ###select one lower,upper,digit and special character
    password = password + random.choice(upper_case)
    password = password + random.choice(digits)
    password = password + random.choice(symbols)
    for i in range (passlen-4):                     ###select random characters for length - 4
        password = password + random.choice(cset)
    print(passlen)
    password = ''.join(random.sample(password,len(password)))   ###shuffle the password to avoid the sequence of first 4 character
    print(password)
    return password

if __name__ == '__main__':

    username = input("Enter username: ")
    password = password_generator()
    conn = sqlite3.connect('example.sqlite')
    c = conn.cursor()
    #c.execute(''' DROP TABLE IF EXISTS IdPass''')
    c.execute('''CREATE TABLE IF NOT EXISTS IdPass
                    (ID INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,Username TEXT NOT NULL,Password TEXT NOT NULL UNIQUE)
    ''')
    
    c.execute('INSERT INTO IdPass (Username,Password) VALUES (?,?) ',(username,password) )
    conn.commit()
    conn.close()