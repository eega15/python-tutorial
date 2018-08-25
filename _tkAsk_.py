#_tkAsk_.py#
#18 08 25#
#
from Tkinter import *

import Tkinter, Tkconstants, tkFileDialog

#
import os

#
def _tkAskFile( _initialdir = os.sep,
                   _title = 'Select File',
                   _filetypes = (("all files","*.*"),
                                ("srt...","*.srt"),
                                ("py...","*.py"),
                                ("au3...","*.au3"),
                                ("db...","*.db"),
                                ("txt...","*.txt"),
                                ("pdf...","*.pdf")
                                )):
    root = Tk()
    _ret = tkFileDialog.askopenfilename( initialdir = _initialdir,
                    title = _title,
                    filetypes = _filetypes)
    root.destroy()
    _ret = _ret.replace( '\\', os.sep ).replace( '/', os.sep )
    return _ret


#
def _tkAskDirectory():
    root = Tk()
    _ret = tkFileDialog.askdirectory()
    root.destroy()
    _ret = _ret.replace( '\\', os.sep ).replace( '/', os.sep )
    return _ret


#
if __name__ == '__main__':
    #
    print( os.sep )
    print( os.getcwd() )
    print(_tkAskDirectory())
    print(_tkAskFile( _initialdir = os.getcwd() ))