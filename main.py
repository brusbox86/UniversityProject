import pymysql
from pymysql.cursors import DictCursor


class DataBase:
    def __init__(self):
        self.connection = self.connect()
        self.cursors = self.connection.cursor()

    def connect(self):
        connection = pymysql.connect(
            host='localhost',
            user='Andrew',
            password='1111',
            db='users',
            charset='utf8mb4',
            cursorclass=DictCursor
        )
        return connection

    def addUser(self, login, password, type):
        sql = "INSERT INTO users (login, password, type) VALUES (%s, %s, %s)"
        temp = [login, password, type]
        self.cursors.execute(sql, temp)
        self.connection.commit()

    def getUsers(self):
        sql = "SELECT * FROM users WHERE login = login"
        self.cursors.execute(sql)
        data = self.cursors.fetchall()
        print(data)

    def checkLogin(self, login):
        sql = f"SELECT * FROM users WHERE login = {login}"
        try:

            self.cursors.execute(sql)
            data = self.cursors.fetchall()
            #print(data)
            if len(data) > 0:
                return True
            else:
                return False
        except:
            return False

    def checkUserData(self, login, password):
        sql = f"SELECT password FROM users WHERE login = {login}"
        self.cursors.execute(sql)
        data = self.cursors.fetchall()
        if data = password:
            print('Welcome') and return True
        else:
            print('Incorrect password or login')


def reg_func():
    login = input('Enter your login  ')    # asking for login
    return login


def get_password():
    password = input('enter your password ')
    return password

def log_in_func():
    login = input('Enter your login  ')
    password = input('enter your password ')
    return password, login


def reg_or_log_in_menu():         #1 function
    reg_log_choose = input('Please, log in (L) or registration (R)\n   L/R?  ')  #choose a log or registration
    if reg_log_choose == 'L' or 'l':
        log_in_func()                      # if L is chosen, we're going to log in function

    elif reg_log_choose == 'R' or 'r':
        if DataBase().checkLogin(reg_func()) is True:                        # if R is chosen, we're going to reg function
            print('This login is also used. Try another login')
            reg_func()
        elif DataBase().checkLogin(reg_func()) is False:
            checkUserData()
    else:
        print('Incorrect input')         # nu ponyatno

reg_or_log_in_menu()



