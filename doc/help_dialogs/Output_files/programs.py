
import prettytable
import re
from PyQt5.QtWidgets import QApplication
def u(x):
    return str(x)
if True:  #here just to achieve the indent
    if True:
# ----- Cut below ---------------------------------------------

        # autogenerated help pasted below

        newline = "\n"  #@UnusedVariable
        helpstr = ""
        helpstr += "<head><style>"
        helpstr += "td, th {border: 1px solid #ddd;  padding: 6px;}"
        helpstr += "th {padding-top: 6px;padding-bottom: 6px;text-align: left;background-color: #0C6AA6; color: white;}"
        helpstr += "</style></head>"
        helpstr += "<body>"
        helpstr += "<b>" + u(QApplication.translate('HelpDlg','EXTERNAL PROGRAMS',None)) + "</b>"
        tbl_Programstop = prettytable.PrettyTable()
        tbl_Programstop.header = False
        tbl_Programstop.add_row([u(QApplication.translate('HelpDlg','Allows to link to external programs that print temperature when called',None))+newline+u(QApplication.translate('HelpDlg','',None))+newline+u(QApplication.translate('HelpDlg','The output of the program must be to Stdout (like when using print statements)',None))+newline+u(QApplication.translate('HelpDlg','',None))+newline+u(QApplication.translate('HelpDlg','this allo ws to connect meters that use any programming language',None))+newline+u(QApplication.translate('HelpDlg','',None))+newline+u(QApplication.translate('HelpDlg','Example of output needed from program for single temperature (BT)',None))+newline+u(QApplication.translate('HelpDlg','',None))+newline+u(QApplication.translate('HelpDlg','"100.4" (note: "" not needed)',None))+newline+u(QApplication.translate('HelpDlg','',None))+newline+u(QApplication.translate('HelpDlg','Example of output needed from program for double temperature (ET,BT)',None))+newline+u(QApplication.translate('HelpDlg','',None))+newline+u(QApplication.translate('HelpDlg','"200.4,100.4" (note: temperatures are separated by a comma "ET,BT")',None))])
        helpstr += tbl_Programstop.get_html_string(attributes={"width":"100%","border":"1","padding":"1","border-collapse":"collapse"})
        tbl_Programsbottom = prettytable.PrettyTable()
        tbl_Programsbottom.header = False
        tbl_Programsbottom.add_row([u(QApplication.translate('HelpDlg','Example of a file written in python language called test.py:',None))+newline+u(QApplication.translate('HelpDlg','#comment: print a string with two numbers separated by a comma',None))+newline+u(QApplication.translate('HelpDlg','',None))+newline+u(QApplication.translate('HelpDlg','#!/usr/bin/env python',None))+newline+u(QApplication.translate('HelpDlg','print ("237.1,100.4")',None))])
        helpstr += tbl_Programsbottom.get_html_string(attributes={"width":"100%","border":"1","padding":"1","border-collapse":"collapse"})
        helpstr += "</body>"
        helpstr = re.sub(r"&amp;#160;", r"&#160;",helpstr)

        # autogenerated help pasted above

# ----- Cut above ---------------------------------------------
outfile = open('../output_files/programs.html','w')
outfile.write(helpstr)
outfile.close()
outfile = open('../output_files/help.html','w')
outfile.write(helpstr)
outfile.close()