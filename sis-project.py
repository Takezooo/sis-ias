from tkinter import *
from datetime import date
from ttkbootstrap.constants import *
import ttkbootstrap as ttkb

#root
root = ttkb.Window(themename="darkly")
root.title("Student Information System")
root.geometry("800x750")

#Style
#for main menu/ home
style = ttkb.Style()
style.configure("primary.TButton", font=("Helvetica", 16))
style.configure("update.primary.TButton", font=("Helvetica",10))

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
birth_date = ttkb.DateEntry(birthdate_frame, bootstyle="primary", width=29, startdate=date(2023, 3, 1))
birth_date.grid(row=0, column=1, padx=20, pady=5)
#======================================

#AGE LABEL ============================
age_label = ttkb.Label(birthdate_frame, text="Age: ", font=("Helvetica", 12), bootstyle="default", width=8)
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
back_button = ttkb.Button(addButtons_frame, text="Back", bootstyle="warning",
                            width= 15,
                            command=lambda:hideAndShow(create_frame, mainButtons_frame))
back_button.grid(row=0, column=0, padx=18, pady=5)

save_button = ttkb.Button(addButtons_frame, text="Save", bootstyle="success",
                            width= 15,
                            command=lambda:addConfirmation_popup())
save_button.grid(row=0, column=1, padx=18, pady=5)

#=====================================================================================

# Update Section =====================================================================

#SEARCH STUDENT ID LABEL ==============
studentIdUpt_frame = ttkb.Frame(update_frame, bootstyle="default")
studentIdUpt_frame.config( width=700, height=50 )
studentIdUpt_frame.pack(pady=15)
studentIdUpt_label = ttkb.Label(studentIdUpt_frame, text="Student ID: ", font=("Helvetica", 12), bootstyle="default")
studentIdUpt_label.place(x=135, y=0)
studentIdUpt_entry = ttkb.Entry(studentIdUpt_frame, font=("Helvetica", 10), bootstyle="default", width=18)
studentIdUpt_entry.place(x=277, y=0)
studentIdUpt_button = ttkb.Button(studentIdUpt_frame, text="Search", width= 7,
                                  bootstyle="primary",
                                  style="update.primary.TButton")
studentIdUpt_button.place(x=475, y=0)
#======================================

#NAME =================================
nameUpt_frame = ttkb.Frame(update_frame, bootstyle="default")
nameUpt_frame.pack(pady=5)
nameUpt_label = ttkb.Label(nameUpt_frame, text="Name:", font=("Helvetica", 12), bootstyle="default")
nameUpt_label.grid(row=0, column=0, padx=38, pady=5)
nameUpt_entry = ttkb.Entry(nameUpt_frame, font=("Helvetica", 10), bootstyle="default", width=30)
nameUpt_entry.grid(row=0, column=1, padx=37, pady=5)
#======================================

#BIRTHDATE ============================
birthdateUpt_frame = ttkb.Frame(update_frame, bootstyle="default")
birthdateUpt_frame.pack(pady=5)
birthdateUpt_label = ttkb.Label(birthdateUpt_frame, text="Birth Date:", font=("Helvetica", 12), bootstyle="default")
birthdateUpt_label.grid(row=0, column=0, padx=20, pady=5)
birthUpt_date = ttkb.DateEntry(birthdateUpt_frame, bootstyle="primary", width=29)
birthUpt_date.grid(row=0, column=1, padx=20, pady=5)
#======================================

#AGE LABEL ============================
age_labelUpt = ttkb.Label(birthdateUpt_frame, text="Age: ", font=("Helvetica", 12), bootstyle="default", width=8)
age_labelUpt.grid(row=1, column=0, padx=20, pady=10)
#======================================

#SEX ==================================
sexUpt_frame = ttkb.Frame(update_frame, bootstyle="default")
sexUpt_frame.pack(pady=5)
sexUpt_label = ttkb.Label(sexUpt_frame, text="Sex:", font=("Helvetica", 12), bootstyle="default")
sexUpt_label.grid(row=0, column=0, padx=47, pady=5)
sexUpt_combobox = ttkb.Combobox(sexUpt_frame, font=("Helvetica", 10), bootstyle="default", 
                             values=sex, width=28)
sexUpt_combobox.grid(row=0, column=1, padx=45, pady=5)
#======================================

#ADDRESS ==============================
addressUpt_frame = ttkb.Frame(update_frame, bootstyle="default")
addressUpt_frame.pack(pady=5)
addressUpt_label = ttkb.Label(addressUpt_frame, text="Address:", font=("Helvetica", 12), bootstyle="default")
addressUpt_label.grid(row=0, column=0, padx=27, pady=5)
addressUpt_entry = ttkb.Entry(addressUpt_frame, font=("Helvetica", 10), bootstyle="default", width=30)
addressUpt_entry.grid(row=0, column=1, padx=25, pady=5)
#======================================

#COURSE ===============================
courseUpt_frame = ttkb.Frame(update_frame, bootstyle="default")
courseUpt_frame.pack(pady=5)
courseUpt_label = ttkb.Label(courseUpt_frame, text="Course:", font=("Helvetica", 12), bootstyle="default")
courseUpt_label.grid(row=0, column=0, padx=33, pady=5)
courseUpt_entry = ttkb.Entry(courseUpt_frame, font=("Helvetica", 10), bootstyle="default", width=30)
courseUpt_entry.grid(row=0, column=1, padx=30, pady=5)
#======================================

#YEAR_LEVEL ===========================
yearLvlUpt_frame = ttkb.Frame(update_frame, bootstyle="default")
yearLvlUpt_frame.pack(pady=5)
yearLvlUpt_label = ttkb.Label(yearLvlUpt_frame, text="Year Level:", font=("Helvetica", 12), bootstyle="default")
yearLvlUpt_label.grid(row=0, column=0, padx=18, pady=5)
yearLvlUpt_entry = ttkb.Entry(yearLvlUpt_frame, font=("Helvetica", 10), bootstyle="default", width=30)
yearLvlUpt_entry.grid(row=0, column=1, padx=15, pady=5)
#======================================

# BUTTONS =============================
updateButtons_frame = ttkb.Frame(update_frame, bootstyle="default")
updateButtons_frame.pack(pady=30)
backUpt_button = ttkb.Button(updateButtons_frame, text="Cancel", bootstyle="warning",
                            width= 15,
                            command=lambda:hideAndShow(update_frame, mainButtons_frame))
backUpt_button.grid(row=0, column=0, padx=18, pady=5)

saveUpt_button = ttkb.Button(updateButtons_frame, text="Save", bootstyle="success",
                            width= 15,
                            command=lambda:hideAndShow(update_frame, mainButtons_frame))
saveUpt_button.grid(row=0, column=1, padx=18, pady=5)

#=====================================================================================


#Functions
#hide and show toggle function
def hideAndShow(hidden, display): 
    hidden.pack_forget() 
    display.pack()

def closeWindow(window):
    window.destroy()

def continueAddWindow(hidden, display, text):
    hidden.pack_forget()
    display.pack()
    text.config(text=f"Student Data Saved", bootstyle="success")


#add function
def addStudent():
    #auto compute age ========================================
    birthdate = str(birth_date.entry.get())
    day_str, month_str, year_str = birthdate.split("/")
    day = int(day_str)
    month = int(month_str)
    year = int(year_str)
    today = date.today()
    age = today.year - year - ((today.month, today.day) < (month, day))
    age_label.config(text=f"Age: {age}")
    # ========================================================

# create confirmation function
def addConfirmation_popup():

    addStudent()

    addTop= Toplevel(create_frame)
    addTop.geometry("350x250")
    addTop.title("Confirmation Window")
    addTop.resizable(False,False)

    addConfirmationLabel = ttkb.Label(addTop, text="Do you want to add this student?", font=("Helvetica", 12), bootstyle="default")
    addConfirmationLabel.pack(pady=60)

    addConfirmationButtons_frame = ttkb.Frame(addTop, bootstyle="default")
    addConfirmationButtons_frame.pack(pady=10)

    addConfirmNo_button = ttkb.Button(addConfirmationButtons_frame, text="No", bootstyle="warning",
                                width= 10,
                                command=lambda:closeWindow(addTop))
    addConfirmNo_button.grid(row=0, column=0, padx=18, pady=5)

    addConfirmYes_button = ttkb.Button(addConfirmationButtons_frame, text="Yes", bootstyle="success",
                                    width= 10,
                                command=lambda:continueAddWindow(addConfirmationButtons_frame, addContinuation_button, addConfirmationLabel))
    addConfirmYes_button.grid(row=0, column=1, padx=18, pady=5)

    addContinuation_button = ttkb.Button(addTop, text="Ok", bootstyle="success",
                                width= 10,
                                command=lambda:closeWindow(addTop))
    
#run
root.mainloop()



