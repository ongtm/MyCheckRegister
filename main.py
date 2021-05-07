import re
from kivy.app import App
from kivy.uix.behaviors import FocusBehavior
from kivy.uix.recyclegridlayout import RecycleGridLayout
from kivy.uix.recycleview.layout import LayoutSelectionBehavior
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.lang import Builder
import mysql.connector
from mysql.connector import errorcode
from kivy.properties import ObjectProperty
from kivy.uix.textinput import TextInput





#def createMySQLTransactionsTable(mycursor):
#    try:
#        mycursor.execute("CREATE TABLE tblTransactions (NumCode VARCHAR(10), TransDate DATETIME(6), TransDescription "
#                     "VARCHAR(255), PayFee DECIMAL(15,2), Cleared TINYINT(1) , DepCrd DECIMAL(15,2), Balance DECIMAL(15,2)")
#    except:
#        print("tblTransactions exists")

class StartScreen(Screen):
    btnNewUser = ObjectProperty()

    try:
        mydb = mysql.connector.connect(host="localhost", user="general", password="dbms_532021!")
        mycursor = mydb.cursor()
    except Exception as e:
        print(e)

    try:
        mycursor.execute("CREATE DATABASE dbTransactions")
    except Exception as e:
        print(e)

    try:
        mycursor.execute("CREATE TABLE dbtransactions.tblUser (name VARCHAR (8), pin int(4))")
    except mysql.connector.Error as err:
        if err.errno == 1050:
            # btnNewUser.opacity = 0
            print("Hide button")

        else:
            print("WTF")
    try:
        mycursor.execute("CREATE TABLE dbtransactions.tblTransactions (numcode VARCHAR(10), date DATETIME, transdescr VARCHAR(255), payfee DECIMAL(15,2), cleared TINYINT(1), depref DECIMAL(15,2), balance DECIMAL(15,2));")
    except Exception as e:
        print(e)
    try:
        mycursor.close()
    except Exception as e:
        print(e)



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
            mydb = mysql.connector.connect(host="localhost", user="general", password="dbms_532021!")
            mycursor = mydb.cursor()

            sqlQuery = "INSERT INTO dbtransactions.tblUser (name, pin) VALUES (%s, %s);"
            data_user = ('mainuser', self.input1.text)

            mycursor.execute(sqlQuery, data_user)
            mydb.commit()
        except Exception as e:
            print(e)

        try:
            mycursor.close()
        except Exception as e:
            print(e)

    def getUserPin(self):
        try:
            mydb = mysql.connector.connect(host="localhost", user="general", password="dbms_532021!")
            mycursor = mydb.cursor()

            sqlQuery = "SELECT * FROM dbtransactions.tblUser WHERE name = 'mainuser';"
            mycursor.execute(sqlQuery)
            thisPin = mycursor.fetchone()
            print("get succeeds")
        except:
            print("Get fails")


class LoginScreen(Screen):
    btnLoginSubmit = ObjectProperty(None)
    lsErrorLabel = ObjectProperty(None)

    def btnLSS(self):
        if self.checkInputNulls() is False:
            self.lsErrorLabel.text = "Please enter a Pin"
            self.lsErrorLabel.color = 1, 0, 0, 1
            return 0
        elif self.lenValidation() is False:
            self.lsErrorLabel.color = 1, 0, 0, 1
            self.lsErrorLabel.text = "Pin can only be 4 digits"
            return 0
        elif self.verifyPin() is True:
            self.lsErrorLabel.text = "0"
            self.lsErrorLabel.color = 0, 0, 0, 0
            return 1
        else:
            self.lsErrorLabel.text = "Incorrect Pin"
            self.lsErrorLabel.color = 1, 0, 0, 1
            return 0

    def checkInputNulls(self):
        if self.input1.text != '':
            return True
        else:
            return False

    def lenValidation(self):
        if len(self.input1.text) != 4:
            return False
        else:
            return True

    def verifyPin(self):

        try:
            mydb = mysql.connector.connect(host="localhost", user="general", password="dbms_532021!")
            mycursor = mydb.cursor()

            sqlQuery = "SELECT pin FROM dbtransactions.tblUser WHERE name = 'mainuser';"
            mycursor.execute(sqlQuery)

            thisTuple = mycursor.fetchone()

            mycursor.close()

            thisPin = int(thisTuple[0])

            if thisPin == int(self.input1.text):
                return True
            else:
                return False

        except Exception as e:
            print(e)




class TransactionScreen(Screen):


    def getTransactions(self):
        pass

        try:
            mydb = mysql.connector.connect(host="localhost", user="general", password="dbms_532021!")
            mycursor = mydb.cursor()

            sqlQuery = "SELECT pin FROM dbtransactions.tblUser WHERE name = 'mainuser';"

            mycursor.execute(sqlQuery)

            thisTuple = mycursor.fetchall()

            mycursor.close()

        except Exception as e:
            print(e)

    def __init__(self, **kwargs):
        super(TransactionScreen, self).__init__(**kwargs)
        self.insertDummyTransactions()
        self.getTransactions()
        #self.data = [{'text': str(x)} for x in range(100)]

    def insertDummyTransactions(self):
        try:
            mydb = mysql.connector.connect(host="localhost", user="general", password="dbms_532021!")
            mycursor = mydb.cursor()

            sqlQuery = "INSERT INTO dbtransactions.tblTransactions (numcode, date, transdescr, payfee, cleared, depref, balance) VALUES (%s, %s, %s, %s, %s, %s, %s);"

            data_transaction = ('atm', '2021-1-1', 'testing_starting balance', '0', '1', '0', '1000')
            mycursor.execute(sqlQuery, data_transaction)

            mydb.commit()
            print("transaction added?")
        except Exception as e:
            print(e)


class EditScreen(Screen):
    pass


class WindowManager(ScreenManager):
    pass


class SelectableRecycleGridLayout(FocusBehavior, LayoutSelectionBehavior, RecycleGridLayout):
    pass


class PinInput(TextInput):

    pat = re.compile(r'\D')
    def insert_text(self, substring, from_undo=False):
        pat = self.pat

        s = re.sub(pat, '', substring)

        return super(PinInput, self).insert_text(s, from_undo=from_undo)


#kv = Builder.load_file("my.kv")


class MyApp(App):
    pass
    #def build(self):
    #   return kv




if __name__ == '__main__':
   MyApp().run()
