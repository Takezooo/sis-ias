from tkinter import *
from ttkbootstrap.constants import *
import ttkbootstrap as ttkb

#root
root = ttkb.Window(themename="vapor")
root.title("Student Information System")
root.geometry("800x700")

#Style
#for main menu/ home
style = ttkb.Style()
style.configure("primary.TButton", font=("Helvetica", 16))

#Frames
#menu buttons
mainButtons_frame = ttkb.Frame(root, bootstyle="default")
#add/create function
create_frame = ttkb.Frame(root, bootstyle="default")

systemTitle_Label = ttkb.Label(text="Student Information System", font=("Helvetica", 22), bootstyle="default")
systemTitle_Label.pack(pady=50)

#main menu section =================================================================
mainButtons_frame.pack(pady=20)

add_Button = ttkb.Button(mainButtons_frame, text="Create", bootstyle="primary",
                         style="primary.TButton",
                         width=20,
                         command=lambda:hideAndShow(mainButtons_frame, create_frame))
add_Button.pack(pady=20)
search_Button = ttkb.Button(mainButtons_frame, text="Search", bootstyle="primary",
                            style="primary.TButton",
                            width=20)
search_Button.pack(pady=20)
update_Button = ttkb.Button(mainButtons_frame, text="Update", bootstyle="primary",
                            style="primary.TButton",
                            width=20)
update_Button.pack(pady=20)
delete_Button = ttkb.Button(mainButtons_frame, text="Delete", bootstyle="primary",
                            style="primary.TButton",
                            width=20)
delete_Button.pack(pady=20)
#=====================================================================================

# Create Section =====================================================================

#STUDENT ID LABEL =====================
studentID_label = ttkb.Label(create_frame, text="", font=("Helvetica", 12), bootstyle="default")
studentID_label.pack()
#======================================

#NAME =================================
name_label = ttkb.Label(create_frame, text="Name:", font=("Helvetica", 12), bootstyle="default")
name_label.pack()
#======================================

#BIRTHDATE ============================
birthdate_label = ttkb.Label(create_frame, text="Birth Date:", font=("Helvetica", 12), bootstyle="default")
birthdate_label.pack()
birth_date = ttkb.DateEntry(create_frame, bootstyle="primary")
birth_date.pack()
#======================================

#AGE LABEL ============================
age_label = ttkb.Label(create_frame, text="Age:", font=("Helvetica", 12), bootstyle="default")
age_label.pack()
#======================================

#SEX ==================================
sex_label = ttkb.Label(create_frame, text="Sex:", font=("Helvetica", 12), bootstyle="default")
sex_label.pack()
#======================================

#ADDRESS ==============================
address_label = ttkb.Label(create_frame, text="Address:", font=("Helvetica", 12), bootstyle="default")
address_label.pack()
#======================================

#COURSE ===============================
course_label = ttkb.Label(create_frame, text="Course:", font=("Helvetica", 12), bootstyle="default")
course_label.pack()
#======================================

#YEAR_LEVEL ===========================
yearLvl_label = ttkb.Label(create_frame, text="Year Level:", font=("Helvetica", 12), bootstyle="default")
yearLvl_label.pack()
#======================================

cancel_button = ttkb.Button(create_frame, text="Cancel", bootstyle="warning",
                            width= 15,
                            command=lambda:hideAndShow(create_frame, mainButtons_frame))
cancel_button.pack(pady=20)

#=====================================================================================

#Functions
#hide and show toggle function
def hideAndShow(hidden, display): 
    hidden.pack_forget() 
    display.pack()
  

#run
root.mainloop()
