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

# class giao diện window, vẽ bằng wxFrameBuilder
class OdwaiWindow ( wx.Frame ):
	
	def __init__( self, controller ):
		wx.Frame.__init__ ( self, None, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( 243,181 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )
        
		# gán controller (odwai_app, class: TaskBarIcon) để gọi hàm
		self.controller = controller
		
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
		
		self.exit_button = wx.Button( self, wx.ID_ANY, u"Quit", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.exit_button.SetMinSize( wx.Size( 100,-1 ) )
		
		gSizer2.Add( self.exit_button, 0, wx.ALL, 5 )
		
		self.automate_checkbox = wx.CheckBox( self, wx.ID_ANY, u"Automate without checking", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.automate_checkbox.SetValue(self.controller.skip_check)
		gSizer2.Add( self.automate_checkbox, 0, wx.ALL, 5 )
		
		
		self.SetSizer( gSizer2 )
		self.Layout()

        # Connect Events
		self.get_button.Bind( wx.EVT_BUTTON, self.controller.on_get )
		self.realtime_button.Bind( wx.EVT_BUTTON, self.controller.on_realtime )
		self.static_button.Bind( wx.EVT_BUTTON, self.controller.on_static )
		self.automate_button.Bind( wx.EVT_BUTTON, self.controller.on_simulate )
		self.hide_button.Bind( wx.EVT_BUTTON, lambda x: self.Hide() )
		self.exit_button.Bind( wx.EVT_BUTTON, self.controller.on_exit )
		self.automate_checkbox.Bind( wx.EVT_CHECKBOX, self.controller.toggle_skip_check )
		self.Bind(wx.EVT_CLOSE, lambda x: self.Hide())
		
		self.Centre( wx.BOTH )

		
		self.Centre( wx.BOTH )

	def toggle(self, event):
		print(self.automate_checkbox.GetValue())
		print(self.controller.skip_check)
