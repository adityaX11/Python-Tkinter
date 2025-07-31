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

root.geometry("500x400-150-150") # by this you can resize the gui interface and set point where you want to view the Interface

# for set the position on center of system of GUI interface.
width=300
height=400

sys_width = root.win


root.mainloop() ## by the help of this command you run the tkinter page
