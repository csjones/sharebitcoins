from sendmanytransactions import SendManyTransactions
import wx

#   http://www.zetcode.com/wxpython/dialogs/
class CreateTransaction(wx.Dialog):

    def __init__(self, *args, **kw):
        super(CreateTransaction, self).__init__(*args, **kw) 
        self.InitUI()
        self.SetSize((200, 175))
        self.SetTitle("Share Bitcoins")
        
    def InitUI(self):
        pnl = wx.Panel(self)
        
        st1 = wx.StaticText(pnl,label="Hexadecimal Private Key")
        tc1 = wx.TextCtrl(pnl)
        st2 = wx.StaticText(pnl,label="Bitcoins Per Share")
        tc2 = wx.TextCtrl(pnl)
        
        sb = wx.StaticBox(pnl, label='Create Transaction')
        sbs = wx.StaticBoxSizer(sb, orient=wx.VERTICAL)
        sbs.Add(st1, flag=wx.LEFT, border=5)
        sbs.Add(tc1, flag=wx.EXPAND, border=5)
        sbs.Add(st2, flag=wx.LEFT, border=5)
        sbs.Add(tc2, flag=wx.EXPAND, border=5)

        pnl.SetSizer(sbs)

        hbox2 = wx.BoxSizer(wx.HORIZONTAL)
        
        okButton = wx.Button(self, wx.ID_OK)
#   http://stackoverflow.com/questions/173687/is-it-possible-to-pass-arguments-into-event-bindings
        okButton.Bind(wx.EVT_BUTTON, lambda event: self.On_Okay(event, tc1.GetValue(), tc2.GetValue() ) )
        
        closeButton = wx.Button(self, wx.ID_CLOSE)
        closeButton.Bind(wx.EVT_BUTTON, self.On_Close)
        
        hbox2.Add(okButton)
        hbox2.Add(closeButton, flag=wx.LEFT, border=5)

        vbox = wx.BoxSizer(wx.VERTICAL)
        vbox.Add(pnl, proportion=1, flag=wx.ALL|wx.EXPAND, border=5)
        vbox.Add(hbox2, flag=wx.ALIGN_CENTER|wx.TOP|wx.BOTTOM, border=10)

        self.SetSizer(vbox)
        
    def On_Close(self, event):
        self.Destroy()
        
    def On_Okay(self, event, privateKey, bitcoinsPerShare):
        SendManyTransactions().prepareParams(privateKey, bitcoinsPerShare)
        
        self.EndModal( event.GetId() )