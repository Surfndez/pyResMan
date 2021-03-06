# -*- coding:utf8 -*-

'''
Created on 2017-3-28

@author: javacardos@gmail.com
@organization: https://www.javacardos.com/
@copyright: JavaCardOS Technologies. All rights reserved.
'''

import wx
from pyResMan.Dialogs.pyResManDialog import pyResManDialog

class App(wx.App):
    '''
    The main application class;
    '''
    def OnInit(self):
        '''
        Called when application initialize;
        '''
        
        # Display the main dialog;
        dlg = pyResManDialog(None)
        dlg.ShowModal()
        dlg.Bind(wx.EVT_CLOSE, self.OnDialogClose())
        return True

    def OnDialogClose(self):
        '''
        Dialog close event handler;
        '''
        
        # Exit the app;
        wx.Exit()

# Create application instance;
app=App()
app.MainLoop()
