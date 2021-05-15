import re
from kivy.app import App
from kivy.lang import Builder
from kivy.properties import ObjectProperty, ListProperty
from kivy.properties import BooleanProperty

from kivy.uix.behaviors import FocusBehavior
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.checkbox import CheckBox
from kivy.uix.dropdown import DropDown
from kivy.uix.recycleview.views import RecycleDataViewBehavior
from kivy.uix.recyclegridlayout import RecycleGridLayout
from kivy.uix.recycleview import RecycleView
from kivy.uix.recycleview.layout import LayoutSelectionBehavior

import mysql.connector
from mysql.connector import errorcode







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
        mycursor.execute("CREATE TABLE dbtransactions.tblUser (userID int NOT NULL AUTO_INCREMENT, name VARCHAR (8), pin int(4), PRIMARY KEY(userID))")
    except mysql.connector.Error as err:
        if err.errno == 1050:
            # btnNewUser.opacity = 0
            print("Hide button")

        else:
            print(err)
    try:
        mycursor.execute("CREATE TABLE dbtransactions.tblTransactions (transID int NOT NULL AUTO_INCREMENT, numcode VARCHAR(10), date DATE, transdescr VARCHAR(255), payfee DECIMAL(15,2), cleared TINYINT(1), depref DECIMAL(15,2), balance DECIMAL(15,2), PRIMARY KEY (transID))")

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

            sqlQuery = "SELECT * FROM dbtransactions.tblUser WHERE name = 'mainuser'"
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

            sqlQuery = "SELECT pin FROM dbtransactions.tblUser WHERE name = 'mainuser'"
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
    pass

class AddScreen(Screen):
    atsErrorLabel = ObjectProperty(None)
    btnAddNewTransaction = ObjectProperty(None)

    def btnAddNewTransaction(self):
            if self.checkInputNulls() is False:
                self.atsErrorLabel.text = "Please enter an amount"
                self.atsErrorLabel.color = 1, 0, 0, 1
                print("I am here")
                return 0
            elif self.verifyType() is False:
                print('Add label here for error')
            else:
                return 1

    def checkInputNulls(self):
        if self.txtAmount.text != '':
            return True
        else:
            return False


class EditScreen(Screen):
    pass


class WindowManager(ScreenManager):
    pass


class SelectableRecycleGridLayout(FocusBehavior, LayoutSelectionBehavior, RecycleGridLayout):
    pass

class SelectableLabel(RecycleDataViewBehavior, Label):

    def refresh_view_layout(self, rv, index, layout, viewport):
        mod = index % 8
        if mod == 0:
            layout['size_hint'] = (0, 0.1)
        elif mod == 1:
            layout['size_hint'] = (0.2, 0.1)
        elif mod == 2:
            layout['size_hint'] = (0.15, 0.1)
        elif mod == 3:
            layout['size_hint'] = (0.35, 0.1)
        elif mod == 4:
            layout['size_hint'] = (0.3, 0.1)
        elif mod == 5:
            layout['size_hint'] = (0.25, 0.1)
        elif mod == 6:
            layout['size_hint'] = (0.2, 0.1)
        elif mod == 7:
            layout['size_hint'] = (0.3, 0.1)
        super(SelectableLabel, self).refresh_view_layout(rv, index, layout, viewport)


class RV(RecycleView):
    data_items = ListProperty([])

    def __init__(self, **kwargs):
        super(RV, self).__init__(**kwargs)
        self.getTransactions()


    def getTransactions(self):
        try:
            mydb = mysql.connector.connect(host="localhost", user="general", password="dbms_532021!")
            mycursor = mydb.cursor()

            sqlQuery = "SELECT * FROM dbtransactions.tblTransactions"

            mycursor.execute(sqlQuery)

            rows = mycursor.fetchall()

            for row in rows:
                for col in row:
                    self.data_items.append(col)


        except Exception as e:
            print(e)


class PinInput(TextInput):

    pat = re.compile(r'\D')
    def insert_text(self, substring, from_undo=False):
        pat = self.pat

        s = re.sub(pat, '', substring)

        return super(PinInput, self).insert_text(s, from_undo=from_undo)


class AmountInput(TextInput):
    pat = re.compile('[^0-9]')
    def insert_text(self, substring, from_undo=False):
        pat = self.pat
        if '.' in self.text:
            s = re.sub(pat, '', substring)
        else:
            s = '.'.join([re.sub(pat, '', s) for s in substring.split('.', 1)])
        return super(AmountInput, self).insert_text(s, from_undo=from_undo)


class CustomDropDown(DropDown):
    pass



class MyApp(App):
    pass
    #def build(self):
    #   return kv




if __name__ == '__main__':
   MyApp().run()
