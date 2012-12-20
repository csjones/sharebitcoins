from sendmanytransactions import SendManyTransactions
import wx

#   http://www.zetcode.com/wxpython/dialogs/
class CreateBatch(wx.Dialog):

    def __init__(self, *args, **kw):
        super(CreateBatch, self).__init__(*args, **kw) 
        self.InitUI()
        self.SetSize((300, 125))
        self.SetTitle("Share Bitcoins")
        
    def InitUI(self):
        pnl = wx.Panel(self)
        tc = wx.TextCtrl(pnl)
        
        sb = wx.StaticBox(pnl, label='New Batch Name')
        sbs = wx.StaticBoxSizer(sb, orient=wx.VERTICAL)
        sbs.Add(tc, flag=wx.EXPAND, border=5)

        pnl.SetSizer(sbs)

        hbox2 = wx.BoxSizer(wx.HORIZONTAL)
        
        okButton = wx.Button(self, label='Ok')
#   http://stackoverflow.com/questions/173687/is-it-possible-to-pass-arguments-into-event-bindings
        okButton.Bind(wx.EVT_BUTTON, lambda event: self.On_Okay(event, tc.GetValue() ) )
        
        closeButton = wx.Button(self, label='Close')
        closeButton.Bind(wx.EVT_BUTTON, self.On_Close)
        
        hbox2.Add(okButton)
        hbox2.Add(closeButton, flag=wx.LEFT, border=5)

        vbox = wx.BoxSizer(wx.VERTICAL)
        vbox.Add(pnl, proportion=1, flag=wx.ALL|wx.EXPAND, border=5)
        vbox.Add(hbox2, flag=wx.ALIGN_CENTER|wx.TOP|wx.BOTTOM, border=10)

        self.SetSizer(vbox)
        
    def On_Close(self, event):
        self.Destroy()
        
    def On_Okay(self, event, batchName):
        SendManyTransactions().createNewBatch(batchName)
        self.Destroy()