import datetime
import wx
import wx.grid
import re
import MySQLdb
import MySQLdb.cursors
import gettext
from ConnectDB import *

class ViewRecords(wx.Frame):
    def __init__(self, *args, **kwds):
        # begin wxGlade: ViewRecords.__init__
        kwds["style"] = wx.DEFAULT_FRAME_STYLE
        wx.Frame.__init__(self, wx.GetApp().TopWindow)
        self.notebook_1 = wx.Notebook(self, wx.ID_ANY, style=0)
        self.notebook_1_pane_1 = wx.Panel(self.notebook_1, wx.ID_ANY)
        self.panel_1 = wx.Panel(self.notebook_1_pane_1, wx.ID_ANY)
        self.grid_1 = wx.grid.Grid(self.panel_1, wx.ID_ANY, size=(1, 1))
        self.refresh = wx.Button(self.notebook_1_pane_1, wx.ID_ANY, _("Refresh"))
        self.notebook_1_pane_2 = wx.Panel(self.notebook_1, wx.ID_ANY)
        self.panel_1_copy = wx.Panel(self.notebook_1_pane_2, wx.ID_ANY)
        self.grid_1_copy = wx.grid.Grid(self.panel_1_copy, wx.ID_ANY, size=(1, 1))
        self.refresh_copy = wx.Button(self.notebook_1_pane_2, wx.ID_ANY, _("Refresh"))
        self.notebook_1_pane_3 = wx.Panel(self.notebook_1, wx.ID_ANY)
		###
        self.Bind(wx.EVT_BUTTON, self.refreshbutton, self.refresh)
        self.__set_properties()
        self.__do_layout()
        # end wxGlade
    def refreshbutton(self, event):   
       	self.refreshdata()
    def refreshdata(self):
        self.grid_1.ClearGrid()
        self.grid_1_copy.ClearGrid()
        db = connectdb()
        cur = db.cursor()
        cur.execute("SELECT * FROM Students")
        rows=cur.fetchall()

        for i in range (0,len(rows)):
            for j in range(0,19):
                cell = rows[i]
                self.grid_1.SetCellValue(i,j,str(cell[j]))
        #x=list()
        #for i in range (0,len(rows)):
        #    x.append(self.grid_1.GetCellValue(i,1))
        #for i in range (0,len(rows)):
		#    print x[i]
      
        cur.execute("SELECT * FROM Teachers")
        rows1=cur.fetchall()
       
        for i1 in range (0,len(rows1)):
            for j1 in range(0,15):
                cell1 = rows1[i1]
                self.grid_1_copy.SetCellValue(i1,j1,str(cell1[j1]))		
				
    def __set_properties(self):
        # begin wxGlade: ViewRecords.__set_properties
        self.SetTitle(_("View Records"))
        self.SetSize((727, 589))
        #row=studentrow()
        self.grid_1.CreateGrid(20000, 19)#####################################################!!!!
        self.grid_1.SetColLabelValue(0, _("ID"))
        self.grid_1.SetColLabelValue(1, _("LastName"))
        self.grid_1.SetColSize(1, 100)
        self.grid_1.SetColLabelValue(2, _("FirstName"))
        self.grid_1.SetColSize(2, 120)
        self.grid_1.SetColLabelValue(3, _("MiddleName"))
        self.grid_1.SetColSize(3, 100)
        self.grid_1.SetColLabelValue(4, _("BirthDate"))
        self.grid_1.SetColLabelValue(5, _("Gender"))
        self.grid_1.SetColLabelValue(6, _("Nationality"))
        self.grid_1.SetColLabelValue(7, _("Address"))
        self.grid_1.SetColSize(7, 120)
        self.grid_1.SetColLabelValue(8, _("City"))
        self.grid_1.SetColLabelValue(9, _("Region"))
        self.grid_1.SetColLabelValue(10, _("Country"))
        self.grid_1.SetColLabelValue(11, _("Guardian's LastName"))
        self.grid_1.SetColSize(11, 120)
        self.grid_1.SetColLabelValue(12, _("Guardian's FirstName"))
        self.grid_1.SetColSize(12, 120)
        self.grid_1.SetColLabelValue(13, _("Guardian's Contactno"))
        self.grid_1.SetColSize(13, 120)
        self.grid_1.SetColLabelValue(14, _("Telephone Number"))
        self.grid_1.SetColSize(14, 120)
        self.grid_1.SetColLabelValue(15, _("Cell Number"))
        self.grid_1.SetColSize(15, 100)
        self.grid_1.SetColLabelValue(16, _("Email"))
        self.grid_1.SetColSize(16, 120)
        self.grid_1.SetColLabelValue(17, _("Year/Grade"))
        self.grid_1.SetColLabelValue(18, _("Year Entered"))
        self.grid_1_copy.CreateGrid(20000, 15)#######################################!!!!!
        self.grid_1_copy.SetColLabelValue(0, _("ID"))
        self.grid_1_copy.SetColLabelValue(1, _("LastName"))
        self.grid_1_copy.SetColSize(1, 100)
        self.grid_1_copy.SetColLabelValue(2, _("FirstName"))
        self.grid_1_copy.SetColSize(2, 120)
        self.grid_1_copy.SetColLabelValue(3, _("MiddleName"))
        self.grid_1_copy.SetColSize(3, 100)
        self.grid_1_copy.SetColLabelValue(4, _("BirthDate"))
        self.grid_1_copy.SetColLabelValue(5, _("Gender"))
        self.grid_1_copy.SetColLabelValue(6, _("Nationality"))
        self.grid_1_copy.SetColLabelValue(7, _("Address"))
        self.grid_1_copy.SetColSize(7, 120)
        self.grid_1_copy.SetColLabelValue(8, _("City"))
        self.grid_1_copy.SetColLabelValue(9, _("Region"))
        self.grid_1_copy.SetColLabelValue(10, _("Country"))
        self.grid_1_copy.SetColLabelValue(11, _("Telephone Number"))
        self.grid_1_copy.SetColSize(11, 120)
        self.grid_1_copy.SetColLabelValue(12, _("Cell Number"))
        self.grid_1_copy.SetColSize(12, 100)
        self.grid_1_copy.SetColLabelValue(13, _("Email"))
        self.grid_1_copy.SetColSize(13, 120)
        self.grid_1_copy.SetColLabelValue(14, _("Year Entered"))
        self.refreshdata()
        # end wxGlade

    def __do_layout(self):
        # begin wxGlade: ViewRecords.__do_layout
        sizer_1 = wx.BoxSizer(wx.VERTICAL)
        sizer_2_copy = wx.BoxSizer(wx.VERTICAL)
        sizer_3_copy = wx.BoxSizer(wx.HORIZONTAL)
        sizer_4_copy = wx.BoxSizer(wx.HORIZONTAL)
        sizer_2 = wx.BoxSizer(wx.VERTICAL)
        sizer_3 = wx.BoxSizer(wx.HORIZONTAL)
        sizer_4 = wx.BoxSizer(wx.HORIZONTAL)
        sizer_4.Add(self.grid_1, 1, wx.EXPAND, 0)
        self.panel_1.SetSizer(sizer_4)
        sizer_2.Add(self.panel_1, 1, wx.EXPAND, 0)
        sizer_3.Add(self.refresh, 0, 0, 0)
        sizer_2.Add(sizer_3, 0, wx.EXPAND, 0)
        self.notebook_1_pane_1.SetSizer(sizer_2)
        sizer_4_copy.Add(self.grid_1_copy, 1, wx.EXPAND, 0)
        self.panel_1_copy.SetSizer(sizer_4_copy)
        sizer_2_copy.Add(self.panel_1_copy, 1, wx.EXPAND, 0)
        sizer_3_copy.Add(self.refresh_copy, 0, 0, 0)
        sizer_2_copy.Add(sizer_3_copy, 0, wx.EXPAND, 0)
        self.notebook_1_pane_2.SetSizer(sizer_2_copy)
        self.notebook_1.AddPage(self.notebook_1_pane_1, _("Students"))
        self.notebook_1.AddPage(self.notebook_1_pane_2, _("Teachers"))
        self.notebook_1.AddPage(self.notebook_1_pane_3, _("Search"))
        sizer_1.Add(self.notebook_1, 1, wx.EXPAND, 0)
        self.SetSizer(sizer_1)
        self.Layout()