import tkinter as tk

root = tk.Tk()


# this is the title command..
root.title("-----------------------BANK-------------------------")
root.iconbitmap(r"C:\Users\Aditya Kumar\Downloads\icon.ico")

#now we use attribute for visibilty
# root.attributes('-alpha',0.7) # it range have only 0 to 1.

## change the background colour
# root.config(bg="red")
# root['bg'] = "#3b253b"
root.config(bg="light blue")

# root.geometry("500x400-150-150") # by this you can resize the gui interface and set point where you want to view the Interface

# for set the position on center of system of GUI interface.
'''width=300
height=400

sys_width = root.winfo_screenwidth()
sys_height = root.winfo_screenheight()

c_x = int(sys_width/2-width/2)
c_y = int(sys_height/2-height/2)

root.geometry(f"{width}x{height}+{c_x}+{c_y}")'''

#min and max size..

'''root.minsize(300,300)
root.maxsize(700,700)'''

# resizeable of gui interface

'''root.geometry("600x500")
root.resizable(False,False)''' # by this you can't resize the gui interface.


# LAYOUT MANAGEMENT.....
# start with label and their position with pack()..

'''lab = tk.Label(root,text="BANK",font=("Times New Roman",50,"bold"),bg="#ADD8E6")
# lab.pack(padx=10,pady=1,ipadx=30,ipady=50,fill="x") # if we use expand=True -> grid open in center of the desktop
lab.pack(side="left")

lab1=tk.Label(root,text="WELCOME HERE ",font=("Times New Roman",50,"bold"),bg="#ADD8E6")
lab1.pack(side="left",padx=10)
'''
# now we use gride..

'''lab=tk.Label(root,text="Hello world",font=("Times New Roman",40,"bold"),bg="red")
lab.grid(row=0,column=0,padx=50,pady=80)

lab1=tk.Label(root,text="Nice to meet you",font=("Times New Roman",40,"bold"),bg="Yellow")
lab1.grid(row=0,column=2,columnspan=3) # columnspan means increase the size of Area of column..'''

# now we use place()..

'''lab=tk.Label(root,text="Good Morning",font=("Times New Roman",30,"bold"),bg="White")
lab.place(x=30,y=25, height=100,width=350)

lab1=tk.Label(root,text="Happy Day",font=("Arial",25,"italic"),bg="Gold")
lab1.place(x=245,y=250)  #relx -> relative x and rely-> relative y..'''

# variables in tkinter
"""
Tkinter Variable	Python Equivalent	Used For
StringVar()	        str	Text values (e.g. Entry, Label)
IntVar()	        int	Whole numbers (e.g. Radiobuttons)
DoubleVar()	        float	Decimal numbers
BooleanVar()	    bool	True / False values (Checkboxes)

for access of this variable we have to use 
get(),getvar() method | set(), setvar() method

"""

'''
var1=tk.StringVar(root,value="Aditya Kumar")
var2=tk.IntVar(root,value=12344)
var3=tk.DoubleVar(root,value=243.23)
var4=tk.BooleanVar(root,value=True)
var5=tk.StringVar(root,name="2")
var5.set("Good Morning")
print(var5.get())
print(var1.get())
print(var2.get())
print(var3.get())
print(var4.get())'''


# learn more of label..
# entry=input("Enter the Something : ")
# var=tk.StringVar()
'''lab=tk.Label(
    root,
    text="Python \nDeveloper", # this is static text
    # textvariable=var, # this is dynamic text you can change the at run time.

    font=("Arial",40,"bold"),bg="white",fg="black",
    cursor="hand2",
    relief="ridge", # you can use "flat","raised","sunken","groove","solid".
    justify="center",  # it means hows your text alingment.
    width=10,
    height=4,
    # underline=3,
)
lab.place(x=500,y=10)
# var.set(entry)'''

# image setup...

# from PIL import Image,ImageTk  ## this pillow library for display the jpg images because tkinter support only png ,ioc images. 
# image=Image.open(r"C:\Users\Aditya Kumar\Desktop\my file\Python-Tkinter\tkinter\cafepic.JPG")
# photo = ImageTk.PhotoImage(image)

'''lab=tk.Label( 
    root,
    image=photo,
    bg="light blue",
    text="Profile",
    font=("Arial",20,"bold"),
    fg="black",
    compound="top"
)

lab.place(x=100,y=100)'''


# label with frame..

'''label_frame=tk.LabelFrame(
    root,
    text="Aditya",
    font=("Arial",30),
    # labelanchor="n",
    bg="light blue"

)
label_frame.place(x=150,y=150, height=100,width=400)

lab1=tk.Label(
    root,
    text="I am Python developer",
    font=("Times Now Roman",20,"italic"),
    bg="light blue",
    fg="brown"
)
lab1.place(x=200,y=200)'''


# button setup........

def python():
    lb1.config(text="Aditya Kumar")

bt=tk.Button(
    root,
    text="ON",
    font=(10),
    bg="green",
    cursor="hand2",
    command=python
)
bt.place(x=200,y=200)

lb1=tk.Label(
    root,
    text="Hello",
    font=("Arial",20,"italic"),
    bg="light green",
    relief="sunken"
)
lb1.place(x=300,y=200)


root.mainloop() ## by the help of this command you run the tkinter page
