import datetime
import wx
import wx.grid
import re
import MySQLdb
import MySQLdb.cursors
import gettext
from ConnectDB import *

class AddSubject(wx.Frame):
    def __init__(self, *args, **kwds):
        # begin wxGlade: AddSubject.__init__
        kwds["style"] = wx.DEFAULT_FRAME_STYLE
        wx.Frame.__init__(self, wx.GetApp().TopWindow)
        self.label_1 = wx.StaticText(self, wx.ID_ANY, _("Subject"))
        self.text_ctrl_18 = wx.TextCtrl(self, wx.ID_ANY, "")
        self.AddSub = wx.Button(self, wx.ID_ANY, _("Add"))
        self.DeleteSub = wx.Button(self, wx.ID_ANY, _("Delete"))
        self.panel_3 = wx.Panel(self, wx.ID_ANY)
        self.grid_3 = wx.grid.Grid(self.panel_3, wx.ID_ANY, size=(1, 1))

        self.Bind(wx.EVT_BUTTON, self.add, self.AddSub)
        self.Bind(wx.EVT_BUTTON, self.delete, self.DeleteSub)
        self.__set_properties()
        self.__do_layout()
        # end wxGlade

    def __set_properties(self):
        # begin wxGlade: AddSubject.__set_properties
        self.SetTitle(_("Subjects"))
        self.SetSize((370, 376))
        self.label_1.SetFont(wx.Font(12, wx.DEFAULT, wx.NORMAL, wx.NORMAL, 0, "MS Shell Dlg 2"))
        self.AddSub.SetFont(wx.Font(12, wx.DEFAULT, wx.NORMAL, wx.NORMAL, 0, "MS Shell Dlg 2"))
        self.DeleteSub.SetFont(wx.Font(12, wx.DEFAULT, wx.NORMAL, wx.NORMAL, 0, "MS Shell Dlg 2"))
        self.grid_3.CreateGrid(50, 1)
        self.grid_3.SetRowLabelSize(30)
        self.grid_3.SetColLabelSize(30)
        self.grid_3.SetColLabelValue(0, _("Subject Name"))
        self.grid_3.SetColSize(0, 150)
        self.grid_3.SetMinSize((246, 354))
        self.refreshsubjects() 
        # end wxGlade

    def __do_layout(self):
        # begin wxGlade: AddSubject.__do_layout
        sizer_15 = wx.BoxSizer(wx.HORIZONTAL)
        sizer_15_copy = wx.BoxSizer(wx.HORIZONTAL)
        sizer_31 = wx.BoxSizer(wx.VERTICAL)
        sizer_32 = wx.BoxSizer(wx.VERTICAL)
        sizer_31.Add(self.label_1, 0, wx.TOP | wx.ALIGN_CENTER_HORIZONTAL, 80)
        sizer_31.Add(self.text_ctrl_18, 0, 0, 0)
        sizer_32.Add(self.AddSub, 0, wx.TOP | wx.ALIGN_CENTER_HORIZONTAL, 5)
        sizer_32.Add(self.DeleteSub, 0, wx.ALIGN_CENTER_HORIZONTAL, 0)
        sizer_31.Add(sizer_32, 1, wx.EXPAND, 0)
        sizer_15.Add(sizer_31, 0, wx.EXPAND, 0)
        sizer_15_copy.Add(self.grid_3, 1, wx.EXPAND, 0)
        self.panel_3.SetSizer(sizer_15_copy)
        sizer_15.Add(self.panel_3, 1, wx.EXPAND, 0)
        self.SetSizer(sizer_15)
        self.Layout()	
    def add(self, event):
        Subject= (self.text_ctrl_18.GetValue())	
        db = connectdb()
        cur = db.cursor()
        cur.execute("INSERT INTO Subjects (Subject_Name) VALUES (%s)", (Subject))
        db.commit()		
        cur.close()
        self.refreshsubjects()       
    def delete(self, event):
        Subject= (self.text_ctrl_18.GetValue())	
        db = connectdb()
        cur = db.cursor()
        cur.execute("DELETE FROM Subjects WHERE Subject_Name=%s", (Subject))
        db.commit()		
        cur.close()
        self.refreshsubjects() 
    def refreshsubjects(self):
        self.grid_3.ClearGrid()
        db = connectdb()
        cur = db.cursor()
        cur.execute("SELECT * FROM Subjects")
        rows=cur.fetchall()
       
        for i in range (0,len(rows)):
            for j in range(0,1):
                cell = rows[i]
                self.grid_3.SetCellValue(i,j,str(cell[j]))		
class Curriculum(wx.Frame):
    def __init__(self, *args, **kwds):
        # begin wxGlade: curriculum.__init__
        kwds["style"] = wx.DEFAULT_FRAME_STYLE
        wx.Frame.__init__(self, wx.GetApp().TopWindow)
        self.label_19_copy = wx.StaticText(self, wx.ID_ANY, _("School Year"))
        self.combo_box_4_copy = wx.ComboBox(self, wx.ID_ANY, choices=[], style=wx.CB_DROPDOWN)
        self.label_19 = wx.StaticText(self, wx.ID_ANY, _("Year/Grade"))
        self.combo_box_4 = wx.ComboBox(self, wx.ID_ANY, choices=[], style=wx.CB_DROPDOWN)
        self.Load = wx.Button(self, wx.ID_ANY, _("Load"))
        self.label_1 = wx.StaticText(self, wx.ID_ANY, _("Subject"))
        self.combo_box_4_copy_1 = wx.ComboBox(self, wx.ID_ANY, choices=[], style=wx.CB_DROPDOWN)
        self.AddSub = wx.Button(self, wx.ID_ANY, _("Add"))
        self.DeleteSub = wx.Button(self, wx.ID_ANY, _("Delete"))
        self.panel_3 = wx.Panel(self, wx.ID_ANY)
        self.grid_3 = wx.grid.Grid(self.panel_3, wx.ID_ANY, size=(1, 1))
        self.Bind(wx.EVT_BUTTON, self.load1, self.Load)		
        self.Bind(wx.EVT_BUTTON, self.add1, self.AddSub)		
        self.Bind(wx.EVT_BUTTON, self.delete1, self.DeleteSub)	
        self.__set_properties()
        self.__do_layout()
        # end wxGlade

    def __set_properties(self):
        # begin wxGlade: curriculum.__set_properties
        self.SetTitle(_("Curriculum"))
        self.SetSize((352, 385))
        self.label_19_copy.SetFont(wx.Font(12, wx.DEFAULT, wx.NORMAL, wx.NORMAL, 0, "MS Shell Dlg 2"))
        self.label_19.SetFont(wx.Font(12, wx.DEFAULT, wx.NORMAL, wx.NORMAL, 0, "MS Shell Dlg 2"))
        self.Load.SetFont(wx.Font(12, wx.DEFAULT, wx.NORMAL, wx.NORMAL, 0, "MS Shell Dlg 2"))
        self.label_1.SetFont(wx.Font(12, wx.DEFAULT, wx.NORMAL, wx.NORMAL, 0, "MS Shell Dlg 2"))
        self.AddSub.SetFont(wx.Font(12, wx.DEFAULT, wx.NORMAL, wx.NORMAL, 0, "MS Shell Dlg 2"))
        self.DeleteSub.SetFont(wx.Font(12, wx.DEFAULT, wx.NORMAL, wx.NORMAL, 0, "MS Shell Dlg 2"))
        self.grid_3.CreateGrid(50, 1)
        self.grid_3.SetRowLabelSize(30)
        self.grid_3.SetColLabelSize(30)
        self.grid_3.EnableEditing(0)
        self.grid_3.SetColLabelValue(0, _("Subject Name"))
        self.grid_3.SetColSize(0, 150)
        self.grid_3.SetMinSize((246, 354))
        # end wxGlade

    def __do_layout(self):
        # begin wxGlade: curriculum.__do_layout
        sizer_15 = wx.BoxSizer(wx.HORIZONTAL)
        sizer_15_copy = wx.BoxSizer(wx.HORIZONTAL)
        sizer_31 = wx.BoxSizer(wx.VERTICAL)
        sizer_32 = wx.BoxSizer(wx.VERTICAL)
        sizer_31.Add(self.label_19_copy, 0, wx.TOP | wx.ALIGN_CENTER_HORIZONTAL, 20)
        sizer_31.Add(self.combo_box_4_copy, 0, 0, 0)
        sizer_31.Add(self.label_19, 0, wx.ALIGN_CENTER_HORIZONTAL, 40)
        sizer_31.Add(self.combo_box_4, 0, 0, 0)
        sizer_31.Add(self.Load, 0, wx.TOP | wx.ALIGN_CENTER_HORIZONTAL, 5)
        sizer_31.Add(self.label_1, 0, wx.TOP | wx.ALIGN_CENTER_HORIZONTAL, 20)
        sizer_31.Add(self.combo_box_4_copy_1, 0, 0, 0)
        sizer_32.Add(self.AddSub, 0, wx.TOP | wx.ALIGN_CENTER_HORIZONTAL, 5)
        sizer_32.Add(self.DeleteSub, 0, wx.ALIGN_CENTER_HORIZONTAL, 0)
        sizer_31.Add(sizer_32, 1, wx.EXPAND, 0)
        sizer_15.Add(sizer_31, 0, wx.EXPAND, 0)
        sizer_15_copy.Add(self.grid_3, 1, wx.EXPAND, 0)
        self.panel_3.SetSizer(sizer_15_copy)
        sizer_15.Add(self.panel_3, 1, wx.EXPAND, 0)
        self.SetSizer(sizer_15)
        self.Layout()

    def load1(self, event):
        SY= (self.combo_box_4_copy.GetValue())	
        Year= (self.combo_box_4.GetValue())	
        db = connectdb()
        cur = db.cursor()
        cur.execute("SELECT Subjects FROM Curriculum WHERE SchoolYear= %s AND Year= %s", (SY,Year))
        rows=cur.fetchall()
        for i in range (0,len(rows)):
            for j in range(0,1):
                cell = rows[i]
                self.grid_3.SetCellValue(i,j,str(cell[j]))			

        self.refreshsubjects()   		
    def add1(self, event):
        SY= (self.combo_box_4_copy.GetValue())	
        Year= (self.combo_box_4.GetValue())	
     	Subject= (self.combo_box_4_copy_1.GetValue())	
        db = connectdb()
        cur = db.cursor()
        cur.execute("INSERT INTO Curriculum (SchoolYear, Year, Subjects) VALUES (%s, %s, %s)", (SY, Year, Subject))
        db.commit()		
        cur.close()
        self.refreshsubjects()       
    def delete1(self, event):
        Subject= (self.combo_box_4_copy_1.GetValue())	
        db = connectdb()
        cur = db.cursor()
        cur.execute("DELETE FROM Curriculum WHERE SchoolYear=%s, Year=%s, Subjects=%s", (SY, Year, Subject))
        db.commit()		
        cur.close()
        self.refreshsubjects() 
    def refreshsubjects(self):
        SY= (self.combo_box_4_copy.GetValue())	
        Year= (self.combo_box_4.GetValue())	
        self.grid_3.ClearGrid()
        db = connectdb()
        cur = db.cursor()
        cur.execute("SELECT Subjects FROM Curriculum WHERE SchoolYear= %s AND Year= %s", (SY,Year))
        rows=cur.fetchall()
       
        for i in range (0,len(rows)):
            for j in range(0,1):
                cell = rows[i]
                self.grid_3.SetCellValue(i,j,str(cell[j]))	