from sendmanytransactions import SendManyTransactions
import webbrowser
import wx

#   http://www.zetcode.com/wxpython/dialogs/
class FinishedDialog(wx.Dialog):

    def __init__(self, *args, **kw):
        super(FinishedDialog, self).__init__(*args, **kw) 
        self.InitUI()
        self.SetSize((350, 125))
        self.SetTitle("Share Bitcoins")
        
    def InitUI(self):
        pnl = wx.Panel(self)
        
        sb = wx.StaticBox(pnl, label='Finished')
        sbs = wx.StaticBoxSizer(sb, orient=wx.VERTICAL)
        
        response = SendManyTransactions().getResponse()
        
        if 'error' in response:
            st0 = wx.StaticText(pnl,label=response['error'] )
            sbs.Add(st0, flag=wx.EXPAND, border=5)
        else:
            st0 = wx.StaticText(pnl,label=response['message'] )
            webbrowser.open('http://blockchain.info/tx/' + response['tx_hash'] )
            sbs.Add(st0, flag=wx.EXPAND, border=5)

        pnl.SetSizer(sbs)

        hbox2 = wx.BoxSizer(wx.HORIZONTAL)
        
        okButton = wx.Button(self, label='Ok')

        okButton.Bind(wx.EVT_BUTTON, self.On_Okay )
        
        hbox2.Add(okButton)

        vbox = wx.BoxSizer(wx.VERTICAL)
        vbox.Add(pnl, proportion=1, flag=wx.ALL|wx.EXPAND, border=5)
        vbox.Add(hbox2, flag=wx.ALIGN_CENTER|wx.TOP|wx.BOTTOM, border=10)

        self.SetSizer(vbox)
        
    def On_Okay(self, event):
        self.Destroy()