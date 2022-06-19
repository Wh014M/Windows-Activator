import ctypes, os

# Function to check if the application is running as an Administrator
def isAdmin():
    try:
        is_admin = (os.getuid() == 0)
    except AttributeError:
        is_admin = ctypes.windll.shell32.IsUserAnAdmin() != 0
    return is_admin

if isAdmin():
    print("Windows Activator By Padsala Tushal")
else:
    print("Run the program as Administrator!!")
    exit()

# view license details
# os.system('cscript //nologo c:\windows\system32\slmgr.vbs /dlv')

# KMS Client Key
Home = 'TX9XD-98N7V-6WMQ6-BX7FG-H8Q99'
Home_N = '3KHY7-WNT83-DGQKR-F7HPR-844BM'
Home_Single_Language = '7HNRX-D7KGG-3K4RQ-4WPJ4-YTDFH'
Professional = 'W269N-WFGWX-YVC9B-4J6C9-T83GX'
Professional_N = 'MH37W-N47XK-V7XM9-C7227-GCQG9'
Education = 'NW6C2-QMPVW-D7KKK-3GKT6-VCFB2'
Education_N = '2WH4N-8QGBV-H22JP-CT43Q-MDWWJ'
Enterprise = 'NPPR9-FWDCX-D2C8J-H872K-2YT43'
Enterprise_N = 'DPH2V-TTNVB-4X9Q3-TJR4H-KHJW4'

print(" 1 : Home Edition \n","2 : Home N Edition \n","3 : Home Single Language Edition \n","4 : Professional Edition \n","5 : Professional N Edition \n","6 : Education Edition \n","7 : Education N Edition \n","8 : Enterprise Edition \n","9 : Enterprise N Edition \n")

choice = int(input('Enter your choice:'))
if (choice == 1):
    edition = Home
elif (choice == 2):
    edition = Home_N
elif (choice == 3):
    edition = Home_Single_Language
elif (choice == 4):
    edition = Professional
elif (choice == 5):
    edition = Professional_N
elif (choice == 6):
    edition = Education
elif (choice == 7):
    edition = Education_N
elif (choice == 8):
    edition = Enterprise
elif (choice == 9):
    edition = Enterprise_N
else:
    print('Invalid choice')
    exit()


# install kms client key
os.system(f'cscript //nologo c:\windows\system32\slmgr.vbs /ipk {edition}')


# Try to connect to kms server 1
os.system('cscript //nologo c:\windows\system32\slmgr.vbs /skms s8.uk.to')
a = os.system('cscript //nologo c:\windows\system32\slmgr.vbs /ato')

# If first kms server is not working then try to connect to second kms server
if (a != 0):
    os.system(f'cscript //nologo c:\windows\system32\slmgr.vbs /skms s9.us.to')
    os.system('cscript //nologo c:\windows\system32\slmgr.vbs /ato')
