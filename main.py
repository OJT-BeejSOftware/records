import wx
import wx.grid
import gettext

from CreateRecords import NewStudent, NewTeacher
from ViewRecords import ViewRecords
from EditRecords import EditRecords

from ClassRecords import ClassRecordsMain
from SubjectsCurriculum import AddSubject, Curriculum  
from Grades import Grades, InputGrades


		
class MainFrame(wx.Frame):
    def __init__(self, *args, **kwds):
        # begin wxGlade: MainFrame.__init__
        kwds["style"] = wx.DEFAULT_FRAME_STYLE
        wx.Frame.__init__(self, *args, **kwds)
        self.ClassRecords = wx.Button(self, wx.ID_ANY, _("Class Records"))
        self.Grades = wx.Button(self, wx.ID_ANY, _(" Grades"))
        self.Curriculum = wx.Button(self, wx.ID_ANY, _("Curriculum"))
        self.InputGrades = wx.Button(self, wx.ID_ANY, _(" Input Grades"))
        self.Subjects = wx.Button(self, wx.ID_ANY, _("Subjects"))
        self.Attendance = wx.Button(self, wx.ID_ANY, _("Attendance"))
        self.ViewRecords = wx.Button(self, wx.ID_ANY, _("View Records"))
        self.CreateNewStudent = wx.Button(self, wx.ID_ANY, _("Create New Student"))
        self.EditRecords = wx.Button(self, wx.ID_ANY, _("Edit Records"))
        self.CreateNewTeacher = wx.Button(self, wx.ID_ANY, _("Create New Teacher"))
        ##mainframe buttons
        self.Bind(wx.EVT_BUTTON, self.createstudent, self.CreateNewStudent)			
        self.Bind(wx.EVT_BUTTON, self.view, self.ViewRecords)
        self.Bind(wx.EVT_BUTTON, self.createteacher, self.CreateNewTeacher)
        self.Bind(wx.EVT_BUTTON, self.edit, self.EditRecords)
        self.Bind(wx.EVT_BUTTON, self.classrecords1, self.ClassRecords)
        self.Bind(wx.EVT_BUTTON, self.grades1, self.Grades)
        self.Bind(wx.EVT_BUTTON, self.curriculum1, self.Curriculum)
        self.Bind(wx.EVT_BUTTON, self.InputGrades1, self.InputGrades)
        self.Bind(wx.EVT_BUTTON, self.Subjects1, self.Subjects)
        self.Bind(wx.EVT_BUTTON, self.attendance1, self.Attendance)
        self.__set_properties()
        self.__do_layout()
    def __set_properties(self):
        # begin wxGlade: MainFrame.__set_properties
        self.SetTitle(_("CKHS l Database"))
        self.ClassRecords.SetMinSize((200, 40))
        self.ClassRecords.SetFont(wx.Font(14, wx.DEFAULT, wx.NORMAL, wx.NORMAL, 0, "MS Shell Dlg 2"))
        self.Grades.SetMinSize((200, 40))
        self.Grades.SetFont(wx.Font(14, wx.DEFAULT, wx.NORMAL, wx.NORMAL, 0, "MS Shell Dlg 2"))
        self.Curriculum.SetMinSize((200, 40))
        self.Curriculum.SetFont(wx.Font(14, wx.DEFAULT, wx.NORMAL, wx.NORMAL, 0, "MS Shell Dlg 2"))
        self.InputGrades.SetMinSize((200, 40))
        self.InputGrades.SetFont(wx.Font(14, wx.DEFAULT, wx.NORMAL, wx.NORMAL, 0, "MS Shell Dlg 2"))
        self.Subjects.SetMinSize((200, 40))
        self.Subjects.SetFont(wx.Font(14, wx.DEFAULT, wx.NORMAL, wx.NORMAL, 0, "MS Shell Dlg 2"))
        self.Attendance.SetMinSize((200, 40))
        self.Attendance.SetFont(wx.Font(14, wx.DEFAULT, wx.NORMAL, wx.NORMAL, 0, "MS Shell Dlg 2"))
        self.ViewRecords.SetMinSize((130, 40))
        self.ViewRecords.SetFont(wx.Font(14, wx.DEFAULT, wx.NORMAL, wx.NORMAL, 0, "MS Shell Dlg 2"))
        self.CreateNewStudent.SetMinSize((200, 40))
        self.CreateNewStudent.SetFont(wx.Font(14, wx.DEFAULT, wx.NORMAL, wx.NORMAL, 0, "MS Shell Dlg 2"))
        self.EditRecords.SetMinSize((130, 40))
        self.EditRecords.SetFont(wx.Font(14, wx.DEFAULT, wx.NORMAL, wx.NORMAL, 0, "MS Shell Dlg 2"))
        self.CreateNewTeacher.SetMinSize((200, 40))
        self.CreateNewTeacher.SetFont(wx.Font(14, wx.DEFAULT, wx.NORMAL, wx.NORMAL, 0, "MS Shell Dlg 2"))
    def __do_layout(self):
        # begin wxGlade: MainFrame.__do_layout
        sizer_18 = wx.BoxSizer(wx.VERTICAL)
        sizer_27 = wx.BoxSizer(wx.HORIZONTAL)
        sizer_26 = wx.BoxSizer(wx.HORIZONTAL)
        sizer_25 = wx.BoxSizer(wx.HORIZONTAL)
        sizer_24 = wx.BoxSizer(wx.HORIZONTAL)
        sizer_23 = wx.BoxSizer(wx.HORIZONTAL)
        sizer_22 = wx.BoxSizer(wx.HORIZONTAL)
        sizer_21 = wx.BoxSizer(wx.HORIZONTAL)
        sizer_20 = wx.BoxSizer(wx.HORIZONTAL)
        sizer_20.Add((410, 50), 0, 0, 0)
        sizer_20.Add(self.ClassRecords, 0, 0, 0)
        sizer_18.Add(sizer_20, 0, wx.EXPAND, 0)
        sizer_21.Add((410, 50), 0, 0, 0)
        sizer_21.Add(self.Grades, 0, 0, 0)
        sizer_18.Add(sizer_21, 0, wx.EXPAND, 0)
        sizer_22.Add((410, 50), 0, 0, 0)
        sizer_22.Add(self.Curriculum, 0, 0, 0)
        sizer_18.Add(sizer_22, 0, wx.EXPAND, 0)
        sizer_23.Add((410, 50), 0, 0, 0)
        sizer_23.Add(self.InputGrades, 0, 0, 0)
        sizer_18.Add(sizer_23, 0, wx.EXPAND, 0)
        sizer_24.Add((410, 50), 0, 0, 0)
        sizer_24.Add(self.Subjects, 0, 0, 0)
        sizer_18.Add(sizer_24, 0, wx.EXPAND, 0)
        sizer_25.Add((410, 50), 0, 0, 0)
        sizer_25.Add(self.Attendance, 0, 0, 0)
        sizer_18.Add(sizer_25, 0, wx.EXPAND, 0)
        sizer_26.Add(self.ViewRecords, 0, 0, 0)
        sizer_26.Add((280, 50), 0, 0, 0)
        sizer_26.Add(self.CreateNewStudent, 0, 0, 0)
        sizer_18.Add(sizer_26, 0, wx.EXPAND, 0)
        sizer_27.Add(self.EditRecords, 0, 0, 0)
        sizer_27.Add((280, 50), 0, 0, 0)
        sizer_27.Add(self.CreateNewTeacher, 0, 0, 0)
        sizer_18.Add(sizer_27, 0, wx.EXPAND, 0)
        self.SetSizer(sizer_18)
        sizer_18.Fit(self)
        self.Layout()
    def createstudent(self,event):
		NewStudent().Show()
    def createteacher(self,event):
		NewTeacher().Show()		
    def view(self,event):
		ViewRecords().Show()
    def edit(self,event):
		EditRecords().Show()
    def classrecords1(self,event):
	    ClassRecordsMain().Show()
    def InputGrades1(self,event):	
	    InputGrades().Show()
    def grades1(self,event):	
	    Grades().Show()
    def curriculum1(self,event):	
        Curriculum().Show()
    def Subjects1(self,event):
        AddSubject().Show()	
    def attendance1(self,event):
        pass
	
			
if __name__ == "__main__":
    gettext.install("app1") # replace with the appropriate catalog name
    app1 = wx.PySimpleApp(0)
    wx.InitAllImageHandlers()
    MainFrame = MainFrame(None, wx.ID_ANY, "")
    app1.SetTopWindow(MainFrame)
    MainFrame.Show()
    app1.MainLoop()