import tkinter as tk

root = tk.Tk()


# this is the title command..
root.title("-----------------------BANK-------------------------")
root.iconbitmap(r"C:\Users\Aditya Kumar\Downloads\icon.ico")

#now we use attribute for visibilty
# root.attributes('-alpha',0.7) # it range have only 0 to 1.

## change the background colour
# root.config(bg="red")
root['bg'] = "#3b253b"

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

# start with label and their position with pack()..

'''lab = tk.Label(root,text="BANK",font=("Times New Roman",50,"bold"),bg="#ADD8E6")
# lab.pack(padx=10,pady=1,ipadx=30,ipady=50,fill="x") # if we use expand=True -> grid open in center of the desktop
lab.pack(side="left")

lab1=tk.Label(root,text="WELCOME HERE ",font=("Times New Roman",50,"bold"),bg="#ADD8E6")
lab1.pack(side="left",padx=10)
'''
# now we use gride..



root.mainloop() ## by the help of this command you run the tkinter page
