import re
from kivy.app import App
from kivy.uix.behaviors import FocusBehavior
from kivy.uix.recyclegridlayout import RecycleGridLayout
from kivy.uix.recycleview.layout import LayoutSelectionBehavior
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.lang import Builder
import mysql.connector
# from mysql.connector import Connect, Error
# from getpass import getpass
from kivy.properties import ObjectProperty

try:
  mydb = mysql.connector.connect(host="localhost", user="general", password="dbms")
  mycursor = mydb.cursor()
  mycursor.execute("CREATE DATABASE dbTransactions")
except:
  print("Database exists")

try:
    mycursor.execute("CREATE TABLE tblUser (name VARCHAR, pinOne INT(1), pinTwo INT(1), pinThree(1), pinFour(1) ")
except:
  print("tblUser Exists")

try:
    mycursor.execute("CREATE TABLE tblTransactions (NumCode VARCHAR(10), TransDate DATETIME(6), TransDescription "
                     "VARCHAR(255), PayFee DECIMAL(15,2), Cleared TINYINT(1) , DepCrd DECIMAL(15,2), Balance DECIMAL(15,2)")
except:
  print("tblTransactions exists")

class StartScreen(Screen):
    #Check if user exists, if so move to login screen, if not show new user screen
    pass


class NewUserScreen(Screen):
    btnNewUserSubmit = ObjectProperty(None)
    nuErrorLabel = ObjectProperty(None)

    def btnNUS(self):
        if self.reValidation() is False:
            self.nuErrorLabel.color = 1, 0, 0, 1
            self.nuErrorLabel.text = "Invalided character entered"
            exit

        if self.checkInputNulls() is True and self.compareInputs() is True:
            self.nuErrorLabel.color = 0, 0, 0, 1
            self.setUserPin()

        elif self.checkInputNulls() is True and self.compareInputs() is False:
            self.nuErrorLabel.text = "Pins do not match"
            self.nuErrorLabel.color = 1, 0, 0, 1
        else:
            self.nuErrorLabel.text = "Please enter a value in each box"
            self.nuErrorLabel.color = 1, 0, 0, 1

    def reValidation(self):
        #Need to watch a video on this
        return True

    def compareInputs(self):

        if self.input1.text == self.input5.text and self.input2.text == self.input6.text and self.input3.text == self.input7.text and self.input4.text == self.input8.text:
            return True
        else:
            return False


    def checkInputNulls(self):
        if self.input1.text != '' and self.input2.text != '' and self.input3.text != '' and self.input4.text != '' and self.input5.text != '' and self.input6.text != '' and self.input7.text != '' and self.input8.text != '':
            return True
        else:
            return False

    def setUserPin(self):
        #Add Pin to database
        pass

class LoginScreen(Screen):
    def __init__(self, **kwargs):
        super(LoginScreen, self).__init__(**kwargs)


class TransactionScreen(Screen):


    def getTransactions(self):
        pass
        # conn = ""
        #try:
        #    conn = mysql.connector.connect(host='localhost', database='python_sql')
        #    if conn.is_connected():
        #        print('Connected to database')
        #except Error as e:
        #    print(e)

        #finally:
        #    if conn is not None and conn.is_connected():
        #        conn.close()

    def __init__(self, **kwargs):
        super(TransactionScreen, self).__init__(**kwargs)
        self.getTransactions()
        #self.data = [{'text': str(x)} for x in range(100)]


class EditScreen(Screen):
    pass


class WindowManager(ScreenManager):
    pass


class SelectableRecycleGridLayout(FocusBehavior, LayoutSelectionBehavior, RecycleGridLayout):
    pass



kv = Builder.load_file("my.kv")


class MyApp(App):
    def build(self):
       return kv




if __name__ == '__main__':
    MyApp().run()
