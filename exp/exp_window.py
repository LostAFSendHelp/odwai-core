# -*- coding: utf-8 -*- 

###########################################################################
## Python code generated with wxFormBuilder (version Jun 17 2015)
## http://www.wxformbuilder.org/
##
## PLEASE DO "NOT" EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc

###########################################################################
## Class MyFrame2
###########################################################################

class MyFrame2 ( wx.Frame ):
	
	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( 243,181 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )
		
		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )
		
		gSizer2 = wx.GridSizer( 0, 2, 0, 0 )
		
		self.get_button = wx.Button( self, wx.ID_ANY, u"Get Frame", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.get_button.SetMinSize( wx.Size( 100,-1 ) )
		
		gSizer2.Add( self.get_button, 0, wx.ALL, 5 )
		
		self.static_button = wx.Button( self, wx.ID_ANY, u"Static dtcn", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.static_button.SetMinSize( wx.Size( 100,-1 ) )
		
		gSizer2.Add( self.static_button, 0, wx.ALL, 5 )
		
		self.automate_button = wx.Button( self, wx.ID_ANY, u"Automate", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.automate_button.SetMinSize( wx.Size( 100,-1 ) )
		
		gSizer2.Add( self.automate_button, 0, wx.ALL, 5 )
		
		self.realtime_button = wx.Button( self, wx.ID_ANY, u"Real-time dtcn", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.realtime_button.SetMinSize( wx.Size( 100,-1 ) )
		
		gSizer2.Add( self.realtime_button, 0, wx.ALL, 5 )
		
		self.hide_button = wx.Button( self, wx.ID_ANY, u"Hide", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.hide_button.SetMinSize( wx.Size( 100,-1 ) )
		
		gSizer2.Add( self.hide_button, 0, wx.ALL, 5 )
		
		self.quit_button = wx.Button( self, wx.ID_ANY, u"Quit", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.quit_button.SetMinSize( wx.Size( 100,-1 ) )
		
		gSizer2.Add( self.quit_button, 0, wx.ALL, 5 )
		
		self.automate_checkbox = wx.CheckBox( self, wx.ID_ANY, u"Automate without checking", wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer2.Add( self.automate_checkbox, 0, wx.ALL, 5 )
		
		
		self.SetSizer( gSizer2 )
		self.Layout()
		
		self.Centre( wx.BOTH )
	
	def __del__( self ):
		pass
	

if __name__ == "__main__":
    app = wx.App()
    frame = MyFrame2(None)
    frame.Show()
    app.exec_()