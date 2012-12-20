from taskbaricon import TaskBarIcon
import wx

def main():
    app = wx.PySimpleApp()
    TaskBarIcon()
    app.MainLoop()
    
if __name__ == '__main__':
    main()