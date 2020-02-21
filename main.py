import wx
import keyboard
import tkinter as tk

import master as mt
import odwai_app

root = tk.Tk()
width = int(root.winfo_screenwidth()/2)
height = int(root.winfo_screenheight())
master = mt.Master(0, 0, width, height)

class App(wx.App):

    def OnInit(self):
        frame = wx.Frame(None)
        self.icon = odwai_app.TaskBarIcon(frame, master)
        self.SetTopWindow(self.icon.frame)
        return True

def main():
    app = App(False)
    keyboard.add_hotkey("ctrl+f1", app.icon.on_get)
    keyboard.add_hotkey("ctrl+f2", app.icon.on_static)
    keyboard.add_hotkey("ctrl+f3", app.icon.on_realtime)
    keyboard.add_hotkey("ctrl+f6", app.icon.on_simulate)
    app.MainLoop()

if __name__ == "__main__":
    main()
