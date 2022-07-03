
import tkinter
from tkinter import messagebox

import mysqlx

from Controllers.loginController import LoginWindowController
from Views.loginGUI import LoginGUI

from connection import connectMySQL
from utils.encryption import Encryption


class AdminCreatorWindowController():

    def __init__(self):
        self.dbConnection = connectMySQL()
        self.dbCursor = self.dbConnection.cursor()

    def registerAccountToDatabase(self, firstName, lastName, email, password):
        sql = f"""
        INSERT INTO user (FirstName, LastName, EmailAdd, Password) VALUES (
            %s, %s, %s, %s 
        )
        """
        try:
            self.dbCursor.execute(sql, (firstName, lastName, email, password))
            self.dbConnection.commit()
        except mysqlx.IntegrityError:
            messagebox.showerror('Registration', 'There was a problem in the registration. Please try again later.')
        finally:
            self.dbConnection.close()
            messagebox.showinfo('Registration Success', 'Admin Account successfully created.')
    
    def inconsistentPasswords(self, password, confirm):
        print(password != confirm)
        return password != confirm
    
    def createAdminAccount(self, data : dict, window: tkinter.Tk):
        firstName = data['firstName']
        lastName = data['lastName']
        email = data['email']
        password = data['password']
        confirmPassword = data['confirmPassword']

        if '' in data.values():
            messagebox.showwarning('Registration Error', 'Please make sure to fill up all the fields.')
            return

        if self.inconsistentPasswords(password, confirmPassword):
            messagebox.showwarning('Registration Error', 'Please make sure your passwords match')
            return 
        
        encryptedPassword = Encryption().encryptPassword(password)
        self.registerAccountToDatabase(firstName, lastName, email, encryptedPassword)
        window.destroy()
        LoginGUI(LoginWindowController())