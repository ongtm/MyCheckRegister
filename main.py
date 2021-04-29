import re
from kivy.app import App
from kivy.uix.behaviors import FocusBehavior
from kivy.uix.recyclegridlayout import RecycleGridLayout
from kivy.uix.recycleview.layout import LayoutSelectionBehavior
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.lang import Builder
import mysql.connector
from kivy.properties import ObjectProperty
from kivy.uix.textinput import TextInput



try:
  mydb = mysql.connector.connect(host="localhost", user="general", password="dbms")
  mycursor = mydb.cursor()
  mycursor.execute("CREATE DATABASE dbTransactions")
except:
  print("Database exists")

try:
    mycursor.execute("CREATE TABLE tblUser (name VARCHAR, pin(4) ")
    #mycursor.execute("DROP TABLE tblUser")
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
        if self.lenValidation() is False:
            self.nuErrorLabel.color = 1, 0, 0, 1
            self.nuErrorLabel.text = "Pin can only be 4 digits"
            return 0

        elif self.checkInputNulls() is True and self.compareInputs() is False:
            self.nuErrorLabel.text = "Pins do not match"
            self.nuErrorLabel.color = 1, 0, 0, 1
            return 0

        elif self.checkInputNulls() is True and self.compareInputs() is True:
            self.nuErrorLabel.color = 0, 0, 0, 1
            self.nuErrorLabel.text = "0"
            self.setUserPin()
            self.getUserPin()
            return 0

        else:
            self.nuErrorLabel.text = "Please enter a value in each box"
            self.nuErrorLabel.color = 1, 0, 0, 1
            return 0

    def compareInputs(self):

        if self.input1.text == self.input2.text:
            return True
        else:
            return False

    def checkInputNulls(self):
        if self.input1.text != '' and self.input2.text != '':
            return True
        else:
            return False

    def lenValidation(self):
        if len(self.input1.text) != 4 or len(self.input2.text) != 4:
            return False
        else:
            return True

    def setUserPin(self):
        try:
            mycursor.execute("INSERT INTO tblUsers (name, pin) VALUES (thisUser, " + self.input1.text + ")")
        except:
            print("Set fails")

    def getUserPin(self):
        try:
            mycursor.execute("SELECT pin FROM tblUsers WHERE user = 'thisUser'")
            thisPin = mycursor.fetchall()
            print(thisPin)
        except:
            print("Get fails")


class LoginScreen(Screen):
    #def __init__(self, **kwargs):
    #    super(LoginScreen, self).__init__(**kwargs)

    def btnNUS(self):
        if self.lenValidation() is False:
            self.nuErrorLabel.color = 1, 0, 0, 1
            self.nuErrorLabel.text = "Pin can only be 4 digits"
            return 0

        elif self.checkInputNulls() is True and self.compareInputs() is False:
            self.nuErrorLabel.text = "Pins do not match"
            self.nuErrorLabel.color = 1, 0, 0, 1
            return 0

        elif self.checkInputNulls() is True and self.compareInputs() is True:
            self.nuErrorLabel.color = 0, 0, 0, 1
            self.nuErrorLabel.text = "0"
            #self.verifyPin()
            return 1

        else:
            self.nuErrorLabel.text = "Please enter a value in each box"
            self.nuErrorLabel.color = 1, 0, 0, 1
            return 0

    def compareInputs(self):

        if self.input1.text == self.input2.text:
            return True
        else:
            return False

    def checkInputNulls(self):
        if self.input1.text != '' and self.input2.text != '':
            return True
        else:
            return False

    def lenValidation(self):
        if len(self.input1.text) != 4 or len(self.input2.text) != 4:
            return False
        else:
            return True



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


class PinInput(TextInput):
    #pat = re.compile(r'\D')

    #def insert_text(self, substring, from_undo=False):
    #    s = self.pat
    #    print(s)

        #return super(PinInput, self).insert_text(s, from_undo=from_undo)

    pat = re.compile(r'\D')
    def insert_text(self, substring, from_undo=False):
        pat = self.pat

        s = re.sub(pat, '', substring)

        return super(PinInput, self).insert_text(s, from_undo=from_undo)


kv = Builder.load_file("my.kv")


class MyApp(App):
    def build(self):
       return kv




if __name__ == '__main__':
    MyApp().run()
