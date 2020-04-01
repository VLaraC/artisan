
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
        helpstr += "<b>" + u(QApplication.translate('HelpDlg','AUTOSAVE FIELDS',None)) + "</b>"
        tbl_Autosave = prettytable.PrettyTable()
        tbl_Autosave.field_names = [u(QApplication.translate('HelpDlg','Prefix Field',None)),u(QApplication.translate('HelpDlg','Source',None)),u(QApplication.translate('HelpDlg','Example',None))]
        tbl_Autosave.add_row([u(QApplication.translate('HelpDlg','~batchprefix',None)),u(QApplication.translate('HelpDlg','The batch prefix set in Config>Batch>Prefix',None)),u(QApplication.translate('HelpDlg','Prod-',None))])
        tbl_Autosave.add_row([u(QApplication.translate('HelpDlg','~batchcounter',None)),u(QApplication.translate('HelpDlg','The current batch number',None)),653])
        tbl_Autosave.add_row([u(QApplication.translate('HelpDlg','~batch',None)),u(QApplication.translate('HelpDlg','Same as "~batchprefix~batchnum"',None)),u(QApplication.translate('HelpDlg','Prod-653',None))])
        tbl_Autosave.add_row([u(QApplication.translate('HelpDlg','~batchposition',None)),u(QApplication.translate('HelpDlg','The current batch position, or "Roast of the Day"',None)),9])
        tbl_Autosave.add_row([u(QApplication.translate('HelpDlg','~batch_long',None)),u(QApplication.translate('HelpDlg','Same as Batch field in Roast Properties\n "~batchprefix~batchnum (~batchposition)"',None)),u(QApplication.translate('HelpDlg','Prod-653 (9)',None))])
        tbl_Autosave.add_row([u(QApplication.translate('HelpDlg','~title',None)),u(QApplication.translate('HelpDlg','From Roast>Properties>Title',None)),u(QApplication.translate('HelpDlg','Ethiopia Guji',None))])
        tbl_Autosave.add_row([u(QApplication.translate('HelpDlg','~beans',None)),u(QApplication.translate('HelpDlg','The first 30 characters of the first line \nFrom Roast>Properties>Beans',None)),u(QApplication.translate('HelpDlg','Ethiopia Guji purchased from R',None))])
        tbl_Autosave.add_row([u(QApplication.translate('HelpDlg','~beans_line',None)),u(QApplication.translate('HelpDlg','The entire first line From Roast>Properties>Beans',None)),u(QApplication.translate('HelpDlg','Ethiopia Guji purchased from Royal',None))])
        tbl_Autosave.add_row([u(QApplication.translate('HelpDlg','~date',None)),u(QApplication.translate('HelpDlg','Roast date in format yy-MM-dd',None)),u(QApplication.translate('HelpDlg','20-02-05',None))])
        tbl_Autosave.add_row([u(QApplication.translate('HelpDlg','~date_long',None)),u(QApplication.translate('HelpDlg','Roast date in format yyyy-MM-dd',None)),u(QApplication.translate('HelpDlg','2020-02-05',None))])
        tbl_Autosave.add_row([u(QApplication.translate('HelpDlg','~time',None)),u(QApplication.translate('HelpDlg','Roast time in format hhmm',None)),1742])
        tbl_Autosave.add_row([u(QApplication.translate('HelpDlg','~datetime',None)),u(QApplication.translate('HelpDlg','Roast date and time in format yy-MM-dd_hhmm',None)),u(QApplication.translate('HelpDlg','20-02-05_1742',None))])
        tbl_Autosave.add_row([u(QApplication.translate('HelpDlg','~datetime_long',None)),u(QApplication.translate('HelpDlg','Roast date and time in format yyyy-MM-dd_hhmm',None)),u(QApplication.translate('HelpDlg','2020-02-05_1742',None))])
        tbl_Autosave.add_row([u(QApplication.translate('HelpDlg','~operator',None)),u(QApplication.translate('HelpDlg','From Roast>Properties>Operator',None)),u(QApplication.translate('HelpDlg','Dave',None))])
        tbl_Autosave.add_row([u(QApplication.translate('HelpDlg','~weight',None)),u(QApplication.translate('HelpDlg','From Roast>Properties>Weight Green',None)),3])
        tbl_Autosave.add_row([u(QApplication.translate('HelpDlg','~weightunits',None)),u(QApplication.translate('HelpDlg','From Roast>Properties>Weight',None)),u(QApplication.translate('HelpDlg','Kg',None))])
        tbl_Autosave.add_row([u(QApplication.translate('HelpDlg','~volume',None)),u(QApplication.translate('HelpDlg','From Roast>Properties>Volume Green',None)),4.1])
        tbl_Autosave.add_row([u(QApplication.translate('HelpDlg','~volumeunits',None)),u(QApplication.translate('HelpDlg','From Roast>Properties>Volume',None)),u(QApplication.translate('HelpDlg','l',None))])
        tbl_Autosave.add_row([u(QApplication.translate('HelpDlg','~density',None)),u(QApplication.translate('HelpDlg','From Roast>Properties>Density Green',None)),756.4])
        tbl_Autosave.add_row([u(QApplication.translate('HelpDlg','~densityunits',None)),u(QApplication.translate('HelpDlg','From Roast>Properties>Density',None)),u(QApplication.translate('HelpDlg','g_l',None))])
        tbl_Autosave.add_row([u(QApplication.translate('HelpDlg','~moisture',None)),u(QApplication.translate('HelpDlg','From Roast>Properties>Moisture Green',None)),11.7])
        tbl_Autosave.add_row([u(QApplication.translate('HelpDlg','~moisturetunits',None)),u(QApplication.translate('HelpDlg','From Roast>Properties>Moisture',None)),u(QApplication.translate('HelpDlg','pct',None))])
        tbl_Autosave.add_row([u(QApplication.translate('HelpDlg','~machine',None)),u(QApplication.translate('HelpDlg','From Roast>Properties>Machine',None)),u(QApplication.translate('HelpDlg','SF-6',None))])
        tbl_Autosave.add_row([u(QApplication.translate('HelpDlg','~drumspeed',None)),u(QApplication.translate('HelpDlg','From Roast>Properties>Drum Speed',None)),64])
        helpstr += tbl_Autosave.get_html_string(attributes={"width":"100%","border":"1","padding":"1","border-collapse":"collapse"})
        helpstr += "</body>"
        helpstr = re.sub(r"&amp;#160;", r"&#160;",helpstr)

        # autogenerated help pasted above

# ----- Cut above ---------------------------------------------
outfile = open('../output_files/autosave.html','w')
outfile.write(helpstr)
outfile.close()
outfile = open('../output_files/help.html','w')
outfile.write(helpstr)
outfile.close()