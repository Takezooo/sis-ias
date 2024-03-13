from tkinter import *
from ttkbootstrap.constants import *
import ttkbootstrap as ttkb

#root
root = ttkb.Window(themename="darkly")
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
#update function
update_frame = ttkb.Frame(root, bootstyle="default")

systemTitle_Label = ttkb.Label(text="Student Information System", font=("Helvetica", 22), bootstyle="default")
systemTitle_Label.pack(pady=50)

#main menu section =================================================================
mainButtons_frame.pack(pady=20)

view_Button = ttkb.Button(mainButtons_frame, text="View Data", bootstyle="primary",
                            style="primary.TButton",
                            width=20)
view_Button.pack(pady=20)

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
                            width=20,
                            command=lambda:hideAndShow(mainButtons_frame, update_frame))
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
name_frame = ttkb.Frame(create_frame, bootstyle="default")
name_frame.pack(pady=5)
name_label = ttkb.Label(name_frame, text="Name:", font=("Helvetica", 12), bootstyle="default")
name_label.grid(row=0, column=0, padx=38, pady=5)
name_entry = ttkb.Entry(name_frame, font=("Helvetica", 10), bootstyle="default", width=30)
name_entry.grid(row=0, column=1, padx=37, pady=5)
#======================================

#BIRTHDATE ============================
birthdate_frame = ttkb.Frame(create_frame, bootstyle="default")
birthdate_frame.pack(pady=5)
birthdate_label = ttkb.Label(birthdate_frame, text="Birth Date:", font=("Helvetica", 12), bootstyle="default")
birthdate_label.grid(row=0, column=0, padx=20, pady=5)
birth_date = ttkb.DateEntry(birthdate_frame, bootstyle="primary", width=29)
birth_date.grid(row=0, column=1, padx=20, pady=5)
#======================================

#AGE LABEL ============================
age_label = ttkb.Label(birthdate_frame, text="Age: 99", font=("Helvetica", 12), bootstyle="default", width=8)
age_label.grid(row=1, column=0, padx=20, pady=10)
#======================================

#SEX ==================================
sex = ["Male", "Female"]
sex_frame = ttkb.Frame(create_frame, bootstyle="default")
sex_frame.pack(pady=5)
sex_label = ttkb.Label(sex_frame, text="Sex:", font=("Helvetica", 12), bootstyle="default")
sex_label.grid(row=0, column=0, padx=47, pady=5)
sex_combobox = ttkb.Combobox(sex_frame, font=("Helvetica", 10), bootstyle="default", 
                             values=sex, width=28)
sex_combobox.grid(row=0, column=1, padx=45, pady=5)
#======================================

#ADDRESS ==============================
address_frame = ttkb.Frame(create_frame, bootstyle="default")
address_frame.pack(pady=5)
address_label = ttkb.Label(address_frame, text="Address:", font=("Helvetica", 12), bootstyle="default")
address_label.grid(row=0, column=0, padx=27, pady=5)
address_entry = ttkb.Entry(address_frame, font=("Helvetica", 10), bootstyle="default", width=30)
address_entry.grid(row=0, column=1, padx=25, pady=5)
#======================================

#COURSE ===============================
course_frame = ttkb.Frame(create_frame, bootstyle="default")
course_frame.pack(pady=5)
course_label = ttkb.Label(course_frame, text="Course:", font=("Helvetica", 12), bootstyle="default")
course_label.grid(row=0, column=0, padx=33, pady=5)
course_entry = ttkb.Entry(course_frame, font=("Helvetica", 10), bootstyle="default", width=30)
course_entry.grid(row=0, column=1, padx=30, pady=5)
#======================================

#YEAR_LEVEL ===========================
yearLvl_frame = ttkb.Frame(create_frame, bootstyle="default")
yearLvl_frame.pack(pady=5)
yearLvl_label = ttkb.Label(yearLvl_frame, text="Year Level:", font=("Helvetica", 12), bootstyle="default")
yearLvl_label.grid(row=0, column=0, padx=18, pady=5)
yearLvl_entry = ttkb.Entry(yearLvl_frame, font=("Helvetica", 10), bootstyle="default", width=30)
yearLvl_entry.grid(row=0, column=1, padx=15, pady=5)
#======================================

# BUTTONS =============================
addButtons_frame = ttkb.Frame(create_frame, bootstyle="default")
addButtons_frame.pack(pady=30)
cancel_button = ttkb.Button(addButtons_frame, text="Cancel", bootstyle="warning",
                            width= 15,
                            command=lambda:hideAndShow(create_frame, mainButtons_frame))
cancel_button.grid(row=0, column=0, padx=18, pady=5)

save_button = ttkb.Button(addButtons_frame, text="Save", bootstyle="success",
                            width= 15,
                            command=lambda:hideAndShow(create_frame, mainButtons_frame))
save_button.grid(row=0, column=1, padx=18, pady=5)

#=====================================================================================

# Update Section =====================================================================

#STUDENT ID LABEL =====================
studentID_label = ttkb.Label(update_frame, text="", font=("Helvetica", 12), bootstyle="default")
studentID_label.pack()
#======================================

#NAME =================================
name_label = ttkb.Label(update_frame, text="Name:", font=("Helvetica", 12), bootstyle="default")
name_label.pack()
#======================================

#BIRTHDATE ============================
birthdate_label = ttkb.Label(update_frame, text="Birth Date:", font=("Helvetica", 12), bootstyle="default")
birthdate_label.pack()
birth_date = ttkb.DateEntry(update_frame, bootstyle="primary")
birth_date.pack()
#======================================

#AGE LABEL ============================
age_label = ttkb.Label(update_frame, text="Age:", font=("Helvetica", 12), bootstyle="default")
age_label.pack()
#======================================

#SEX ==================================
sex_label = ttkb.Label(update_frame, text="Sex:", font=("Helvetica", 12), bootstyle="default")
sex_label.pack()
#======================================

#ADDRESS ==============================
address_label = ttkb.Label(update_frame, text="Address:", font=("Helvetica", 12), bootstyle="default")
address_label.pack()
#======================================

#COURSE ===============================
course_label = ttkb.Label(update_frame, text="Course:", font=("Helvetica", 12), bootstyle="default")
course_label.pack()
#======================================

#YEAR_LEVEL ===========================
yearLvl_label = ttkb.Label(update_frame, text="Year Level:", font=("Helvetica", 12), bootstyle="default")
yearLvl_label.pack()
#======================================

cancel_button = ttkb.Button(update_frame, text="Cancel", bootstyle="warning",
                            width= 15,
                            command=lambda:hideAndShow(update_frame, mainButtons_frame))
cancel_button.pack(pady=20)

#=====================================================================================


#Functions
#hide and show toggle function
def hideAndShow(hidden, display): 
    hidden.pack_forget() 
    display.pack()
  

#run
root.mainloop()
