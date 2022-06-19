from tkinter import *

root = Tk()

root.geometry('500x400')
root.minsize(450,300)
# root.maxsize(700, 400)

root.title('Windows activator by Padsala Tushal')


def sel():
   edition = var.get()
   print(edition)



var = StringVar()
R1 = Radiobutton(root, text="Home", variable=var, value='TX9XD-98N7V-6WMQ6-BX7FG-H8Q99',
                  command=sel)
R1.pack( anchor = W )

R2 = Radiobutton(root, text="Home N", variable=var, value='3KHY7-WNT83-DGQKR-F7HPR-844BM',
                  command=sel)
R2.pack( anchor = W )

R3 = Radiobutton(root, text="Home Single Language", variable=var, value='7HNRX-D7KGG-3K4RQ-4WPJ4-YTDFH',
                  command=sel)
R3.pack( anchor = W)

R4 = Radiobutton(root, text="Professional", variable=var, value='W269N-WFGWX-YVC9B-4J6C9-T83GX',
                  command=sel)
R4.pack( anchor = W)

R5 = Radiobutton(root, text="Professional N", variable=var, value='MH37W-N47XK-V7XM9-C7227-GCQG9',
                  command=sel)
R5.pack( anchor = W)

R6 = Radiobutton(root, text="Education", variable=var, value='NW6C2-QMPVW-D7KKK-3GKT6-VCFB2',
                  command=sel)
R6.pack( anchor = W)

R7 = Radiobutton(root, text="Education N", variable=var, value='2WH4N-8QGBV-H22JP-CT43Q-MDWWJ',
                  command=sel)
R7.pack( anchor = W)

R8 = Radiobutton(root, text="Enterprise", variable=var, value='NPPR9-FWDCX-D2C8J-H872K-2YT43',
                  command=sel)
R8.pack( anchor = W)

R9 = Radiobutton(root, text="Enterprise N", variable=var, value='DPH2V-TTNVB-4X9Q3-TJR4H-KHJW4',
                  command=sel)
R9.pack( anchor = W)







label = Label(root)
label.pack()

root.mainloop()
