from tkinter import *
from ttkbootstrap.constants import *
import ttkbootstrap as ttkb

#root
root = ttkb.Window(themename="vapor")
root.title("Student Information System")
root.geometry("800x700")

#Style
style = ttkb.Style()
style.configure("primary.TButton", font=("Helvetica", 16))


systemTitle_Label = ttkb.Label(text="Student Information System", font=("Helvetica", 22), bootstyle="default")
systemTitle_Label.pack(pady=90)

add_Button = ttkb.Button(text="Create", bootstyle="primary",
                         style="primary.TButton",
                         width=20)
add_Button.pack(pady=20)
search_Button = ttkb.Button(text="Search", bootstyle="primary",
                            style="primary.TButton",
                            width=20)
search_Button.pack(pady=20)
update_Button = ttkb.Button(text="Update", bootstyle="primary",
                            style="primary.TButton",
                            width=20)
update_Button.pack(pady=20)
delete_Button = ttkb.Button(text="Delete", bootstyle="primary",
                            style="primary.TButton",
                            width=20)
delete_Button.pack(pady=20)




def hide_button(widget): 
    # This will remove the widget from toplevel 
    widget.pack_forget() 
  
  
# Method to make Button(widget) visible 
def show_button(widget): 
    # This will recover the widget from toplevel 
    widget.pack() 


root.mainloop()
