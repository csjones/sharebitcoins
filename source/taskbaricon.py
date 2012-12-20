from sendmanytransactions import SendManyTransactions
from confirmtransaction import ConfirmTransaction
from createtransaction import CreateTransaction
from finisheddialog import FinishedDialog
from createbatch import CreateBatch
import os
import wx

#   http://stackoverflow.com/questions/6389580/quick-and-easy-trayicon-with-python
def create_menu_item(menu, label, func):
    item = wx.MenuItem(menu, -1, label)
    menu.Bind(wx.EVT_MENU, func, id=item.GetId())
    menu.AppendItem(item)
    return item

class TaskBarIcon(wx.TaskBarIcon):

    def __init__(self):
        super(TaskBarIcon, self).__init__()
        iconPath = os.path.expanduser('cube.png')
        self.set_icon(iconPath)
        
    def CreatePopupMenu(self):
        menu = wx.Menu()
        
        batchDirPath = os.path.dirname(os.path.abspath(__file__)) + '\\batches\\'
        
        if os.path.exists(batchDirPath):
            for path, dirs, files in os.walk(batchDirPath):
                for file in files:
                    fileName, extName = file.split('.')
                    create_menu_item(menu, fileName, self.on_run)
                    
                if files:
                    menu.AppendSeparator()
        
        create_menu_item(menu, 'Create Batch', self.on_create)
        menu.AppendSeparator()
        create_menu_item(menu, 'Exit', self.on_exit)
        return menu
        
    def set_icon(self, path):
        icon = wx.IconFromBitmap(wx.Bitmap(path))
        self.SetIcon(icon, 'Share Bitcoins')
        
    def on_create(self, event):
        tp = CreateBatch(None, title='Create Batch')
        tp.ShowModal()
        
    def on_run(self, event):
        newTransaction = SendManyTransactions()
        
        newTransaction.loadBatch( event.GetEventObject().GetLabelText( event.GetId() ) )
        
        createTX = CreateTransaction(None, title='Create Transaction')
        
        if createTX.ShowModal() == wx.ID_OK:
            createTX.Destroy()
            newTransaction.prepareBatch()
            
            confirmTX = ConfirmTransaction(None, title='Confirm Transaction')
            
            if confirmTX.ShowModal() == wx.ID_YES:
                confirmTX.Destroy()
                newTransaction.sendBatch()
                FinishedDialog(None, title='Finished').ShowModal()
                
        
    def on_exit(self, event):
        wx.CallAfter(self.Destroy)