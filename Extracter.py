import os
import socket

cmd = ('xcopy C:\\Program_Files\\services '+os.getcwd()+'\\Host_'+socket.gethostname()+' /I /Y')
os.system(cmd)
os.system('rmdir C:\\Program_Files\\services /S /Q')
os.system('md C:\\Program_Files\\services')
    
