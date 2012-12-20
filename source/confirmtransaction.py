from sendmanytransactions import SendManyTransactions
import wx

#   http://www.zetcode.com/wxpython/dialogs/
class ConfirmTransaction(wx.Dialog):

    def __init__(self, *args, **kw):
        super(ConfirmTransaction, self).__init__(*args, **kw) 
        self.InitUI()
        self.SetSize((200, 175))
        self.SetTitle("Share Bitcoins")
        
    def InitUI(self):
        pnl = wx.Panel(self)
        
        tx = SendManyTransactions()
        
        st0 = wx.StaticText(pnl,label="Bitcoins Per Share: %s" % str( "%.8f" % tx.getBitcoinsPerShare() ) )
        st1 = wx.StaticText(pnl,label="Total Shares: %s" % str( tx.getTotalShares() ) )
        st2 = wx.StaticText(pnl,label="Total Bitcoins: %s" % str( "%.8f" % tx.getTotalBitcoins() ) )
        st3 = wx.StaticText(pnl,label="\nAre you sure?")
        
        sb = wx.StaticBox(pnl, label='Confirm Transaction')
        sbs = wx.StaticBoxSizer(sb, orient=wx.VERTICAL)
        sbs.Add(st0, flag=wx.LEFT, border=5)
        sbs.Add(st1, flag=wx.LEFT, border=5)
        sbs.Add(st2, flag=wx.LEFT, border=5)
        sbs.Add(st3, flag=wx.LEFT, border=5)

        pnl.SetSizer(sbs)

        hbox2 = wx.BoxSizer(wx.HORIZONTAL)
        
        okButton = wx.Button(self, wx.ID_YES)
        okButton.Bind(wx.EVT_BUTTON, self.On_Yes )
        
        closeButton = wx.Button(self, wx.ID_NO)
        closeButton.Bind(wx.EVT_BUTTON, self.On_No)
        
        hbox2.Add(okButton)
        hbox2.Add(closeButton, flag=wx.LEFT, border=5)

        vbox = wx.BoxSizer(wx.VERTICAL)
        vbox.Add(pnl, proportion=1, flag=wx.ALL|wx.EXPAND, border=5)
        vbox.Add(hbox2, flag=wx.ALIGN_CENTER|wx.TOP|wx.BOTTOM, border=10)

        self.SetSizer(vbox)
        
    def On_No(self, event):
        self.Destroy()
        
    def On_Yes(self, event):
        self.EndModal( event.GetId() )