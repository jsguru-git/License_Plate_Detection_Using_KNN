:: This batch cmd is run as the final step in the installation of PAGE
:: It creates the file winpage.bat

@ECHO OFF

SET location=%*

SET  "command=start /min wish.exe  "%location%\page.tcl" %%1"

@ECHO %command%>winpage.bat
