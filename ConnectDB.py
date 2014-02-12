import datetime
import wx
import wx.grid
import re
import MySQLdb
import MySQLdb.cursors
import gettext


def connectdb():  #global database connection
    try:
        return MySQLdb.connect(host="127.0.0.1", user="root", passwd="rappy3", db="records2")  

    except MySQLdb.DatabaseError:
        dlg = wx.MessageDialog(None,
                               message='Could not connect to Database.\n1) You can check if the database server is running.\n2) You can check if database still exists',
                               caption='A Message Box',
                               style=wx.OK|wx.ICON_INFORMATION
                               )
        dlg.ShowModal()
        dlg.Destroy()

def Age(birthdate):
   if birthdate is None:
       pass
   else:
       return int((datetime.datetime.now( ) - datetime.datetime.strptime(birthdate,"%m/%d/%y")).days/365.2425)