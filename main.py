from kivy.app import App
from kivy.uix.behaviors import FocusBehavior
from kivy.uix.recyclegridlayout import RecycleGridLayout
from kivy.uix.recycleview.layout import LayoutSelectionBehavior
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.lang import Builder
import mysql.connector
from mysql.connector import Connect, Error
from getpass import getpass




class LoginScreen(Screen):

    def __init__(self):
        self.checkForDatabase()

    def checkForDatabase(self):
        conn = ""
        try:
            mysql.connector.connect(host='localhost', database='myCheckRegisterDB')
            if conn.is_connected():
                conn.close()
        except:
            newdb = mysql.connector.connect(host='localhost')
            thiscursor = newdb.cursor()
            thiscursor.execute("CREATE DATABASE myCheckRegisterDB")
            thiscursor.execute("CREATE TABLE tblUsers (name VARCHAR(4), inputOne INT(1), inputTwo INT(1), inputThree INT(1), inputFour INT(1)")
            thiscursor.execute("INSERT INTO tblUsers (name, inputOne, inputTwo, inputThree, inputFour) VALUES ('User','1', '2', '3' ,'4')")
        finally:
            if conn is not None and conn.is_connected():
                conn.close()
    #pass


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
