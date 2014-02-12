import datetime
import wx
import wx.grid
import re
import MySQLdb
import MySQLdb.cursors
import gettext
from ConnectDB import *

class Grades(wx.Frame):
    def __init__(self, *args, **kwds):
        # begin wxGlade: Grades.__init__
        kwds["style"] = wx.DEFAULT_FRAME_STYLE
        wx.Frame.__init__(self, wx.GetApp().TopWindow)
        self.label_1 = wx.StaticText(self, wx.ID_ANY, _("SY"))
        self.SY = wx.ComboBox(self, wx.ID_ANY, choices=[_("2012-2013"), _("2013-2014"), _("2014-2015"), _("2015-2016"), _("2016-2017"), _("2017-2018"), _("2018-2019")], style=wx.CB_DROPDOWN | wx.CB_DROPDOWN | wx.CB_READONLY)
        self.label_1_copy = wx.StaticText(self, wx.ID_ANY, _("Year/Grade"))
        self.Year = wx.ComboBox(self, wx.ID_ANY, choices=[_(""),_("Grade1"), _("Grade2"), _("Grade3"), _("Grade4"), _("Grade5"), _("Grade6"), _("Year1"), _("Year2"), _("Year3"), _("Year4")], style=wx.CB_DROPDOWN | wx.CB_DROPDOWN | wx.CB_READONLY)
        self.label_1_copy_1 = wx.StaticText(self, wx.ID_ANY, _("Section"))
        self.Section = wx.ComboBox(self, wx.ID_ANY, choices=[_(""),_("Section1"), _("Section2"), _("Section3"), _("Section4")], style=wx.CB_DROPDOWN | wx.CB_DROPDOWN | wx.CB_READONLY)
        self.label_1_copy_2 = wx.StaticText(self, wx.ID_ANY, _("Subject"))
        self.Subject = wx.ComboBox(self, wx.ID_ANY, choices=[], style=wx.CB_DROPDOWN | wx.CB_DROPDOWN | wx.CB_READONLY)
        self.label4 = wx.StaticText(self, wx.ID_ANY, _("Term/Grading"))
        self.Term = wx.ComboBox(self, wx.ID_ANY, choices=[_("1st"), _("2nd"), _("3rd"), _("4th")], style=wx.CB_DROPDOWN | wx.CB_DROPDOWN | wx.CB_READONLY)
        self.load_button = wx.Button(self, wx.ID_ANY, _("Load"))
        self.panel_1 = wx.Panel(self, wx.ID_ANY)
        self.tablegrades = wx.grid.Grid(self.panel_1, wx.ID_ANY, size=(1, 1))
        self.EditButton = wx.Button(self, wx.ID_ANY, _("Edit"))
        self.SaveButton = wx.Button(self, wx.ID_ANY, _("Save"))
		
		
        self.Bind(wx.EVT_BUTTON, self.OnLoad, self.load_button)## load grades
        self.Bind(wx.EVT_BUTTON, self.OnEdit, self.EditButton)## edit grades
        self.Bind(wx.EVT_BUTTON, self.OnSave, self.SaveButton)## save grades
		
        self.__set_properties()
        self.__do_layout()
        # end wxGlade

    def __set_properties(self):
        # begin wxGlade: Grades.__set_properties
        self.SetTitle(_("Grades"))
        self.SetSize((583, 676))
        self.label_1.SetFont(wx.Font(16, wx.DEFAULT, wx.NORMAL, wx.NORMAL, 0, "MS Shell Dlg 2"))
        self.SY.SetSelection(-1)
        self.label_1_copy.SetFont(wx.Font(16, wx.DEFAULT, wx.NORMAL, wx.NORMAL, 0, "MS Shell Dlg 2"))
        self.Year.SetSelection(-1)
        self.label_1_copy_1.SetFont(wx.Font(16, wx.DEFAULT, wx.NORMAL, wx.NORMAL, 0, "MS Shell Dlg 2"))
        self.Section.SetSelection(-1)
        self.label_1_copy_2.SetFont(wx.Font(16, wx.DEFAULT, wx.NORMAL, wx.NORMAL, 0, "MS Shell Dlg 2"))
        self.Subject.SetSelection(-1)
        self.label4.SetFont(wx.Font(16, wx.DEFAULT, wx.NORMAL, wx.NORMAL, 0, "MS Shell Dlg 2"))
        self.Term.SetSelection(-1)
        self.tablegrades.CreateGrid(60, 5)
        self.tablegrades.SetRowLabelSize(30)
        self.tablegrades.SetColLabelValue(0, _("ID Number"))
        self.tablegrades.SetColLabelValue(1, _("Last Name"))
        self.tablegrades.SetColSize(1, 100)
        self.tablegrades.SetColLabelValue(2, _("First Name"))
        self.tablegrades.SetColSize(2, 140)
        self.tablegrades.SetColLabelValue(3, _("Middle Name"))
        self.tablegrades.SetColSize(3, 100)
        self.tablegrades.SetColLabelValue(4, _("Grade"))
        self.tablegrades.SetMinSize((546, 559))
        self.tablegrades.EnableEditing(False)
        self.SaveButton.Enable(False)
        self.loadsubjects()

    def __do_layout(self):
        # begin wxGlade: Grades.__do_layout
        sizer_33 = wx.BoxSizer(wx.VERTICAL)
        sizer_35 = wx.BoxSizer(wx.HORIZONTAL)
        sizer_4 = wx.BoxSizer(wx.HORIZONTAL)
        sizer_8 = wx.BoxSizer(wx.HORIZONTAL)
        sizer_34_copy = wx.BoxSizer(wx.HORIZONTAL)
        sizer_34 = wx.BoxSizer(wx.HORIZONTAL)
        sizer_34.Add(self.label_1, 0, wx.RIGHT, 45)
        sizer_34.Add(self.SY, 0, 0, 0)
        sizer_34.Add(self.label_1_copy, 0, wx.RIGHT, 25)
        sizer_34.Add(self.Year, 0, 0, 0)
        sizer_34.Add(self.label_1_copy_1, 0, 0, 0)
        sizer_34.Add(self.Section, 0, 0, 0)
        sizer_33.Add(sizer_34, 0, wx.EXPAND, 0)
        sizer_34_copy.Add(self.label_1_copy_2, 0, 0, 0)
        sizer_34_copy.Add(self.Subject, 0, 0, 0)
        sizer_34_copy.Add(self.label4, 0, 0, 0)
        sizer_34_copy.Add(self.Term, 0, 0, 0)
        sizer_34_copy.Add(self.load_button, 0, wx.LEFT, 70)
        sizer_33.Add(sizer_34_copy, 0, wx.EXPAND, 0)
        sizer_8.Add(self.tablegrades, 1, wx.EXPAND, 0)
        self.panel_1.SetSizer(sizer_8)
        sizer_4.Add(self.panel_1, 1, wx.EXPAND, 0)
        sizer_33.Add(sizer_4, 1, wx.EXPAND, 0)
        sizer_35.Add(self.EditButton, 0, wx.LEFT, 380)
        sizer_35.Add(self.SaveButton, 0, 0, 0)
        sizer_33.Add(sizer_35, 0, wx.EXPAND, 0)
        self.SetSizer(sizer_33)
        self.Layout()
        
    def OnLoad(self,event):
        self.tablegrades.ClearGrid()
        SY=(self.SY.GetValue())
        Year=(self.Year.GetValue())	
        Section=(self.Section.GetValue())		
        Subject=(self.Subject.GetValue())
        Term=(self.Term.GetValue())
        db = connectdb()
        cur = db.cursor()
        cur.execute("SELECT Students.Student_ID, Students.LastName, Students.FirstName, Students.MiddleName, Grades.Subject_Grade FROM Students, Grades, ClassRecords WHERE Students.Student_ID=ClassRecords.Students_Student_ID AND Grades.Students_Student_ID=ClassRecords.Students_Student_ID AND Grades.SchoolYear= %s AND ClassRecords.Year= %s AND ClassRecords.Section= %s AND Grades.Subject_Name= %s AND Grades.Grading= %s ",(SY, Year, Section, Subject, Term))
        rows=cur.fetchall()
       #print rows

        for i in range (0,len(rows)):     ####for loop
            for j in range(0,5):
                cell = rows[i]            ####access tuples database
                self.tablegrades.SetCellValue(i,j,str(cell[j]))
        self.tablegrades.EnableEditing(False)
        self.SaveButton.Enable(False)
        self.EditButton.Enable(True)
        
    def loadsubjects(self):
        db=connectdb()
        cur1=db.cursor()
        cur1.execute("SELECT Subject_Name FROM Subjects")
        
        x=[]
        index=0
        all=cur1.fetchall()
			
        while index<len(all):
            x.append(all[index][0])
            index=index+1
        self.Subject.SetItems(x)

    def OnEdit(self,event):
        self.tablegrades.EnableEditing(True)
        self.SaveButton.Enable(True)
        self.EditButton.Enable(False)
    def OnSave(self,event):
	
        SY=(self.SY.GetValue())        
        Subject=(self.Subject.GetValue()) 
        Year=(self.Year.GetValue())	
        Section=(self.Section.GetValue())		
        Term=(self.Term.GetValue()) 	
	
        
        db = connectdb()
        cur = db.cursor()
		

        cur.execute("SELECT Students.Student_ID, Students.LastName, Students.FirstName, Students.MiddleName FROM Students, ClassRecords WHERE Students.Student_ID=ClassRecords.Students_Student_ID AND ClassRecords.SchoolYear= %s AND ClassRecords.Year= %s AND ClassRecords.Section= %s",(SY, Year, Section))
        rows=cur.fetchall()


				
        x=list() ###Grades_List
        for i in range (0,len(rows)):
            x.append(self.tablegrades.GetCellValue(i,4))
        
        y=list() ###Student_ID list
        for i in range (0,len(rows)):
            y.append(self.tablegrades.GetCellValue(i,0))
			
        for i in range (0,len(rows)):
            cur.execute("""UPDATE Grades 
			            SET Subject_Grade=%s WHERE Subject_Name=%s AND Students_Student_ID=%s AND SchoolYear=%s AND Grading=%s""", (x[i], Subject, y[i], SY, Term))

            db.commit()		
        cur.close()
        self.tablegrades.EnableEditing(False)
        self.SaveButton.Enable(False)
        self.EditButton.Enable(True)

class InputGrades(wx.Frame):
    def __init__(self, *args, **kwds):
        # begin wxGlade: InputGrades.__init__
        kwds["style"] = wx.DEFAULT_FRAME_STYLE
        wx.Frame.__init__(self, wx.GetApp().TopWindow)
        self.label_1 = wx.StaticText(self, wx.ID_ANY, _("SY"))
        self.SY = wx.ComboBox(self, wx.ID_ANY, choices=[_("2012-2013"), _("2013-2014"), _("2014-2015"), _("2015-2016"), _("2016-2017"), _("2017-2018"), _("2018-2019")], style=wx.CB_DROPDOWN | wx.CB_DROPDOWN | wx.CB_READONLY)
        self.label_1_copy = wx.StaticText(self, wx.ID_ANY, _("Year/Grade"))
        self.Year = wx.ComboBox(self, wx.ID_ANY, choices=[_(""),_("Grade1"), _("Grade2"), _("Grade3"), _("Grade4"), _("Grade5"), _("Grade6"), _("Year1"), _("Year2"), _("Year3"), _("Year4")], style=wx.CB_DROPDOWN | wx.CB_DROPDOWN | wx.CB_READONLY)
        self.label_1_copy_1 = wx.StaticText(self, wx.ID_ANY, _("Section"))
        self.Section = wx.ComboBox(self, wx.ID_ANY, choices=[_(""),_("Section1"), _("Section2"), _("Section3"), _("Section4")], style=wx.CB_DROPDOWN | wx.CB_DROPDOWN | wx.CB_READONLY)
        self.load_button = wx.Button(self, wx.ID_ANY, _("Load"))
        self.panel_1 = wx.Panel(self, wx.ID_ANY)
        self.tablegrades = wx.grid.Grid(self.panel_1, wx.ID_ANY, size=(1, 1))
        self.label_1_copy_2 = wx.StaticText(self, wx.ID_ANY, _("Subject"))
        self.Subject = wx.ComboBox(self, wx.ID_ANY, choices=[], style=wx.CB_DROPDOWN | wx.CB_DROPDOWN | wx.CB_READONLY)
        self.label4 = wx.StaticText(self, wx.ID_ANY, _("Term/Grading"))
        self.Term = wx.ComboBox(self, wx.ID_ANY, choices=[_("1st"), _("2nd"), _("3rd"), _("4th")], style=wx.CB_DROPDOWN | wx.CB_DROPDOWN | wx.CB_READONLY)
        self.input_grades = wx.Button(self, wx.ID_ANY, _("Input Grades"))
        self.Bind(wx.EVT_BUTTON, self.OnLoad, self.load_button)## load class records
        self.Bind(wx.EVT_BUTTON, self.OnInput, self.input_grades)## define input grades
        self.__set_properties()
        self.__do_layout()
        # end wxGlade

    def __set_properties(self):
        # begin wxGlade: InputGrades.__set_properties
        self.SetTitle(_("Input Grades"))
        self.label_1.SetFont(wx.Font(16, wx.DEFAULT, wx.NORMAL, wx.NORMAL, 0, "MS Shell Dlg 2"))
        self.SY.SetSelection(-1)
        self.label_1_copy.SetFont(wx.Font(16, wx.DEFAULT, wx.NORMAL, wx.NORMAL, 0, "MS Shell Dlg 2"))
        self.Year.SetSelection(-1)
        self.label_1_copy_1.SetFont(wx.Font(16, wx.DEFAULT, wx.NORMAL, wx.NORMAL, 0, "MS Shell Dlg 2"))
        self.Section.SetSelection(-1)
        self.tablegrades.CreateGrid(60, 5)
        self.tablegrades.SetRowLabelSize(30)
        self.tablegrades.SetColLabelValue(0, _("ID Number"))
        self.tablegrades.SetColLabelValue(1, _("Last Name"))
        self.tablegrades.SetColSize(1, 100)
        self.tablegrades.SetColLabelValue(2, _("First Name"))
        self.tablegrades.SetColSize(2, 140)
        self.tablegrades.SetColLabelValue(3, _("Middle Name"))
        self.tablegrades.SetColSize(3, 100)
        self.tablegrades.SetColLabelValue(4, _("Grade"))
        self.tablegrades.SetMinSize((546, 559))
        self.label_1_copy_2.SetFont(wx.Font(16, wx.DEFAULT, wx.NORMAL, wx.NORMAL, 0, "MS Shell Dlg 2"))
        self.Subject.SetSelection(-1)
        self.label4.SetFont(wx.Font(16, wx.DEFAULT, wx.NORMAL, wx.NORMAL, 0, "MS Shell Dlg 2"))
        self.Term.SetSelection(-1)
        self.loadsubjects()
        # end wxGlade

    def __do_layout(self):
        # begin wxGlade: InputGrades.__do_layout
        sizer_33 = wx.BoxSizer(wx.VERTICAL)
        sizer_34_copy = wx.BoxSizer(wx.HORIZONTAL)
        sizer_4 = wx.BoxSizer(wx.HORIZONTAL)
        sizer_8 = wx.BoxSizer(wx.HORIZONTAL)
        sizer_34 = wx.BoxSizer(wx.HORIZONTAL)
        sizer_34.Add(self.label_1, 0, 0, 0)
        sizer_34.Add(self.SY, 0, 0, 0)
        sizer_34.Add(self.label_1_copy, 0, 0, 0)
        sizer_34.Add(self.Year, 0, 0, 0)
        sizer_34.Add(self.label_1_copy_1, 0, 0, 0)
        sizer_34.Add(self.Section, 0, 0, 0)
        sizer_34.Add(self.load_button, 0, 0, 0)
        sizer_33.Add(sizer_34, 0, wx.EXPAND, 0)
        sizer_8.Add(self.tablegrades, 1, wx.EXPAND, 0)
        self.panel_1.SetSizer(sizer_8)
        sizer_4.Add(self.panel_1, 1, wx.EXPAND, 0)
        sizer_33.Add(sizer_4, 1, wx.EXPAND, 0)
        sizer_34_copy.Add(self.label_1_copy_2, 0, 0, 0)
        sizer_34_copy.Add(self.Subject, 0, 0, 0)
        sizer_34_copy.Add(self.label4, 0, 0, 0)
        sizer_34_copy.Add(self.Term, 0, 0, 0)
        sizer_34_copy.Add(self.input_grades, 0, 0, 0)
        sizer_33.Add(sizer_34_copy, 0, wx.EXPAND, 0)
        self.SetSizer(sizer_33)
        sizer_33.Fit(self)
        self.Layout()	

    def OnLoad(self,event):
        self.tablegrades.ClearGrid()
        SY=(self.SY.GetValue())
        Year=(self.Year.GetValue())	
        Section=(self.Section.GetValue())		
        db = connectdb()
        cur = db.cursor()
        cur.execute("SELECT Students.Student_ID, Students.LastName, Students.FirstName, Students.MiddleName FROM Students, ClassRecords WHERE Students.Student_ID=ClassRecords.Students_Student_ID AND ClassRecords.SchoolYear= %s AND ClassRecords.Year= %s AND ClassRecords.Section= %s",(SY, Year, Section))
        rows=cur.fetchall()
        #print rows

        for i in range (0,len(rows)):     ####for loop
            for j in range(0,4):
                cell = rows[i]            ####access tuples database
                self.tablegrades.SetCellValue(i,j,str(cell[j]))
        self.loadsubjects()
        self.input_grades.Enable(True)

    def OnInput(self,event):
	
        SY=(self.SY.GetValue())        
        Subject=(self.Subject.GetValue()) 
        Year=(self.Year.GetValue())	
        Section=(self.Section.GetValue())		
        Term=(self.Term.GetValue()) 	
	
        
        db = connectdb()
        cur = db.cursor()
		

        cur.execute("SELECT Students.Student_ID, Students.LastName, Students.FirstName, Students.MiddleName FROM Students, ClassRecords WHERE Students.Student_ID=ClassRecords.Students_Student_ID AND ClassRecords.SchoolYear= %s AND ClassRecords.Year= %s AND ClassRecords.Section= %s",(SY, Year, Section))
        rows=cur.fetchall()


				
        x=list() ###Grades_List
        for i in range (0,len(rows)):
            x.append(self.tablegrades.GetCellValue(i,4))
        
        y=list() ###Student_ID list
        for i in range (0,len(rows)):
            y.append(self.tablegrades.GetCellValue(i,0))
			
        for i in range (0,len(rows)):
            cur.execute("INSERT INTO Grades (Subject_Grade, Subject_Name, Students_Student_ID, SchoolYear, Grading) VALUES (%s, %s, %s, %s, %s)", (x[i], Subject, y[i], SY, Term))

            db.commit()		
        cur.close()
        self.input_grades.Enable(False)
    def loadsubjects(self):
        db=connectdb()
        cur1=db.cursor()
        cur1.execute("SELECT Subject_Name FROM Subjects")
        
        x=[]
        index=0
        all=cur1.fetchall()
			
        while index<len(all):
            x.append(all[index][0])
            index=index+1
        self.Subject.SetItems(x)	
				