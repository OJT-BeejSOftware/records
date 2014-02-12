import datetime
import wx
import wx.grid
import re
import MySQLdb
import MySQLdb.cursors
import gettext
from ConnectDB import *

class ClassRecordsMain(wx.Frame):
    def __init__(self, *args, **kwds):
        # begin wxGlade: ClassRecords.__init__
        kwds["style"] = wx.DEFAULT_FRAME_STYLE
        wx.Frame.__init__(self, wx.GetApp().TopWindow)
        self.label_1 = wx.StaticText(self, wx.ID_ANY, _("School Year"))
        self.combo_box_1 = wx.ComboBox(self, wx.ID_ANY, choices=[_("2012-2013"), _("2013-2014"), _("2014-2015"), _("2015-2016"), _("2016-2017"), _("2017-2018"), _("2018-2019")], style=wx.CB_DROPDOWN | wx.CB_DROPDOWN | wx.CB_READONLY)
        self.load_button = wx.Button(self, wx.ID_ANY, _("Load"))
        self.notebook_1 = wx.Notebook(self, wx.ID_ANY, style=0)
        self.notebook_1_pane_1 = wx.Panel(self.notebook_1, wx.ID_ANY)
        self.notebook_2 = wx.Notebook(self.notebook_1_pane_1, wx.ID_ANY, style=0)
        self.notebook_2_pane_1 = wx.Panel(self.notebook_2, wx.ID_ANY)
        self.panel_1 = wx.Panel(self.notebook_2_pane_1, wx.ID_ANY)
        self.G1S1 = wx.grid.Grid(self.panel_1, wx.ID_ANY, size=(1, 1))
        self.notebook_2_pane_2 = wx.Panel(self.notebook_2, wx.ID_ANY)
        self.panel_2 = wx.Panel(self.notebook_2_pane_2, wx.ID_ANY)
        self.G1S2 = wx.grid.Grid(self.panel_2, wx.ID_ANY, size=(1, 1))
        self.notebook_2_pane_3 = wx.Panel(self.notebook_2, wx.ID_ANY)
        self.panel_3 = wx.Panel(self.notebook_2_pane_3, wx.ID_ANY)
        self.G1S3 = wx.grid.Grid(self.panel_3, wx.ID_ANY, size=(1, 1))
        self.notebook_2_pane_4 = wx.Panel(self.notebook_2, wx.ID_ANY)
        self.panel_4 = wx.Panel(self.notebook_2_pane_4, wx.ID_ANY)
        self.G1S4 = wx.grid.Grid(self.panel_4, wx.ID_ANY, size=(1, 1))
        self.notebook_1_pane_2 = wx.Panel(self.notebook_1, wx.ID_ANY)
        self.notebook_2_copy = wx.Notebook(self.notebook_1_pane_2, wx.ID_ANY, style=0)
        self.notebook_2_pane_1_copy = wx.Panel(self.notebook_2_copy, wx.ID_ANY)
        self.panel_1_copy = wx.Panel(self.notebook_2_pane_1_copy, wx.ID_ANY)
        self.G2S1 = wx.grid.Grid(self.panel_1_copy, wx.ID_ANY, size=(1, 1))
        self.notebook_2_pane_2_copy = wx.Panel(self.notebook_2_copy, wx.ID_ANY)
        self.panel_2_copy = wx.Panel(self.notebook_2_pane_2_copy, wx.ID_ANY)
        self.G2S2 = wx.grid.Grid(self.panel_2_copy, wx.ID_ANY, size=(1, 1))
        self.notebook_2_pane_3_copy = wx.Panel(self.notebook_2_copy, wx.ID_ANY)
        self.panel_3_copy = wx.Panel(self.notebook_2_pane_3_copy, wx.ID_ANY)
        self.G2S3 = wx.grid.Grid(self.panel_3_copy, wx.ID_ANY, size=(1, 1))
        self.notebook_2_pane_4_copy = wx.Panel(self.notebook_2_copy, wx.ID_ANY)
        self.panel_4_copy = wx.Panel(self.notebook_2_pane_4_copy, wx.ID_ANY)
        self.G2S4 = wx.grid.Grid(self.panel_4_copy, wx.ID_ANY, size=(1, 1))
        self.notebook_1_pane_3 = wx.Panel(self.notebook_1, wx.ID_ANY)
        self.notebook_2_copy_1 = wx.Notebook(self.notebook_1_pane_3, wx.ID_ANY, style=0)
        self.notebook_2_pane_1_copy_1 = wx.Panel(self.notebook_2_copy_1, wx.ID_ANY)
        self.panel_1_copy_1 = wx.Panel(self.notebook_2_pane_1_copy_1, wx.ID_ANY)
        self.G3S1 = wx.grid.Grid(self.panel_1_copy_1, wx.ID_ANY, size=(1, 1))
        self.notebook_2_pane_2_copy_1 = wx.Panel(self.notebook_2_copy_1, wx.ID_ANY)
        self.panel_2_copy_1 = wx.Panel(self.notebook_2_pane_2_copy_1, wx.ID_ANY)
        self.G3S2 = wx.grid.Grid(self.panel_2_copy_1, wx.ID_ANY, size=(1, 1))
        self.notebook_2_pane_3_copy_1 = wx.Panel(self.notebook_2_copy_1, wx.ID_ANY)
        self.panel_3_copy_1 = wx.Panel(self.notebook_2_pane_3_copy_1, wx.ID_ANY)
        self.G3S3 = wx.grid.Grid(self.panel_3_copy_1, wx.ID_ANY, size=(1, 1))
        self.notebook_2_pane_4_copy_1 = wx.Panel(self.notebook_2_copy_1, wx.ID_ANY)
        self.panel_4_copy_1 = wx.Panel(self.notebook_2_pane_4_copy_1, wx.ID_ANY)
        self.G3S4 = wx.grid.Grid(self.panel_4_copy_1, wx.ID_ANY, size=(1, 1))
        self.notebook_1_pane_4 = wx.Panel(self.notebook_1, wx.ID_ANY)
        self.notebook_2_copy_2 = wx.Notebook(self.notebook_1_pane_4, wx.ID_ANY, style=0)
        self.notebook_2_pane_1_copy_2 = wx.Panel(self.notebook_2_copy_2, wx.ID_ANY)
        self.panel_1_copy_2 = wx.Panel(self.notebook_2_pane_1_copy_2, wx.ID_ANY)
        self.G4S1 = wx.grid.Grid(self.panel_1_copy_2, wx.ID_ANY, size=(1, 1))
        self.notebook_2_pane_2_copy_2 = wx.Panel(self.notebook_2_copy_2, wx.ID_ANY)
        self.panel_2_copy_2 = wx.Panel(self.notebook_2_pane_2_copy_2, wx.ID_ANY)
        self.G4S2 = wx.grid.Grid(self.panel_2_copy_2, wx.ID_ANY, size=(1, 1))
        self.notebook_2_pane_3_copy_2 = wx.Panel(self.notebook_2_copy_2, wx.ID_ANY)
        self.panel_3_copy_2 = wx.Panel(self.notebook_2_pane_3_copy_2, wx.ID_ANY)
        self.G4S3 = wx.grid.Grid(self.panel_3_copy_2, wx.ID_ANY, size=(1, 1))
        self.notebook_2_pane_4_copy_2 = wx.Panel(self.notebook_2_copy_2, wx.ID_ANY)
        self.panel_4_copy_2 = wx.Panel(self.notebook_2_pane_4_copy_2, wx.ID_ANY)
        self.G4S4 = wx.grid.Grid(self.panel_4_copy_2, wx.ID_ANY, size=(1, 1))
        self.notebook_1_pane_5 = wx.Panel(self.notebook_1, wx.ID_ANY)
        self.notebook_2_copy_3 = wx.Notebook(self.notebook_1_pane_5, wx.ID_ANY, style=0)
        self.notebook_2_pane_1_copy_3 = wx.Panel(self.notebook_2_copy_3, wx.ID_ANY)
        self.panel_1_copy_3 = wx.Panel(self.notebook_2_pane_1_copy_3, wx.ID_ANY)
        self.G5S1 = wx.grid.Grid(self.panel_1_copy_3, wx.ID_ANY, size=(1, 1))
        self.notebook_2_pane_2_copy_3 = wx.Panel(self.notebook_2_copy_3, wx.ID_ANY)
        self.panel_2_copy_3 = wx.Panel(self.notebook_2_pane_2_copy_3, wx.ID_ANY)
        self.G5S2 = wx.grid.Grid(self.panel_2_copy_3, wx.ID_ANY, size=(1, 1))
        self.notebook_2_pane_3_copy_3 = wx.Panel(self.notebook_2_copy_3, wx.ID_ANY)
        self.panel_3_copy_3 = wx.Panel(self.notebook_2_pane_3_copy_3, wx.ID_ANY)
        self.G5S3 = wx.grid.Grid(self.panel_3_copy_3, wx.ID_ANY, size=(1, 1))
        self.notebook_2_pane_4_copy_3 = wx.Panel(self.notebook_2_copy_3, wx.ID_ANY)
        self.panel_4_copy_3 = wx.Panel(self.notebook_2_pane_4_copy_3, wx.ID_ANY)
        self.G5S4 = wx.grid.Grid(self.panel_4_copy_3, wx.ID_ANY, size=(1, 1))
        self.notebook_1_pane_6 = wx.Panel(self.notebook_1, wx.ID_ANY)
        self.notebook_2_copy_4 = wx.Notebook(self.notebook_1_pane_6, wx.ID_ANY, style=0)
        self.notebook_2_pane_1_copy_4 = wx.Panel(self.notebook_2_copy_4, wx.ID_ANY)
        self.panel_1_copy_4 = wx.Panel(self.notebook_2_pane_1_copy_4, wx.ID_ANY)
        self.G6S1 = wx.grid.Grid(self.panel_1_copy_4, wx.ID_ANY, size=(1, 1))
        self.notebook_2_pane_2_copy_4 = wx.Panel(self.notebook_2_copy_4, wx.ID_ANY)
        self.panel_2_copy_4 = wx.Panel(self.notebook_2_pane_2_copy_4, wx.ID_ANY)
        self.G6S2 = wx.grid.Grid(self.panel_2_copy_4, wx.ID_ANY, size=(1, 1))
        self.notebook_2_pane_3_copy_4 = wx.Panel(self.notebook_2_copy_4, wx.ID_ANY)
        self.panel_3_copy_4 = wx.Panel(self.notebook_2_pane_3_copy_4, wx.ID_ANY)
        self.G6S3 = wx.grid.Grid(self.panel_3_copy_4, wx.ID_ANY, size=(1, 1))
        self.notebook_2_pane_4_copy_4 = wx.Panel(self.notebook_2_copy_4, wx.ID_ANY)
        self.panel_4_copy_4 = wx.Panel(self.notebook_2_pane_4_copy_4, wx.ID_ANY)
        self.G6S4 = wx.grid.Grid(self.panel_4_copy_4, wx.ID_ANY, size=(1, 1))
        self.notebook_1_pane_7 = wx.Panel(self.notebook_1, wx.ID_ANY)
        self.notebook_2_copy_5 = wx.Notebook(self.notebook_1_pane_7, wx.ID_ANY, style=0)
        self.notebook_2_pane_1_copy_5 = wx.Panel(self.notebook_2_copy_5, wx.ID_ANY)
        self.panel_1_copy_5 = wx.Panel(self.notebook_2_pane_1_copy_5, wx.ID_ANY)
        self.Y1S1 = wx.grid.Grid(self.panel_1_copy_5, wx.ID_ANY, size=(1, 1))
        self.notebook_2_pane_2_copy_5 = wx.Panel(self.notebook_2_copy_5, wx.ID_ANY)
        self.panel_2_copy_5 = wx.Panel(self.notebook_2_pane_2_copy_5, wx.ID_ANY)
        self.Y1S2 = wx.grid.Grid(self.panel_2_copy_5, wx.ID_ANY, size=(1, 1))
        self.notebook_2_pane_3_copy_5 = wx.Panel(self.notebook_2_copy_5, wx.ID_ANY)
        self.panel_3_copy_5 = wx.Panel(self.notebook_2_pane_3_copy_5, wx.ID_ANY)
        self.Y1S3 = wx.grid.Grid(self.panel_3_copy_5, wx.ID_ANY, size=(1, 1))
        self.notebook_2_pane_4_copy_5 = wx.Panel(self.notebook_2_copy_5, wx.ID_ANY)
        self.panel_4_copy_5 = wx.Panel(self.notebook_2_pane_4_copy_5, wx.ID_ANY)
        self.Y1S4 = wx.grid.Grid(self.panel_4_copy_5, wx.ID_ANY, size=(1, 1))
        self.notebook_1_pane_8 = wx.Panel(self.notebook_1, wx.ID_ANY)
        self.notebook_2_copy_6 = wx.Notebook(self.notebook_1_pane_8, wx.ID_ANY, style=0)
        self.notebook_2_pane_1_copy_6 = wx.Panel(self.notebook_2_copy_6, wx.ID_ANY)
        self.panel_1_copy_6 = wx.Panel(self.notebook_2_pane_1_copy_6, wx.ID_ANY)
        self.Y2S1 = wx.grid.Grid(self.panel_1_copy_6, wx.ID_ANY, size=(1, 1))
        self.notebook_2_pane_2_copy_6 = wx.Panel(self.notebook_2_copy_6, wx.ID_ANY)
        self.panel_2_copy_6 = wx.Panel(self.notebook_2_pane_2_copy_6, wx.ID_ANY)
        self.Y2S2 = wx.grid.Grid(self.panel_2_copy_6, wx.ID_ANY, size=(1, 1))
        self.notebook_2_pane_3_copy_6 = wx.Panel(self.notebook_2_copy_6, wx.ID_ANY)
        self.panel_3_copy_6 = wx.Panel(self.notebook_2_pane_3_copy_6, wx.ID_ANY)
        self.Y2S3 = wx.grid.Grid(self.panel_3_copy_6, wx.ID_ANY, size=(1, 1))
        self.notebook_2_pane_4_copy_6 = wx.Panel(self.notebook_2_copy_6, wx.ID_ANY)
        self.panel_4_copy_6 = wx.Panel(self.notebook_2_pane_4_copy_6, wx.ID_ANY)
        self.Y2S4 = wx.grid.Grid(self.panel_4_copy_6, wx.ID_ANY, size=(1, 1))
        self.notebook_1_pane_8_copy = wx.Panel(self.notebook_1, wx.ID_ANY)
        self.notebook_2_copy_6_copy = wx.Notebook(self.notebook_1_pane_8_copy, wx.ID_ANY, style=0)
        self.notebook_2_pane_1_copy_6_copy = wx.Panel(self.notebook_2_copy_6_copy, wx.ID_ANY)
        self.panel_1_copy_6_copy = wx.Panel(self.notebook_2_pane_1_copy_6_copy, wx.ID_ANY)
        self.Y3S1 = wx.grid.Grid(self.panel_1_copy_6_copy, wx.ID_ANY, size=(1, 1))
        self.notebook_2_pane_2_copy_6_copy = wx.Panel(self.notebook_2_copy_6_copy, wx.ID_ANY)
        self.panel_2_copy_6_copy = wx.Panel(self.notebook_2_pane_2_copy_6_copy, wx.ID_ANY)
        self.Y3S2 = wx.grid.Grid(self.panel_2_copy_6_copy, wx.ID_ANY, size=(1, 1))
        self.notebook_2_pane_3_copy_6_copy = wx.Panel(self.notebook_2_copy_6_copy, wx.ID_ANY)
        self.panel_3_copy_6_copy = wx.Panel(self.notebook_2_pane_3_copy_6_copy, wx.ID_ANY)
        self.Y3S3 = wx.grid.Grid(self.panel_3_copy_6_copy, wx.ID_ANY, size=(1, 1))
        self.notebook_2_pane_4_copy_6_copy = wx.Panel(self.notebook_2_copy_6_copy, wx.ID_ANY)
        self.panel_4_copy_6_copy = wx.Panel(self.notebook_2_pane_4_copy_6_copy, wx.ID_ANY)
        self.Y3S4 = wx.grid.Grid(self.panel_4_copy_6_copy, wx.ID_ANY, size=(1, 1))
        self.notebook_1_pane_10 = wx.Panel(self.notebook_1, wx.ID_ANY)
        self.notebook_2_copy_7 = wx.Notebook(self.notebook_1_pane_10, wx.ID_ANY, style=0)
        self.notebook_2_pane_1_copy_7 = wx.Panel(self.notebook_2_copy_7, wx.ID_ANY)
        self.panel_1_copy_7 = wx.Panel(self.notebook_2_pane_1_copy_7, wx.ID_ANY)
        self.Y4S1 = wx.grid.Grid(self.panel_1_copy_7, wx.ID_ANY, size=(1, 1))
        self.notebook_2_pane_2_copy_7 = wx.Panel(self.notebook_2_copy_7, wx.ID_ANY)
        self.panel_2_copy_7 = wx.Panel(self.notebook_2_pane_2_copy_7, wx.ID_ANY)
        self.Y4S2 = wx.grid.Grid(self.panel_2_copy_7, wx.ID_ANY, size=(1, 1))
        self.notebook_2_pane_3_copy_7 = wx.Panel(self.notebook_2_copy_7, wx.ID_ANY)
        self.panel_3_copy_7 = wx.Panel(self.notebook_2_pane_3_copy_7, wx.ID_ANY)
        self.Y4S3 = wx.grid.Grid(self.panel_3_copy_7, wx.ID_ANY, size=(1, 1))
        self.notebook_2_pane_4_copy_7 = wx.Panel(self.notebook_2_copy_7, wx.ID_ANY)
        self.panel_4_copy_7 = wx.Panel(self.notebook_2_pane_4_copy_7, wx.ID_ANY)
        self.Y4S4 = wx.grid.Grid(self.panel_4_copy_7, wx.ID_ANY, size=(1, 1))

        self.Bind(wx.EVT_BUTTON, self.load, self.load_button)
        self.__set_properties()
        self.__do_layout()
        # end wxGlade
    def __set_properties(self):
        # begin wxGlade: ClassRecords.__set_properties
        self.SetTitle(_("Class Records"))
        self.SetSize((514, 665))
        self.label_1.SetFont(wx.Font(16, wx.DEFAULT, wx.NORMAL, wx.NORMAL, 0, "MS Shell Dlg 2"))
        self.combo_box_1.SetSelection(-1)
        self.G1S1.CreateGrid(60, 4)
        self.G1S1.SetRowLabelSize(30)
        self.G1S1.SetColLabelValue(0, _("ID Number"))
        self.G1S1.SetColLabelValue(1, _("Last Name"))
        self.G1S1.SetColSize(1, 100)
        self.G1S1.SetColLabelValue(2, _("First Name"))
        self.G1S1.SetColSize(2, 140)
        self.G1S1.SetColLabelValue(3, _("Middle Name"))
        self.G1S1.SetColSize(3, 100)
        self.G1S2.CreateGrid(60, 4)
        self.G1S2.SetRowLabelSize(30)
        self.G1S2.SetColLabelValue(0, _("ID Number"))
        self.G1S2.SetColLabelValue(1, _("Last Name"))
        self.G1S2.SetColSize(1, 100)
        self.G1S2.SetColLabelValue(2, _("First Name"))
        self.G1S2.SetColSize(2, 140)
        self.G1S2.SetColLabelValue(3, _("Middle Name"))
        self.G1S2.SetColSize(3, 100)
        self.G1S3.CreateGrid(60, 4)
        self.G1S3.SetRowLabelSize(30)
        self.G1S3.SetColLabelValue(0, _("ID Number"))
        self.G1S3.SetColLabelValue(1, _("Last Name"))
        self.G1S3.SetColSize(1, 100)
        self.G1S3.SetColLabelValue(2, _("First Name"))
        self.G1S3.SetColSize(2, 140)
        self.G1S3.SetColLabelValue(3, _("Middle Name"))
        self.G1S3.SetColSize(3, 100)
        self.G1S4.CreateGrid(60, 4)
        self.G1S4.SetRowLabelSize(30)
        self.G1S4.SetColLabelValue(0, _("ID Number"))
        self.G1S4.SetColLabelValue(1, _("Last Name"))
        self.G1S4.SetColSize(1, 100)
        self.G1S4.SetColLabelValue(2, _("First Name"))
        self.G1S4.SetColSize(2, 140)
        self.G1S4.SetColLabelValue(3, _("Middle Name"))
        self.G1S4.SetColSize(3, 100)
        self.G2S1.CreateGrid(60, 4)
        self.G2S1.SetRowLabelSize(30)
        self.G2S1.SetColLabelValue(0, _("ID Number"))
        self.G2S1.SetColLabelValue(1, _("Last Name"))
        self.G2S1.SetColSize(1, 100)
        self.G2S1.SetColLabelValue(2, _("First Name"))
        self.G2S1.SetColSize(2, 140)
        self.G2S1.SetColLabelValue(3, _("Middle Name"))
        self.G2S1.SetColSize(3, 100)
        self.G2S2.CreateGrid(60, 4)
        self.G2S2.SetRowLabelSize(30)
        self.G2S2.SetColLabelValue(0, _("ID Number"))
        self.G2S2.SetColLabelValue(1, _("Last Name"))
        self.G2S2.SetColSize(1, 100)
        self.G2S2.SetColLabelValue(2, _("First Name"))
        self.G2S2.SetColSize(2, 140)
        self.G2S2.SetColLabelValue(3, _("Middle Name"))
        self.G2S2.SetColSize(3, 100)
        self.G2S3.CreateGrid(60, 4)
        self.G2S3.SetRowLabelSize(30)
        self.G2S3.SetColLabelValue(0, _("ID Number"))
        self.G2S3.SetColLabelValue(1, _("Last Name"))
        self.G2S3.SetColSize(1, 100)
        self.G2S3.SetColLabelValue(2, _("First Name"))
        self.G2S3.SetColSize(2, 140)
        self.G2S3.SetColLabelValue(3, _("Middle Name"))
        self.G2S3.SetColSize(3, 100)
        self.G2S4.CreateGrid(60, 4)
        self.G2S4.SetRowLabelSize(30)
        self.G2S4.SetColLabelValue(0, _("ID Number"))
        self.G2S4.SetColLabelValue(1, _("Last Name"))
        self.G2S4.SetColSize(1, 100)
        self.G2S4.SetColLabelValue(2, _("First Name"))
        self.G2S4.SetColSize(2, 140)
        self.G2S4.SetColLabelValue(3, _("Middle Name"))
        self.G2S4.SetColSize(3, 100)
        self.G3S1.CreateGrid(60, 4)
        self.G3S1.SetRowLabelSize(30)
        self.G3S1.SetColLabelValue(0, _("ID Number"))
        self.G3S1.SetColLabelValue(1, _("Last Name"))
        self.G3S1.SetColSize(1, 100)
        self.G3S1.SetColLabelValue(2, _("First Name"))
        self.G3S1.SetColSize(2, 140)
        self.G3S1.SetColLabelValue(3, _("Middle Name"))
        self.G3S1.SetColSize(3, 100)
        self.G3S2.CreateGrid(60, 4)
        self.G3S2.SetRowLabelSize(30)
        self.G3S2.SetColLabelValue(0, _("ID Number"))
        self.G3S2.SetColLabelValue(1, _("Last Name"))
        self.G3S2.SetColSize(1, 100)
        self.G3S2.SetColLabelValue(2, _("First Name"))
        self.G3S2.SetColSize(2, 140)
        self.G3S2.SetColLabelValue(3, _("Middle Name"))
        self.G3S2.SetColSize(3, 100)
        self.G3S3.CreateGrid(60, 4)
        self.G3S3.SetRowLabelSize(30)
        self.G3S3.SetColLabelValue(0, _("ID Number"))
        self.G3S3.SetColLabelValue(1, _("Last Name"))
        self.G3S3.SetColSize(1, 100)
        self.G3S3.SetColLabelValue(2, _("First Name"))
        self.G3S3.SetColSize(2, 140)
        self.G3S3.SetColLabelValue(3, _("Middle Name"))
        self.G3S3.SetColSize(3, 100)
        self.G3S4.CreateGrid(60, 4)
        self.G3S4.SetRowLabelSize(30)
        self.G3S4.SetColLabelValue(0, _("ID Number"))
        self.G3S4.SetColLabelValue(1, _("Last Name"))
        self.G3S4.SetColSize(1, 100)
        self.G3S4.SetColLabelValue(2, _("First Name"))
        self.G3S4.SetColSize(2, 140)
        self.G3S4.SetColLabelValue(3, _("Middle Name"))
        self.G3S4.SetColSize(3, 100)
        self.G4S1.CreateGrid(60, 4)
        self.G4S1.SetRowLabelSize(30)
        self.G4S1.SetColLabelValue(0, _("ID Number"))
        self.G4S1.SetColLabelValue(1, _("Last Name"))
        self.G4S1.SetColSize(1, 100)
        self.G4S1.SetColLabelValue(2, _("First Name"))
        self.G4S1.SetColSize(2, 140)
        self.G4S1.SetColLabelValue(3, _("Middle Name"))
        self.G4S1.SetColSize(3, 100)
        self.G4S2.CreateGrid(60, 4)
        self.G4S2.SetRowLabelSize(30)
        self.G4S2.SetColLabelValue(0, _("ID Number"))
        self.G4S2.SetColLabelValue(1, _("Last Name"))
        self.G4S2.SetColSize(1, 100)
        self.G4S2.SetColLabelValue(2, _("First Name"))
        self.G4S2.SetColSize(2, 140)
        self.G4S2.SetColLabelValue(3, _("Middle Name"))
        self.G4S2.SetColSize(3, 100)
        self.G4S3.CreateGrid(60, 4)
        self.G4S3.SetRowLabelSize(30)
        self.G4S3.SetColLabelValue(0, _("ID Number"))
        self.G4S3.SetColLabelValue(1, _("Last Name"))
        self.G4S3.SetColSize(1, 100)
        self.G4S3.SetColLabelValue(2, _("First Name"))
        self.G4S3.SetColSize(2, 140)
        self.G4S3.SetColLabelValue(3, _("Middle Name"))
        self.G4S3.SetColSize(3, 100)
        self.G4S4.CreateGrid(60, 4)
        self.G4S4.SetRowLabelSize(30)
        self.G4S4.SetColLabelValue(0, _("ID Number"))
        self.G4S4.SetColLabelValue(1, _("Last Name"))
        self.G4S4.SetColSize(1, 100)
        self.G4S4.SetColLabelValue(2, _("First Name"))
        self.G4S4.SetColSize(2, 140)
        self.G4S4.SetColLabelValue(3, _("Middle Name"))
        self.G4S4.SetColSize(3, 100)
        self.G5S1.CreateGrid(60, 4)
        self.G5S1.SetRowLabelSize(30)
        self.G5S1.SetColLabelValue(0, _("ID Number"))
        self.G5S1.SetColLabelValue(1, _("Last Name"))
        self.G5S1.SetColSize(1, 100)
        self.G5S1.SetColLabelValue(2, _("First Name"))
        self.G5S1.SetColSize(2, 140)
        self.G5S1.SetColLabelValue(3, _("Middle Name"))
        self.G5S1.SetColSize(3, 100)
        self.G5S2.CreateGrid(60, 4)
        self.G5S2.SetRowLabelSize(30)
        self.G5S2.SetColLabelValue(0, _("ID Number"))
        self.G5S2.SetColLabelValue(1, _("Last Name"))
        self.G5S2.SetColSize(1, 100)
        self.G5S2.SetColLabelValue(2, _("First Name"))
        self.G5S2.SetColSize(2, 140)
        self.G5S2.SetColLabelValue(3, _("Middle Name"))
        self.G5S2.SetColSize(3, 100)
        self.G5S3.CreateGrid(60, 4)
        self.G5S3.SetRowLabelSize(30)
        self.G5S3.SetColLabelValue(0, _("ID Number"))
        self.G5S3.SetColLabelValue(1, _("Last Name"))
        self.G5S3.SetColSize(1, 100)
        self.G5S3.SetColLabelValue(2, _("First Name"))
        self.G5S3.SetColSize(2, 140)
        self.G5S3.SetColLabelValue(3, _("Middle Name"))
        self.G5S3.SetColSize(3, 100)
        self.G5S4.CreateGrid(60, 4)
        self.G5S4.SetRowLabelSize(30)
        self.G5S4.SetColLabelValue(0, _("ID Number"))
        self.G5S4.SetColLabelValue(1, _("Last Name"))
        self.G5S4.SetColSize(1, 100)
        self.G5S4.SetColLabelValue(2, _("First Name"))
        self.G5S4.SetColSize(2, 140)
        self.G5S4.SetColLabelValue(3, _("Middle Name"))
        self.G5S4.SetColSize(3, 100)
        self.G6S1.CreateGrid(60, 4)
        self.G6S1.SetRowLabelSize(30)
        self.G6S1.SetColLabelValue(0, _("ID Number"))
        self.G6S1.SetColLabelValue(1, _("Last Name"))
        self.G6S1.SetColSize(1, 100)
        self.G6S1.SetColLabelValue(2, _("First Name"))
        self.G6S1.SetColSize(2, 140)
        self.G6S1.SetColLabelValue(3, _("Middle Name"))
        self.G6S1.SetColSize(3, 100)
        self.G6S2.CreateGrid(60, 4)
        self.G6S2.SetRowLabelSize(30)
        self.G6S2.SetColLabelValue(0, _("ID Number"))
        self.G6S2.SetColLabelValue(1, _("Last Name"))
        self.G6S2.SetColSize(1, 100)
        self.G6S2.SetColLabelValue(2, _("First Name"))
        self.G6S2.SetColSize(2, 140)
        self.G6S2.SetColLabelValue(3, _("Middle Name"))
        self.G6S2.SetColSize(3, 100)
        self.G6S3.CreateGrid(60, 4)
        self.G6S3.SetRowLabelSize(30)
        self.G6S3.SetColLabelValue(0, _("ID Number"))
        self.G6S3.SetColLabelValue(1, _("Last Name"))
        self.G6S3.SetColSize(1, 100)
        self.G6S3.SetColLabelValue(2, _("First Name"))
        self.G6S3.SetColSize(2, 140)
        self.G6S3.SetColLabelValue(3, _("Middle Name"))
        self.G6S3.SetColSize(3, 100)
        self.G6S4.CreateGrid(60, 4)
        self.G6S4.SetRowLabelSize(30)
        self.G6S4.SetColLabelValue(0, _("ID Number"))
        self.G6S4.SetColLabelValue(1, _("Last Name"))
        self.G6S4.SetColSize(1, 100)
        self.G6S4.SetColLabelValue(2, _("First Name"))
        self.G6S4.SetColSize(2, 140)
        self.G6S4.SetColLabelValue(3, _("Middle Name"))
        self.G6S4.SetColSize(3, 100)
        self.Y1S1.CreateGrid(60, 4)
        self.Y1S1.SetRowLabelSize(30)
        self.Y1S1.SetColLabelValue(0, _("ID Number"))
        self.Y1S1.SetColLabelValue(1, _("Last Name"))
        self.Y1S1.SetColSize(1, 100)
        self.Y1S1.SetColLabelValue(2, _("First Name"))
        self.Y1S1.SetColSize(2, 140)
        self.Y1S1.SetColLabelValue(3, _("Middle Name"))
        self.Y1S1.SetColSize(3, 100)
        self.Y1S2.CreateGrid(60, 4)
        self.Y1S2.SetRowLabelSize(30)
        self.Y1S2.SetColLabelValue(0, _("ID Number"))
        self.Y1S2.SetColLabelValue(1, _("Last Name"))
        self.Y1S2.SetColSize(1, 100)
        self.Y1S2.SetColLabelValue(2, _("First Name"))
        self.Y1S2.SetColSize(2, 140)
        self.Y1S2.SetColLabelValue(3, _("Middle Name"))
        self.Y1S2.SetColSize(3, 100)
        self.Y1S3.CreateGrid(60, 4)
        self.Y1S3.SetRowLabelSize(30)
        self.Y1S3.SetColLabelValue(0, _("ID Number"))
        self.Y1S3.SetColLabelValue(1, _("Last Name"))
        self.Y1S3.SetColSize(1, 100)
        self.Y1S3.SetColLabelValue(2, _("First Name"))
        self.Y1S3.SetColSize(2, 140)
        self.Y1S3.SetColLabelValue(3, _("Middle Name"))
        self.Y1S3.SetColSize(3, 100)
        self.Y1S4.CreateGrid(60, 4)
        self.Y1S4.SetRowLabelSize(30)
        self.Y1S4.SetColLabelValue(0, _("ID Number"))
        self.Y1S4.SetColLabelValue(1, _("Last Name"))
        self.Y1S4.SetColSize(1, 100)
        self.Y1S4.SetColLabelValue(2, _("First Name"))
        self.Y1S4.SetColSize(2, 140)
        self.Y1S4.SetColLabelValue(3, _("Middle Name"))
        self.Y1S4.SetColSize(3, 100)
        self.Y2S1.CreateGrid(60, 4)
        self.Y2S1.SetRowLabelSize(30)
        self.Y2S1.SetColLabelValue(0, _("ID Number"))
        self.Y2S1.SetColLabelValue(1, _("Last Name"))
        self.Y2S1.SetColSize(1, 100)
        self.Y2S1.SetColLabelValue(2, _("First Name"))
        self.Y2S1.SetColSize(2, 140)
        self.Y2S1.SetColLabelValue(3, _("Middle Name"))
        self.Y2S1.SetColSize(3, 100)
        self.Y2S2.CreateGrid(60, 4)
        self.Y2S2.SetRowLabelSize(30)
        self.Y2S2.SetColLabelValue(0, _("ID Number"))
        self.Y2S2.SetColLabelValue(1, _("Last Name"))
        self.Y2S2.SetColSize(1, 100)
        self.Y2S2.SetColLabelValue(2, _("First Name"))
        self.Y2S2.SetColSize(2, 140)
        self.Y2S2.SetColLabelValue(3, _("Middle Name"))
        self.Y2S2.SetColSize(3, 100)
        self.Y2S3.CreateGrid(60, 4)
        self.Y2S3.SetRowLabelSize(30)
        self.Y2S3.SetColLabelValue(0, _("ID Number"))
        self.Y2S3.SetColLabelValue(1, _("Last Name"))
        self.Y2S3.SetColSize(1, 100)
        self.Y2S3.SetColLabelValue(2, _("First Name"))
        self.Y2S3.SetColSize(2, 140)
        self.Y2S3.SetColLabelValue(3, _("Middle Name"))
        self.Y2S3.SetColSize(3, 100)
        self.Y2S4.CreateGrid(60, 4)
        self.Y2S4.SetRowLabelSize(30)
        self.Y2S4.SetColLabelValue(0, _("ID Number"))
        self.Y2S4.SetColLabelValue(1, _("Last Name"))
        self.Y2S4.SetColSize(1, 100)
        self.Y2S4.SetColLabelValue(2, _("First Name"))
        self.Y2S4.SetColSize(2, 140)
        self.Y2S4.SetColLabelValue(3, _("Middle Name"))
        self.Y2S4.SetColSize(3, 100)
        self.Y3S1.CreateGrid(60, 4)
        self.Y3S1.SetRowLabelSize(30)
        self.Y3S1.SetColLabelValue(0, _("ID Number"))
        self.Y3S1.SetColLabelValue(1, _("Last Name"))
        self.Y3S1.SetColSize(1, 100)
        self.Y3S1.SetColLabelValue(2, _("First Name"))
        self.Y3S1.SetColSize(2, 140)
        self.Y3S1.SetColLabelValue(3, _("Middle Name"))
        self.Y3S1.SetColSize(3, 100)
        self.Y3S2.CreateGrid(60, 4)
        self.Y3S2.SetRowLabelSize(30)
        self.Y3S2.SetColLabelValue(0, _("ID Number"))
        self.Y3S2.SetColLabelValue(1, _("Last Name"))
        self.Y3S2.SetColSize(1, 100)
        self.Y3S2.SetColLabelValue(2, _("First Name"))
        self.Y3S2.SetColSize(2, 140)
        self.Y3S2.SetColLabelValue(3, _("Middle Name"))
        self.Y3S2.SetColSize(3, 100)
        self.Y3S3.CreateGrid(60, 4)
        self.Y3S3.SetRowLabelSize(30)
        self.Y3S3.SetColLabelValue(0, _("ID Number"))
        self.Y3S3.SetColLabelValue(1, _("Last Name"))
        self.Y3S3.SetColSize(1, 100)
        self.Y3S3.SetColLabelValue(2, _("First Name"))
        self.Y3S3.SetColSize(2, 140)
        self.Y3S3.SetColLabelValue(3, _("Middle Name"))
        self.Y3S3.SetColSize(3, 100)
        self.Y3S4.CreateGrid(60, 4)
        self.Y3S4.SetRowLabelSize(30)
        self.Y3S4.SetColLabelValue(0, _("ID Number"))
        self.Y3S4.SetColLabelValue(1, _("Last Name"))
        self.Y3S4.SetColSize(1, 100)
        self.Y3S4.SetColLabelValue(2, _("First Name"))
        self.Y3S4.SetColSize(2, 140)
        self.Y3S4.SetColLabelValue(3, _("Middle Name"))
        self.Y3S4.SetColSize(3, 100)
        self.Y4S1.CreateGrid(60, 4)
        self.Y4S1.SetRowLabelSize(30)
        self.Y4S1.SetColLabelValue(0, _("ID Number"))
        self.Y4S1.SetColLabelValue(1, _("Last Name"))
        self.Y4S1.SetColSize(1, 100)
        self.Y4S1.SetColLabelValue(2, _("First Name"))
        self.Y4S1.SetColSize(2, 140)
        self.Y4S1.SetColLabelValue(3, _("Middle Name"))
        self.Y4S1.SetColSize(3, 100)
        self.Y4S2.CreateGrid(60, 4)
        self.Y4S2.SetRowLabelSize(30)
        self.Y4S2.SetColLabelValue(0, _("ID Number"))
        self.Y4S2.SetColLabelValue(1, _("Last Name"))
        self.Y4S2.SetColSize(1, 100)
        self.Y4S2.SetColLabelValue(2, _("First Name"))
        self.Y4S2.SetColSize(2, 140)
        self.Y4S2.SetColLabelValue(3, _("Middle Name"))
        self.Y4S2.SetColSize(3, 100)
        self.Y4S3.CreateGrid(60, 4)
        self.Y4S3.SetRowLabelSize(30)
        self.Y4S3.SetColLabelValue(0, _("ID Number"))
        self.Y4S3.SetColLabelValue(1, _("Last Name"))
        self.Y4S3.SetColSize(1, 100)
        self.Y4S3.SetColLabelValue(2, _("First Name"))
        self.Y4S3.SetColSize(2, 140)
        self.Y4S3.SetColLabelValue(3, _("Middle Name"))
        self.Y4S3.SetColSize(3, 100)
        self.Y4S4.CreateGrid(60, 4)
        self.Y4S4.SetRowLabelSize(30)
        self.Y4S4.SetColLabelValue(0, _("ID Number"))
        self.Y4S4.SetColLabelValue(1, _("Last Name"))
        self.Y4S4.SetColSize(1, 100)
        self.Y4S4.SetColLabelValue(2, _("First Name"))
        self.Y4S4.SetColSize(2, 140)
        self.Y4S4.SetColLabelValue(3, _("Middle Name"))
        self.Y4S4.SetColSize(3, 100)
        # end wxGlade

    def __do_layout(self):
        # begin wxGlade: ClassRecords.__do_layout
        sizer_1 = wx.BoxSizer(wx.VERTICAL)
        sizer_3_copy_7 = wx.BoxSizer(wx.HORIZONTAL)
        sizer_7_copy_7 = wx.BoxSizer(wx.HORIZONTAL)
        sizer_8_copy_2_copy_7 = wx.BoxSizer(wx.HORIZONTAL)
        sizer_6_copy_7 = wx.BoxSizer(wx.HORIZONTAL)
        sizer_8_copy_1_copy_7 = wx.BoxSizer(wx.HORIZONTAL)
        sizer_5_copy_7 = wx.BoxSizer(wx.HORIZONTAL)
        sizer_8_copy_copy_7 = wx.BoxSizer(wx.HORIZONTAL)
        sizer_4_copy_7 = wx.BoxSizer(wx.HORIZONTAL)
        sizer_8_copy_10 = wx.BoxSizer(wx.HORIZONTAL)
        sizer_3_copy_6_copy = wx.BoxSizer(wx.HORIZONTAL)
        sizer_7_copy_6_copy = wx.BoxSizer(wx.HORIZONTAL)
        sizer_8_copy_2_copy_6_copy = wx.BoxSizer(wx.HORIZONTAL)
        sizer_6_copy_6_copy = wx.BoxSizer(wx.HORIZONTAL)
        sizer_8_copy_1_copy_6_copy = wx.BoxSizer(wx.HORIZONTAL)
        sizer_5_copy_6_copy = wx.BoxSizer(wx.HORIZONTAL)
        sizer_8_copy_copy_6_copy = wx.BoxSizer(wx.HORIZONTAL)
        sizer_4_copy_6_copy = wx.BoxSizer(wx.HORIZONTAL)
        sizer_8_copy_9_copy = wx.BoxSizer(wx.HORIZONTAL)
        sizer_3_copy_6 = wx.BoxSizer(wx.HORIZONTAL)
        sizer_7_copy_6 = wx.BoxSizer(wx.HORIZONTAL)
        sizer_8_copy_2_copy_6 = wx.BoxSizer(wx.HORIZONTAL)
        sizer_6_copy_6 = wx.BoxSizer(wx.HORIZONTAL)
        sizer_8_copy_1_copy_6 = wx.BoxSizer(wx.HORIZONTAL)
        sizer_5_copy_6 = wx.BoxSizer(wx.HORIZONTAL)
        sizer_8_copy_copy_6 = wx.BoxSizer(wx.HORIZONTAL)
        sizer_4_copy_6 = wx.BoxSizer(wx.HORIZONTAL)
        sizer_8_copy_9 = wx.BoxSizer(wx.HORIZONTAL)
        sizer_3_copy_5 = wx.BoxSizer(wx.HORIZONTAL)
        sizer_7_copy_5 = wx.BoxSizer(wx.HORIZONTAL)
        sizer_8_copy_2_copy_5 = wx.BoxSizer(wx.HORIZONTAL)
        sizer_6_copy_5 = wx.BoxSizer(wx.HORIZONTAL)
        sizer_8_copy_1_copy_5 = wx.BoxSizer(wx.HORIZONTAL)
        sizer_5_copy_5 = wx.BoxSizer(wx.HORIZONTAL)
        sizer_8_copy_copy_5 = wx.BoxSizer(wx.HORIZONTAL)
        sizer_4_copy_5 = wx.BoxSizer(wx.HORIZONTAL)
        sizer_8_copy_8 = wx.BoxSizer(wx.HORIZONTAL)
        sizer_3_copy_4 = wx.BoxSizer(wx.HORIZONTAL)
        sizer_7_copy_4 = wx.BoxSizer(wx.HORIZONTAL)
        sizer_8_copy_2_copy_4 = wx.BoxSizer(wx.HORIZONTAL)
        sizer_6_copy_4 = wx.BoxSizer(wx.HORIZONTAL)
        sizer_8_copy_1_copy_4 = wx.BoxSizer(wx.HORIZONTAL)
        sizer_5_copy_4 = wx.BoxSizer(wx.HORIZONTAL)
        sizer_8_copy_copy_4 = wx.BoxSizer(wx.HORIZONTAL)
        sizer_4_copy_4 = wx.BoxSizer(wx.HORIZONTAL)
        sizer_8_copy_7 = wx.BoxSizer(wx.HORIZONTAL)
        sizer_3_copy_3 = wx.BoxSizer(wx.HORIZONTAL)
        sizer_7_copy_3 = wx.BoxSizer(wx.HORIZONTAL)
        sizer_8_copy_2_copy_3 = wx.BoxSizer(wx.HORIZONTAL)
        sizer_6_copy_3 = wx.BoxSizer(wx.HORIZONTAL)
        sizer_8_copy_1_copy_3 = wx.BoxSizer(wx.HORIZONTAL)
        sizer_5_copy_3 = wx.BoxSizer(wx.HORIZONTAL)
        sizer_8_copy_copy_3 = wx.BoxSizer(wx.HORIZONTAL)
        sizer_4_copy_3 = wx.BoxSizer(wx.HORIZONTAL)
        sizer_8_copy_6 = wx.BoxSizer(wx.HORIZONTAL)
        sizer_3_copy_2 = wx.BoxSizer(wx.HORIZONTAL)
        sizer_7_copy_2 = wx.BoxSizer(wx.HORIZONTAL)
        sizer_8_copy_2_copy_2 = wx.BoxSizer(wx.HORIZONTAL)
        sizer_6_copy_2 = wx.BoxSizer(wx.HORIZONTAL)
        sizer_8_copy_1_copy_2 = wx.BoxSizer(wx.HORIZONTAL)
        sizer_5_copy_2 = wx.BoxSizer(wx.HORIZONTAL)
        sizer_8_copy_copy_2 = wx.BoxSizer(wx.HORIZONTAL)
        sizer_4_copy_2 = wx.BoxSizer(wx.HORIZONTAL)
        sizer_8_copy_5 = wx.BoxSizer(wx.HORIZONTAL)
        sizer_3_copy_1 = wx.BoxSizer(wx.HORIZONTAL)
        sizer_7_copy_1 = wx.BoxSizer(wx.HORIZONTAL)
        sizer_8_copy_2_copy_1 = wx.BoxSizer(wx.HORIZONTAL)
        sizer_6_copy_1 = wx.BoxSizer(wx.HORIZONTAL)
        sizer_8_copy_1_copy_1 = wx.BoxSizer(wx.HORIZONTAL)
        sizer_5_copy_1 = wx.BoxSizer(wx.HORIZONTAL)
        sizer_8_copy_copy_1 = wx.BoxSizer(wx.HORIZONTAL)
        sizer_4_copy_1 = wx.BoxSizer(wx.HORIZONTAL)
        sizer_8_copy_4 = wx.BoxSizer(wx.HORIZONTAL)
        sizer_3_copy = wx.BoxSizer(wx.HORIZONTAL)
        sizer_7_copy = wx.BoxSizer(wx.HORIZONTAL)
        sizer_8_copy_2_copy = wx.BoxSizer(wx.HORIZONTAL)
        sizer_6_copy = wx.BoxSizer(wx.HORIZONTAL)
        sizer_8_copy_1_copy = wx.BoxSizer(wx.HORIZONTAL)
        sizer_5_copy = wx.BoxSizer(wx.HORIZONTAL)
        sizer_8_copy_copy = wx.BoxSizer(wx.HORIZONTAL)
        sizer_4_copy = wx.BoxSizer(wx.HORIZONTAL)
        sizer_8_copy_3 = wx.BoxSizer(wx.HORIZONTAL)
        sizer_3 = wx.BoxSizer(wx.HORIZONTAL)
        sizer_7 = wx.BoxSizer(wx.HORIZONTAL)
        sizer_8_copy_2 = wx.BoxSizer(wx.HORIZONTAL)
        sizer_6 = wx.BoxSizer(wx.HORIZONTAL)
        sizer_8_copy_1 = wx.BoxSizer(wx.HORIZONTAL)
        sizer_5 = wx.BoxSizer(wx.HORIZONTAL)
        sizer_8_copy = wx.BoxSizer(wx.HORIZONTAL)
        sizer_4 = wx.BoxSizer(wx.HORIZONTAL)
        sizer_8 = wx.BoxSizer(wx.HORIZONTAL)
        sizer_2 = wx.BoxSizer(wx.HORIZONTAL)
        sizer_2.Add(self.label_1, 0, 0, 0)
        sizer_2.Add(self.combo_box_1, 0, 0, 0)
        sizer_2.Add(self.load_button, 0, 0, 0)
        sizer_1.Add(sizer_2, 0, wx.EXPAND, 0)
        sizer_8.Add(self.G1S1, 1, wx.EXPAND, 0)
        self.panel_1.SetSizer(sizer_8)
        sizer_4.Add(self.panel_1, 1, wx.EXPAND, 0)
        self.notebook_2_pane_1.SetSizer(sizer_4)
        sizer_8_copy.Add(self.G1S2, 1, wx.EXPAND, 0)
        self.panel_2.SetSizer(sizer_8_copy)
        sizer_5.Add(self.panel_2, 1, wx.EXPAND, 0)
        self.notebook_2_pane_2.SetSizer(sizer_5)
        sizer_8_copy_1.Add(self.G1S3, 1, wx.EXPAND, 0)
        self.panel_3.SetSizer(sizer_8_copy_1)
        sizer_6.Add(self.panel_3, 1, wx.EXPAND, 0)
        self.notebook_2_pane_3.SetSizer(sizer_6)
        sizer_8_copy_2.Add(self.G1S4, 1, wx.EXPAND, 0)
        self.panel_4.SetSizer(sizer_8_copy_2)
        sizer_7.Add(self.panel_4, 1, wx.EXPAND, 0)
        self.notebook_2_pane_4.SetSizer(sizer_7)
        self.notebook_2.AddPage(self.notebook_2_pane_1, _("Section1"))
        self.notebook_2.AddPage(self.notebook_2_pane_2, _("Section2"))
        self.notebook_2.AddPage(self.notebook_2_pane_3, _("Section3"))
        self.notebook_2.AddPage(self.notebook_2_pane_4, _("Section4"))
        sizer_3.Add(self.notebook_2, 1, wx.EXPAND, 0)
        self.notebook_1_pane_1.SetSizer(sizer_3)
        sizer_8_copy_3.Add(self.G2S1, 1, wx.EXPAND, 0)
        self.panel_1_copy.SetSizer(sizer_8_copy_3)
        sizer_4_copy.Add(self.panel_1_copy, 1, wx.EXPAND, 0)
        self.notebook_2_pane_1_copy.SetSizer(sizer_4_copy)
        sizer_8_copy_copy.Add(self.G2S2, 1, wx.EXPAND, 0)
        self.panel_2_copy.SetSizer(sizer_8_copy_copy)
        sizer_5_copy.Add(self.panel_2_copy, 1, wx.EXPAND, 0)
        self.notebook_2_pane_2_copy.SetSizer(sizer_5_copy)
        sizer_8_copy_1_copy.Add(self.G2S3, 1, wx.EXPAND, 0)
        self.panel_3_copy.SetSizer(sizer_8_copy_1_copy)
        sizer_6_copy.Add(self.panel_3_copy, 1, wx.EXPAND, 0)
        self.notebook_2_pane_3_copy.SetSizer(sizer_6_copy)
        sizer_8_copy_2_copy.Add(self.G2S4, 1, wx.EXPAND, 0)
        self.panel_4_copy.SetSizer(sizer_8_copy_2_copy)
        sizer_7_copy.Add(self.panel_4_copy, 1, wx.EXPAND, 0)
        self.notebook_2_pane_4_copy.SetSizer(sizer_7_copy)
        self.notebook_2_copy.AddPage(self.notebook_2_pane_1_copy, _("Section1"))
        self.notebook_2_copy.AddPage(self.notebook_2_pane_2_copy, _("Section2"))
        self.notebook_2_copy.AddPage(self.notebook_2_pane_3_copy, _("Section3"))
        self.notebook_2_copy.AddPage(self.notebook_2_pane_4_copy, _("Section4"))
        sizer_3_copy.Add(self.notebook_2_copy, 1, wx.EXPAND, 0)
        self.notebook_1_pane_2.SetSizer(sizer_3_copy)
        sizer_8_copy_4.Add(self.G3S1, 1, wx.EXPAND, 0)
        self.panel_1_copy_1.SetSizer(sizer_8_copy_4)
        sizer_4_copy_1.Add(self.panel_1_copy_1, 1, wx.EXPAND, 0)
        self.notebook_2_pane_1_copy_1.SetSizer(sizer_4_copy_1)
        sizer_8_copy_copy_1.Add(self.G3S2, 1, wx.EXPAND, 0)
        self.panel_2_copy_1.SetSizer(sizer_8_copy_copy_1)
        sizer_5_copy_1.Add(self.panel_2_copy_1, 1, wx.EXPAND, 0)
        self.notebook_2_pane_2_copy_1.SetSizer(sizer_5_copy_1)
        sizer_8_copy_1_copy_1.Add(self.G3S3, 1, wx.EXPAND, 0)
        self.panel_3_copy_1.SetSizer(sizer_8_copy_1_copy_1)
        sizer_6_copy_1.Add(self.panel_3_copy_1, 1, wx.EXPAND, 0)
        self.notebook_2_pane_3_copy_1.SetSizer(sizer_6_copy_1)
        sizer_8_copy_2_copy_1.Add(self.G3S4, 1, wx.EXPAND, 0)
        self.panel_4_copy_1.SetSizer(sizer_8_copy_2_copy_1)
        sizer_7_copy_1.Add(self.panel_4_copy_1, 1, wx.EXPAND, 0)
        self.notebook_2_pane_4_copy_1.SetSizer(sizer_7_copy_1)
        self.notebook_2_copy_1.AddPage(self.notebook_2_pane_1_copy_1, _("Section1"))
        self.notebook_2_copy_1.AddPage(self.notebook_2_pane_2_copy_1, _("Section2"))
        self.notebook_2_copy_1.AddPage(self.notebook_2_pane_3_copy_1, _("Section3"))
        self.notebook_2_copy_1.AddPage(self.notebook_2_pane_4_copy_1, _("Section4"))
        sizer_3_copy_1.Add(self.notebook_2_copy_1, 1, wx.EXPAND, 0)
        self.notebook_1_pane_3.SetSizer(sizer_3_copy_1)
        sizer_8_copy_5.Add(self.G4S1, 1, wx.EXPAND, 0)
        self.panel_1_copy_2.SetSizer(sizer_8_copy_5)
        sizer_4_copy_2.Add(self.panel_1_copy_2, 1, wx.EXPAND, 0)
        self.notebook_2_pane_1_copy_2.SetSizer(sizer_4_copy_2)
        sizer_8_copy_copy_2.Add(self.G4S2, 1, wx.EXPAND, 0)
        self.panel_2_copy_2.SetSizer(sizer_8_copy_copy_2)
        sizer_5_copy_2.Add(self.panel_2_copy_2, 1, wx.EXPAND, 0)
        self.notebook_2_pane_2_copy_2.SetSizer(sizer_5_copy_2)
        sizer_8_copy_1_copy_2.Add(self.G4S3, 1, wx.EXPAND, 0)
        self.panel_3_copy_2.SetSizer(sizer_8_copy_1_copy_2)
        sizer_6_copy_2.Add(self.panel_3_copy_2, 1, wx.EXPAND, 0)
        self.notebook_2_pane_3_copy_2.SetSizer(sizer_6_copy_2)
        sizer_8_copy_2_copy_2.Add(self.G4S4, 1, wx.EXPAND, 0)
        self.panel_4_copy_2.SetSizer(sizer_8_copy_2_copy_2)
        sizer_7_copy_2.Add(self.panel_4_copy_2, 1, wx.EXPAND, 0)
        self.notebook_2_pane_4_copy_2.SetSizer(sizer_7_copy_2)
        self.notebook_2_copy_2.AddPage(self.notebook_2_pane_1_copy_2, _("Section1"))
        self.notebook_2_copy_2.AddPage(self.notebook_2_pane_2_copy_2, _("Section2"))
        self.notebook_2_copy_2.AddPage(self.notebook_2_pane_3_copy_2, _("Section3"))
        self.notebook_2_copy_2.AddPage(self.notebook_2_pane_4_copy_2, _("Section4"))
        sizer_3_copy_2.Add(self.notebook_2_copy_2, 1, wx.EXPAND, 0)
        self.notebook_1_pane_4.SetSizer(sizer_3_copy_2)
        sizer_8_copy_6.Add(self.G5S1, 1, wx.EXPAND, 0)
        self.panel_1_copy_3.SetSizer(sizer_8_copy_6)
        sizer_4_copy_3.Add(self.panel_1_copy_3, 1, wx.EXPAND, 0)
        self.notebook_2_pane_1_copy_3.SetSizer(sizer_4_copy_3)
        sizer_8_copy_copy_3.Add(self.G5S2, 1, wx.EXPAND, 0)
        self.panel_2_copy_3.SetSizer(sizer_8_copy_copy_3)
        sizer_5_copy_3.Add(self.panel_2_copy_3, 1, wx.EXPAND, 0)
        self.notebook_2_pane_2_copy_3.SetSizer(sizer_5_copy_3)
        sizer_8_copy_1_copy_3.Add(self.G5S3, 1, wx.EXPAND, 0)
        self.panel_3_copy_3.SetSizer(sizer_8_copy_1_copy_3)
        sizer_6_copy_3.Add(self.panel_3_copy_3, 1, wx.EXPAND, 0)
        self.notebook_2_pane_3_copy_3.SetSizer(sizer_6_copy_3)
        sizer_8_copy_2_copy_3.Add(self.G5S4, 1, wx.EXPAND, 0)
        self.panel_4_copy_3.SetSizer(sizer_8_copy_2_copy_3)
        sizer_7_copy_3.Add(self.panel_4_copy_3, 1, wx.EXPAND, 0)
        self.notebook_2_pane_4_copy_3.SetSizer(sizer_7_copy_3)
        self.notebook_2_copy_3.AddPage(self.notebook_2_pane_1_copy_3, _("Section1"))
        self.notebook_2_copy_3.AddPage(self.notebook_2_pane_2_copy_3, _("Section2"))
        self.notebook_2_copy_3.AddPage(self.notebook_2_pane_3_copy_3, _("Section3"))
        self.notebook_2_copy_3.AddPage(self.notebook_2_pane_4_copy_3, _("Section4"))
        sizer_3_copy_3.Add(self.notebook_2_copy_3, 1, wx.EXPAND, 0)
        self.notebook_1_pane_5.SetSizer(sizer_3_copy_3)
        sizer_8_copy_7.Add(self.G6S1, 1, wx.EXPAND, 0)
        self.panel_1_copy_4.SetSizer(sizer_8_copy_7)
        sizer_4_copy_4.Add(self.panel_1_copy_4, 1, wx.EXPAND, 0)
        self.notebook_2_pane_1_copy_4.SetSizer(sizer_4_copy_4)
        sizer_8_copy_copy_4.Add(self.G6S2, 1, wx.EXPAND, 0)
        self.panel_2_copy_4.SetSizer(sizer_8_copy_copy_4)
        sizer_5_copy_4.Add(self.panel_2_copy_4, 1, wx.EXPAND, 0)
        self.notebook_2_pane_2_copy_4.SetSizer(sizer_5_copy_4)
        sizer_8_copy_1_copy_4.Add(self.G6S3, 1, wx.EXPAND, 0)
        self.panel_3_copy_4.SetSizer(sizer_8_copy_1_copy_4)
        sizer_6_copy_4.Add(self.panel_3_copy_4, 1, wx.EXPAND, 0)
        self.notebook_2_pane_3_copy_4.SetSizer(sizer_6_copy_4)
        sizer_8_copy_2_copy_4.Add(self.G6S4, 1, wx.EXPAND, 0)
        self.panel_4_copy_4.SetSizer(sizer_8_copy_2_copy_4)
        sizer_7_copy_4.Add(self.panel_4_copy_4, 1, wx.EXPAND, 0)
        self.notebook_2_pane_4_copy_4.SetSizer(sizer_7_copy_4)
        self.notebook_2_copy_4.AddPage(self.notebook_2_pane_1_copy_4, _("Section1"))
        self.notebook_2_copy_4.AddPage(self.notebook_2_pane_2_copy_4, _("Section2"))
        self.notebook_2_copy_4.AddPage(self.notebook_2_pane_3_copy_4, _("Section3"))
        self.notebook_2_copy_4.AddPage(self.notebook_2_pane_4_copy_4, _("Section4"))
        sizer_3_copy_4.Add(self.notebook_2_copy_4, 1, wx.EXPAND, 0)
        self.notebook_1_pane_6.SetSizer(sizer_3_copy_4)
        sizer_8_copy_8.Add(self.Y1S1, 1, wx.EXPAND, 0)
        self.panel_1_copy_5.SetSizer(sizer_8_copy_8)
        sizer_4_copy_5.Add(self.panel_1_copy_5, 1, wx.EXPAND, 0)
        self.notebook_2_pane_1_copy_5.SetSizer(sizer_4_copy_5)
        sizer_8_copy_copy_5.Add(self.Y1S2, 1, wx.EXPAND, 0)
        self.panel_2_copy_5.SetSizer(sizer_8_copy_copy_5)
        sizer_5_copy_5.Add(self.panel_2_copy_5, 1, wx.EXPAND, 0)
        self.notebook_2_pane_2_copy_5.SetSizer(sizer_5_copy_5)
        sizer_8_copy_1_copy_5.Add(self.Y1S3, 1, wx.EXPAND, 0)
        self.panel_3_copy_5.SetSizer(sizer_8_copy_1_copy_5)
        sizer_6_copy_5.Add(self.panel_3_copy_5, 1, wx.EXPAND, 0)
        self.notebook_2_pane_3_copy_5.SetSizer(sizer_6_copy_5)
        sizer_8_copy_2_copy_5.Add(self.Y1S4, 1, wx.EXPAND, 0)
        self.panel_4_copy_5.SetSizer(sizer_8_copy_2_copy_5)
        sizer_7_copy_5.Add(self.panel_4_copy_5, 1, wx.EXPAND, 0)
        self.notebook_2_pane_4_copy_5.SetSizer(sizer_7_copy_5)
        self.notebook_2_copy_5.AddPage(self.notebook_2_pane_1_copy_5, _("Section1"))
        self.notebook_2_copy_5.AddPage(self.notebook_2_pane_2_copy_5, _("Section2"))
        self.notebook_2_copy_5.AddPage(self.notebook_2_pane_3_copy_5, _("Section3"))
        self.notebook_2_copy_5.AddPage(self.notebook_2_pane_4_copy_5, _("Section4"))
        sizer_3_copy_5.Add(self.notebook_2_copy_5, 1, wx.EXPAND, 0)
        self.notebook_1_pane_7.SetSizer(sizer_3_copy_5)
        sizer_8_copy_9.Add(self.Y2S1, 1, wx.EXPAND, 0)
        self.panel_1_copy_6.SetSizer(sizer_8_copy_9)
        sizer_4_copy_6.Add(self.panel_1_copy_6, 1, wx.EXPAND, 0)
        self.notebook_2_pane_1_copy_6.SetSizer(sizer_4_copy_6)
        sizer_8_copy_copy_6.Add(self.Y2S2, 1, wx.EXPAND, 0)
        self.panel_2_copy_6.SetSizer(sizer_8_copy_copy_6)
        sizer_5_copy_6.Add(self.panel_2_copy_6, 1, wx.EXPAND, 0)
        self.notebook_2_pane_2_copy_6.SetSizer(sizer_5_copy_6)
        sizer_8_copy_1_copy_6.Add(self.Y2S3, 1, wx.EXPAND, 0)
        self.panel_3_copy_6.SetSizer(sizer_8_copy_1_copy_6)
        sizer_6_copy_6.Add(self.panel_3_copy_6, 1, wx.EXPAND, 0)
        self.notebook_2_pane_3_copy_6.SetSizer(sizer_6_copy_6)
        sizer_8_copy_2_copy_6.Add(self.Y2S4, 1, wx.EXPAND, 0)
        self.panel_4_copy_6.SetSizer(sizer_8_copy_2_copy_6)
        sizer_7_copy_6.Add(self.panel_4_copy_6, 1, wx.EXPAND, 0)
        self.notebook_2_pane_4_copy_6.SetSizer(sizer_7_copy_6)
        self.notebook_2_copy_6.AddPage(self.notebook_2_pane_1_copy_6, _("Section1"))
        self.notebook_2_copy_6.AddPage(self.notebook_2_pane_2_copy_6, _("Section2"))
        self.notebook_2_copy_6.AddPage(self.notebook_2_pane_3_copy_6, _("Section3"))
        self.notebook_2_copy_6.AddPage(self.notebook_2_pane_4_copy_6, _("Section4"))
        sizer_3_copy_6.Add(self.notebook_2_copy_6, 1, wx.EXPAND, 0)
        self.notebook_1_pane_8.SetSizer(sizer_3_copy_6)
        sizer_8_copy_9_copy.Add(self.Y3S1, 1, wx.EXPAND, 0)
        self.panel_1_copy_6_copy.SetSizer(sizer_8_copy_9_copy)
        sizer_4_copy_6_copy.Add(self.panel_1_copy_6_copy, 1, wx.EXPAND, 0)
        self.notebook_2_pane_1_copy_6_copy.SetSizer(sizer_4_copy_6_copy)
        sizer_8_copy_copy_6_copy.Add(self.Y3S2, 1, wx.EXPAND, 0)
        self.panel_2_copy_6_copy.SetSizer(sizer_8_copy_copy_6_copy)
        sizer_5_copy_6_copy.Add(self.panel_2_copy_6_copy, 1, wx.EXPAND, 0)
        self.notebook_2_pane_2_copy_6_copy.SetSizer(sizer_5_copy_6_copy)
        sizer_8_copy_1_copy_6_copy.Add(self.Y3S3, 1, wx.EXPAND, 0)
        self.panel_3_copy_6_copy.SetSizer(sizer_8_copy_1_copy_6_copy)
        sizer_6_copy_6_copy.Add(self.panel_3_copy_6_copy, 1, wx.EXPAND, 0)
        self.notebook_2_pane_3_copy_6_copy.SetSizer(sizer_6_copy_6_copy)
        sizer_8_copy_2_copy_6_copy.Add(self.Y3S4, 1, wx.EXPAND, 0)
        self.panel_4_copy_6_copy.SetSizer(sizer_8_copy_2_copy_6_copy)
        sizer_7_copy_6_copy.Add(self.panel_4_copy_6_copy, 1, wx.EXPAND, 0)
        self.notebook_2_pane_4_copy_6_copy.SetSizer(sizer_7_copy_6_copy)
        self.notebook_2_copy_6_copy.AddPage(self.notebook_2_pane_1_copy_6_copy, _("Section1"))
        self.notebook_2_copy_6_copy.AddPage(self.notebook_2_pane_2_copy_6_copy, _("Section2"))
        self.notebook_2_copy_6_copy.AddPage(self.notebook_2_pane_3_copy_6_copy, _("Section3"))
        self.notebook_2_copy_6_copy.AddPage(self.notebook_2_pane_4_copy_6_copy, _("Section4"))
        sizer_3_copy_6_copy.Add(self.notebook_2_copy_6_copy, 1, wx.EXPAND, 0)
        self.notebook_1_pane_8_copy.SetSizer(sizer_3_copy_6_copy)
        sizer_8_copy_10.Add(self.Y4S1, 1, wx.EXPAND, 0)
        self.panel_1_copy_7.SetSizer(sizer_8_copy_10)
        sizer_4_copy_7.Add(self.panel_1_copy_7, 1, wx.EXPAND, 0)
        self.notebook_2_pane_1_copy_7.SetSizer(sizer_4_copy_7)
        sizer_8_copy_copy_7.Add(self.Y4S2, 1, wx.EXPAND, 0)
        self.panel_2_copy_7.SetSizer(sizer_8_copy_copy_7)
        sizer_5_copy_7.Add(self.panel_2_copy_7, 1, wx.EXPAND, 0)
        self.notebook_2_pane_2_copy_7.SetSizer(sizer_5_copy_7)
        sizer_8_copy_1_copy_7.Add(self.Y4S3, 1, wx.EXPAND, 0)
        self.panel_3_copy_7.SetSizer(sizer_8_copy_1_copy_7)
        sizer_6_copy_7.Add(self.panel_3_copy_7, 1, wx.EXPAND, 0)
        self.notebook_2_pane_3_copy_7.SetSizer(sizer_6_copy_7)
        sizer_8_copy_2_copy_7.Add(self.Y4S4, 1, wx.EXPAND, 0)
        self.panel_4_copy_7.SetSizer(sizer_8_copy_2_copy_7)
        sizer_7_copy_7.Add(self.panel_4_copy_7, 1, wx.EXPAND, 0)
        self.notebook_2_pane_4_copy_7.SetSizer(sizer_7_copy_7)
        self.notebook_2_copy_7.AddPage(self.notebook_2_pane_1_copy_7, _("Section1"))
        self.notebook_2_copy_7.AddPage(self.notebook_2_pane_2_copy_7, _("Section2"))
        self.notebook_2_copy_7.AddPage(self.notebook_2_pane_3_copy_7, _("Section3"))
        self.notebook_2_copy_7.AddPage(self.notebook_2_pane_4_copy_7, _("Section4"))
        sizer_3_copy_7.Add(self.notebook_2_copy_7, 1, wx.EXPAND, 0)
        self.notebook_1_pane_10.SetSizer(sizer_3_copy_7)
        self.notebook_1.AddPage(self.notebook_1_pane_1, _("Grade1"))
        self.notebook_1.AddPage(self.notebook_1_pane_2, _("Grade2"))
        self.notebook_1.AddPage(self.notebook_1_pane_3, _("Grade3"))
        self.notebook_1.AddPage(self.notebook_1_pane_4, _("Grade4"))
        self.notebook_1.AddPage(self.notebook_1_pane_5, _("Grade5"))
        self.notebook_1.AddPage(self.notebook_1_pane_6, _("Grade6"))
        self.notebook_1.AddPage(self.notebook_1_pane_7, _("Year1"))
        self.notebook_1.AddPage(self.notebook_1_pane_8, _("Year2"))
        self.notebook_1.AddPage(self.notebook_1_pane_8_copy, _("Year3"))
        self.notebook_1.AddPage(self.notebook_1_pane_10, _("Year4"))
        sizer_1.Add(self.notebook_1, 1, wx.EXPAND, 0)
        self.SetSizer(sizer_1)
        self.Layout()
		
    def load(self,event):
        self.refreshdata()	
    def refreshdata(self):
        self.G1S1.ClearGrid()
       
        SY= (self.combo_box_1.GetValue())
        db = connectdb()
        cur = db.cursor()
        cur.execute("SELECT Students.Student_ID, Students.LastName, Students.FirstName, Students.MiddleName FROM Students, ClassRecords WHERE Students.Student_ID=ClassRecords.Students_Student_ID AND ClassRecords.SchoolYear= %s AND ClassRecords.Year='Grade1' AND ClassRecords.Section='Section1'",(SY))
        rows=cur.fetchall()

       
        for i in range (0,len(rows)):
            for j in range(0,4):
                cell = rows[i]
                self.G1S1.SetCellValue(i,j,str(cell[j]))
				
       
        cur.execute("SELECT Students.Student_ID, Students.LastName, Students.FirstName, Students.MiddleName FROM Students, ClassRecords WHERE Students.Student_ID=ClassRecords.Students_Student_ID AND ClassRecords.SchoolYear= %s AND ClassRecords.Year='Grade1' AND ClassRecords.Section='Section2'",(SY))
        rows=cur.fetchall()

       
        for i in range (0,len(rows)):
            for j in range(0,4):
                cell = rows[i]
                self.G1S2.SetCellValue(i,j,str(cell[j]))

        cur.execute("SELECT Students.Student_ID, Students.LastName, Students.FirstName, Students.MiddleName FROM Students, ClassRecords WHERE Students.Student_ID=ClassRecords.Students_Student_ID AND ClassRecords.SchoolYear= %s AND ClassRecords.Year='Grade1' AND ClassRecords.Section='Section3'",(SY))
        rows=cur.fetchall()

       
        for i in range (0,len(rows)):
            for j in range(0,4):
                cell = rows[i]
                self.G1S3.SetCellValue(i,j,str(cell[j]))

        cur.execute("SELECT Students.Student_ID, Students.LastName, Students.FirstName, Students.MiddleName FROM Students, ClassRecords WHERE Students.Student_ID=ClassRecords.Students_Student_ID AND ClassRecords.SchoolYear= %s AND ClassRecords.Year='Grade1' AND ClassRecords.Section='Section4'",(SY))
        rows=cur.fetchall()

       
        for i in range (0,len(rows)):
            for j in range(0,4):
                cell = rows[i]
                self.G1S4.SetCellValue(i,j,str(cell[j]))

        cur.execute("SELECT Students.Student_ID, Students.LastName, Students.FirstName, Students.MiddleName FROM Students, ClassRecords WHERE Students.Student_ID=ClassRecords.Students_Student_ID AND ClassRecords.SchoolYear= %s AND ClassRecords.Year='Grade2' AND ClassRecords.Section='Section1'",(SY))
        rows=cur.fetchall()

       
        for i in range (0,len(rows)):
            for j in range(0,4):
                cell = rows[i]
                self.G2S1.SetCellValue(i,j,str(cell[j]))

        cur.execute("SELECT Students.Student_ID, Students.LastName, Students.FirstName, Students.MiddleName FROM Students, ClassRecords WHERE Students.Student_ID=ClassRecords.Students_Student_ID AND ClassRecords.SchoolYear= %s AND ClassRecords.Year='Grade2' AND ClassRecords.Section='Section2'",(SY))
        rows=cur.fetchall()

       
        for i in range (0,len(rows)):
            for j in range(0,4):
                cell = rows[i]
                self.G2S2.SetCellValue(i,j,str(cell[j]))

        cur.execute("SELECT Students.Student_ID, Students.LastName, Students.FirstName, Students.MiddleName FROM Students, ClassRecords WHERE Students.Student_ID=ClassRecords.Students_Student_ID AND ClassRecords.SchoolYear= %s AND ClassRecords.Year='Grade2' AND ClassRecords.Section='Section3'",(SY))
        rows=cur.fetchall()

       
        for i in range (0,len(rows)):
            for j in range(0,4):
                cell = rows[i]
                self.G2S3.SetCellValue(i,j,str(cell[j]))

        cur.execute("SELECT Students.Student_ID, Students.LastName, Students.FirstName, Students.MiddleName FROM Students, ClassRecords WHERE Students.Student_ID=ClassRecords.Students_Student_ID AND ClassRecords.SchoolYear= %s AND ClassRecords.Year='Grade2' AND ClassRecords.Section='Section4'",(SY))
        rows=cur.fetchall()

       
        for i in range (0,len(rows)):
            for j in range(0,4):
                cell = rows[i]
                self.G2S4.SetCellValue(i,j,str(cell[j]))

        cur.execute("SELECT Students.Student_ID, Students.LastName, Students.FirstName, Students.MiddleName FROM Students, ClassRecords WHERE Students.Student_ID=ClassRecords.Students_Student_ID AND ClassRecords.SchoolYear= %s AND ClassRecords.Year='Grade3' AND ClassRecords.Section='Section1'",(SY))
        rows=cur.fetchall()

       
        for i in range (0,len(rows)):
            for j in range(0,4):
                cell = rows[i]
                self.G3S1.SetCellValue(i,j,str(cell[j]))

        cur.execute("SELECT Students.Student_ID, Students.LastName, Students.FirstName, Students.MiddleName FROM Students, ClassRecords WHERE Students.Student_ID=ClassRecords.Students_Student_ID AND ClassRecords.SchoolYear= %s AND ClassRecords.Year='Grade3' AND ClassRecords.Section='Section2'",(SY))
        rows=cur.fetchall()

       
        for i in range (0,len(rows)):
            for j in range(0,4):
                cell = rows[i]
                self.G3S2.SetCellValue(i,j,str(cell[j]))

        cur.execute("SELECT Students.Student_ID, Students.LastName, Students.FirstName, Students.MiddleName FROM Students, ClassRecords WHERE Students.Student_ID=ClassRecords.Students_Student_ID AND ClassRecords.SchoolYear= %s AND ClassRecords.Year='Grade3' AND ClassRecords.Section='Section3'",(SY))
        rows=cur.fetchall()

       
        for i in range (0,len(rows)):
            for j in range(0,4):
                cell = rows[i]
                self.G3S3.SetCellValue(i,j,str(cell[j]))

        cur.execute("SELECT Students.Student_ID, Students.LastName, Students.FirstName, Students.MiddleName FROM Students, ClassRecords WHERE Students.Student_ID=ClassRecords.Students_Student_ID AND ClassRecords.SchoolYear= %s AND ClassRecords.Year='Grade3' AND ClassRecords.Section='Section4'",(SY))
        rows=cur.fetchall()

       
        for i in range (0,len(rows)):
            for j in range(0,4):
                cell = rows[i]
                self.G3S4.SetCellValue(i,j,str(cell[j]))

        cur.execute("SELECT Students.Student_ID, Students.LastName, Students.FirstName, Students.MiddleName FROM Students, ClassRecords WHERE Students.Student_ID=ClassRecords.Students_Student_ID AND ClassRecords.SchoolYear= %s AND ClassRecords.Year='Grade4' AND ClassRecords.Section='Section1'",(SY))
        rows=cur.fetchall()

       
        for i in range (0,len(rows)):
            for j in range(0,4):
                cell = rows[i]
                self.G4S1.SetCellValue(i,j,str(cell[j]))

        cur.execute("SELECT Students.Student_ID, Students.LastName, Students.FirstName, Students.MiddleName FROM Students, ClassRecords WHERE Students.Student_ID=ClassRecords.Students_Student_ID AND ClassRecords.SchoolYear= %s AND ClassRecords.Year='Grade4' AND ClassRecords.Section='Section2'",(SY))
        rows=cur.fetchall()

       
        for i in range (0,len(rows)):
            for j in range(0,4):
                cell = rows[i]
                self.G4S2.SetCellValue(i,j,str(cell[j]))

        cur.execute("SELECT Students.Student_ID, Students.LastName, Students.FirstName, Students.MiddleName FROM Students, ClassRecords WHERE Students.Student_ID=ClassRecords.Students_Student_ID AND ClassRecords.SchoolYear= %s AND ClassRecords.Year='Grade4' AND ClassRecords.Section='Section3'",(SY))
        rows=cur.fetchall()

       
        for i in range (0,len(rows)):
            for j in range(0,4):
                cell = rows[i]
                self.G4S3.SetCellValue(i,j,str(cell[j]))

        cur.execute("SELECT Students.Student_ID, Students.LastName, Students.FirstName, Students.MiddleName FROM Students, ClassRecords WHERE Students.Student_ID=ClassRecords.Students_Student_ID AND ClassRecords.SchoolYear= %s AND ClassRecords.Year='Grade4' AND ClassRecords.Section='Section4'",(SY))
        rows=cur.fetchall()

       
        for i in range (0,len(rows)):
            for j in range(0,4):
                cell = rows[i]
                self.G4S4.SetCellValue(i,j,str(cell[j]))

        cur.execute("SELECT Students.Student_ID, Students.LastName, Students.FirstName, Students.MiddleName FROM Students, ClassRecords WHERE Students.Student_ID=ClassRecords.Students_Student_ID AND ClassRecords.SchoolYear= %s AND ClassRecords.Year='Grade5' AND ClassRecords.Section='Section1'",(SY))
        rows=cur.fetchall()

       
        for i in range (0,len(rows)):
            for j in range(0,4):
                cell = rows[i]
                self.G5S1.SetCellValue(i,j,str(cell[j]))

        cur.execute("SELECT Students.Student_ID, Students.LastName, Students.FirstName, Students.MiddleName FROM Students, ClassRecords WHERE Students.Student_ID=ClassRecords.Students_Student_ID AND ClassRecords.SchoolYear= %s AND ClassRecords.Year='Grade5' AND ClassRecords.Section='Section2'",(SY))
        rows=cur.fetchall()

       
        for i in range (0,len(rows)):
            for j in range(0,4):
                cell = rows[i]
                self.G5S2.SetCellValue(i,j,str(cell[j]))

        cur.execute("SELECT Students.Student_ID, Students.LastName, Students.FirstName, Students.MiddleName FROM Students, ClassRecords WHERE Students.Student_ID=ClassRecords.Students_Student_ID AND ClassRecords.SchoolYear= %s AND ClassRecords.Year='Grade5' AND ClassRecords.Section='Section3'",(SY))
        rows=cur.fetchall()

       
        for i in range (0,len(rows)):
            for j in range(0,4):
                cell = rows[i]
                self.G5S3.SetCellValue(i,j,str(cell[j]))

        cur.execute("SELECT Students.Student_ID, Students.LastName, Students.FirstName, Students.MiddleName FROM Students, ClassRecords WHERE Students.Student_ID=ClassRecords.Students_Student_ID AND ClassRecords.SchoolYear= %s AND ClassRecords.Year='Grade5' AND ClassRecords.Section='Section4'",(SY))
        rows=cur.fetchall()

       
        for i in range (0,len(rows)):
            for j in range(0,4):
                cell = rows[i]
                self.G5S4.SetCellValue(i,j,str(cell[j]))

        cur.execute("SELECT Students.Student_ID, Students.LastName, Students.FirstName, Students.MiddleName FROM Students, ClassRecords WHERE Students.Student_ID=ClassRecords.Students_Student_ID AND ClassRecords.SchoolYear= %s AND ClassRecords.Year='Grade6' AND ClassRecords.Section='Section1'",(SY))
        rows=cur.fetchall()

       
        for i in range (0,len(rows)):
            for j in range(0,4):
                cell = rows[i]
                self.G6S1.SetCellValue(i,j,str(cell[j]))

        cur.execute("SELECT Students.Student_ID, Students.LastName, Students.FirstName, Students.MiddleName FROM Students, ClassRecords WHERE Students.Student_ID=ClassRecords.Students_Student_ID AND ClassRecords.SchoolYear= %s AND ClassRecords.Year='Grade6' AND ClassRecords.Section='Section2'",(SY))
        rows=cur.fetchall()

       
        for i in range (0,len(rows)):
            for j in range(0,4):
                cell = rows[i]
                self.G6S2.SetCellValue(i,j,str(cell[j]))

        cur.execute("SELECT Students.Student_ID, Students.LastName, Students.FirstName, Students.MiddleName FROM Students, ClassRecords WHERE Students.Student_ID=ClassRecords.Students_Student_ID AND ClassRecords.SchoolYear= %s AND ClassRecords.Year='Grade6' AND ClassRecords.Section='Section3'",(SY))
        rows=cur.fetchall()

       
        for i in range (0,len(rows)):
            for j in range(0,4):
                cell = rows[i]
                self.G6S3.SetCellValue(i,j,str(cell[j]))

        cur.execute("SELECT Students.Student_ID, Students.LastName, Students.FirstName, Students.MiddleName FROM Students, ClassRecords WHERE Students.Student_ID=ClassRecords.Students_Student_ID AND ClassRecords.SchoolYear= %s AND ClassRecords.Year='Grade6' AND ClassRecords.Section='Section4'",(SY))
        rows=cur.fetchall()

       
        for i in range (0,len(rows)):
            for j in range(0,4):
                cell = rows[i]
                self.G6S4.SetCellValue(i,j,str(cell[j]))

        cur.execute("SELECT Students.Student_ID, Students.LastName, Students.FirstName, Students.MiddleName FROM Students, ClassRecords WHERE Students.Student_ID=ClassRecords.Students_Student_ID AND ClassRecords.SchoolYear= %s AND ClassRecords.Year='Year1' AND ClassRecords.Section='Section1'",(SY))
        rows=cur.fetchall()

       
        for i in range (0,len(rows)):
            for j in range(0,4):
                cell = rows[i]
                self.Y1S1.SetCellValue(i,j,str(cell[j]))

        cur.execute("SELECT Students.Student_ID, Students.LastName, Students.FirstName, Students.MiddleName FROM Students, ClassRecords WHERE Students.Student_ID=ClassRecords.Students_Student_ID AND ClassRecords.SchoolYear= %s AND ClassRecords.Year='Year1' AND ClassRecords.Section='Section2'",(SY))
        rows=cur.fetchall()

       
        for i in range (0,len(rows)):
            for j in range(0,4):
                cell = rows[i]
                self.Y1S2.SetCellValue(i,j,str(cell[j]))

        cur.execute("SELECT Students.Student_ID, Students.LastName, Students.FirstName, Students.MiddleName FROM Students, ClassRecords WHERE Students.Student_ID=ClassRecords.Students_Student_ID AND ClassRecords.SchoolYear= %s AND ClassRecords.Year='Year1' AND ClassRecords.Section='Section3'",(SY))
        rows=cur.fetchall()

       
        for i in range (0,len(rows)):
            for j in range(0,4):
                cell = rows[i]
                self.Y1S3.SetCellValue(i,j,str(cell[j]))

        cur.execute("SELECT Students.Student_ID, Students.LastName, Students.FirstName, Students.MiddleName FROM Students, ClassRecords WHERE Students.Student_ID=ClassRecords.Students_Student_ID AND ClassRecords.SchoolYear= %s AND ClassRecords.Year='Year1' AND ClassRecords.Section='Section4'",(SY))
        rows=cur.fetchall()

       
        for i in range (0,len(rows)):
            for j in range(0,4):
                cell = rows[i]
                self.Y1S4.SetCellValue(i,j,str(cell[j]))

        cur.execute("SELECT Students.Student_ID, Students.LastName, Students.FirstName, Students.MiddleName FROM Students, ClassRecords WHERE Students.Student_ID=ClassRecords.Students_Student_ID AND ClassRecords.SchoolYear= %s AND ClassRecords.Year='Year2' AND ClassRecords.Section='Section1'",(SY))
        rows=cur.fetchall()

       
        for i in range (0,len(rows)):
            for j in range(0,4):
                cell = rows[i]
                self.Y2S1.SetCellValue(i,j,str(cell[j]))

        cur.execute("SELECT Students.Student_ID, Students.LastName, Students.FirstName, Students.MiddleName FROM Students, ClassRecords WHERE Students.Student_ID=ClassRecords.Students_Student_ID AND ClassRecords.SchoolYear= %s AND ClassRecords.Year='Year2' AND ClassRecords.Section='Section2'",(SY))
        rows=cur.fetchall()

       
        for i in range (0,len(rows)):
            for j in range(0,4):
                cell = rows[i]
                self.Y2S2.SetCellValue(i,j,str(cell[j]))

        cur.execute("SELECT Students.Student_ID, Students.LastName, Students.FirstName, Students.MiddleName FROM Students, ClassRecords WHERE Students.Student_ID=ClassRecords.Students_Student_ID AND ClassRecords.SchoolYear= %s AND ClassRecords.Year='Year2' AND ClassRecords.Section='Section3'",(SY))
        rows=cur.fetchall()

       
        for i in range (0,len(rows)):
            for j in range(0,4):
                cell = rows[i]
                self.Y2S3.SetCellValue(i,j,str(cell[j]))

        cur.execute("SELECT Students.Student_ID, Students.LastName, Students.FirstName, Students.MiddleName FROM Students, ClassRecords WHERE Students.Student_ID=ClassRecords.Students_Student_ID AND ClassRecords.SchoolYear= %s AND ClassRecords.Year='Year2' AND ClassRecords.Section='Section4'",(SY))
        rows=cur.fetchall()

       
        for i in range (0,len(rows)):
            for j in range(0,4):
                cell = rows[i]
                self.Y2S4.SetCellValue(i,j,str(cell[j]))

        cur.execute("SELECT Students.Student_ID, Students.LastName, Students.FirstName, Students.MiddleName FROM Students, ClassRecords WHERE Students.Student_ID=ClassRecords.Students_Student_ID AND ClassRecords.SchoolYear= %s AND ClassRecords.Year='Year3' AND ClassRecords.Section='Section1'",(SY))
        rows=cur.fetchall()

       
        for i in range (0,len(rows)):
            for j in range(0,4):
                cell = rows[i]
                self.Y3S1.SetCellValue(i,j,str(cell[j]))

        cur.execute("SELECT Students.Student_ID, Students.LastName, Students.FirstName, Students.MiddleName FROM Students, ClassRecords WHERE Students.Student_ID=ClassRecords.Students_Student_ID AND ClassRecords.SchoolYear= %s AND ClassRecords.Year='Year3' AND ClassRecords.Section='Section2'",(SY))
        rows=cur.fetchall()

       
        for i in range (0,len(rows)):
            for j in range(0,4):
                cell = rows[i]
                self.Y3S2.SetCellValue(i,j,str(cell[j]))

        cur.execute("SELECT Students.Student_ID, Students.LastName, Students.FirstName, Students.MiddleName FROM Students, ClassRecords WHERE Students.Student_ID=ClassRecords.Students_Student_ID AND ClassRecords.SchoolYear= %s AND ClassRecords.Year='Year3' AND ClassRecords.Section='Section3'",(SY))
        rows=cur.fetchall()

       
        for i in range (0,len(rows)):
            for j in range(0,4):
                cell = rows[i]
                self.Y3S3.SetCellValue(i,j,str(cell[j]))

        cur.execute("SELECT Students.Student_ID, Students.LastName, Students.FirstName, Students.MiddleName FROM Students, ClassRecords WHERE Students.Student_ID=ClassRecords.Students_Student_ID AND ClassRecords.SchoolYear= %s AND ClassRecords.Year='Year3' AND ClassRecords.Section='Section4'",(SY))
        rows=cur.fetchall()

       
        for i in range (0,len(rows)):
            for j in range(0,4):
                cell = rows[i]
                self.Y3S4.SetCellValue(i,j,str(cell[j]))

        cur.execute("SELECT Students.Student_ID, Students.LastName, Students.FirstName, Students.MiddleName FROM Students, ClassRecords WHERE Students.Student_ID=ClassRecords.Students_Student_ID AND ClassRecords.SchoolYear= %s AND ClassRecords.Year='Year4' AND ClassRecords.Section='Section1'",(SY))
        rows=cur.fetchall()

       
        for i in range (0,len(rows)):
            for j in range(0,4):
                cell = rows[i]
                self.Y4S1.SetCellValue(i,j,str(cell[j]))

        cur.execute("SELECT Students.Student_ID, Students.LastName, Students.FirstName, Students.MiddleName FROM Students, ClassRecords WHERE Students.Student_ID=ClassRecords.Students_Student_ID AND ClassRecords.SchoolYear= %s AND ClassRecords.Year='Year4' AND ClassRecords.Section='Section2'",(SY))
        rows=cur.fetchall()

       
        for i in range (0,len(rows)):
            for j in range(0,4):
                cell = rows[i]
                self.Y4S2.SetCellValue(i,j,str(cell[j]))

        cur.execute("SELECT Students.Student_ID, Students.LastName, Students.FirstName, Students.MiddleName FROM Students, ClassRecords WHERE Students.Student_ID=ClassRecords.Students_Student_ID AND ClassRecords.SchoolYear= %s AND ClassRecords.Year='Year4' AND ClassRecords.Section='Section3'",(SY))
        rows=cur.fetchall()

       
        for i in range (0,len(rows)):
            for j in range(0,4):
                cell = rows[i]
                self.Y4S3.SetCellValue(i,j,str(cell[j]))

        cur.execute("SELECT Students.Student_ID, Students.LastName, Students.FirstName, Students.MiddleName FROM Students, ClassRecords WHERE Students.Student_ID=ClassRecords.Students_Student_ID AND ClassRecords.SchoolYear= %s AND ClassRecords.Year='Year4' AND ClassRecords.Section='Section4'",(SY))
        rows=cur.fetchall()

       
        for i in range (0,len(rows)):
            for j in range(0,4):
                cell = rows[i]
                self.Y4S4.SetCellValue(i,j,str(cell[j]))
    