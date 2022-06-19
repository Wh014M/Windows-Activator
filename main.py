import os

# view license details
# os.system('cscript //nologo c:\windows\system32\slmgr.vbs /dlv')

# install kms client key
os.system('cscript //nologo c:\windows\system32\slmgr.vbs /ipk W269N-WFGWX-YVC9B-4J6C9-T83GX')

# connect to kms server
os.system('cscript //nologo c:\windows\system32\slmgr.vbs /skms s8.uk.to')

# Activate Windows 
os.system('cscript //nologo c:\windows\system32\slmgr.vbs /ato')

