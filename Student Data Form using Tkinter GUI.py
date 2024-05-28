from tkinter import *
root = Tk()
root.title("Student Data Form")
root.geometry("580x670+100+50")


# Function Declaration

def show_data():
    if check_var.get() == "ON":
        get_data = "Name : " + name_var.get() + "\nEmail : " + email_var.get() + "\nGender : " + gender_var.get()
        my_data.config(text = get_data, font = ("arial", 15, "bold"))
    else:
        my_data.config(text = "Please Accept Terms and Conditions.")
title_name = Label(root, text = "STUDENT ENTRY FORM", font = ("arial", 35, "bold"), bg = "white", fg = "blue")
title_name.pack(side = TOP)

main_frame = Frame(root, bd = 3, relief = RAISED)
main_frame.place(x = 20, y = 70, width = 550, height = 580)

#Labels
student_name = Label(main_frame, text = "Student Name : ", font = ("arial", 15, "bold"))
student_name.grid(row = 0, column = 0, pady = 10, sticky = W)

email = Label(main_frame, text = "Student Email : ", font = ("arial", 15, "bold"))
email.grid(row = 1, column =0, pady = 10, sticky = W)

gender = Label(main_frame, text = "Select Gender : ", font = ("arial", 15, "bold"))
gender.grid(row = 2, column = 0, pady = 10, sticky = W)

#Variables
name_var = StringVar()
email_var = StringVar()
gender_var = StringVar()
check_var = StringVar()


#Entry
name_entry = Entry(main_frame,textvariable = name_var, font = ("arial", 15, "bold"), width = 20, highlightthickness = 2)
name_entry.grid(row = 0 , column = 1, padx = 10, pady = 10, sticky = W)

email_entry = Entry(main_frame, textvariable = email_var, font = ("arial", 15, "bold"), width = 20, highlightthickness = 2)
email_entry.grid(row = 1 , column = 1, padx = 10, pady = 10, sticky = W)

#radio

male = Radiobutton(main_frame, variable = gender_var, text = "Male", value = "male", font = ("arial", 15, "bold"))
male.grid(row = 2, column = 1, pady = 2, sticky = W)

gender_var.set("male")

female = Radiobutton(main_frame,variable = gender_var, text = "Female", value = "female", font = ("arial", 15, "bold"))
female.grid(row = 3, column = 1, pady = 2, sticky = W)

#Check Button

check_btn = Checkbutton(main_frame, variable = check_var, onvalue = "ON", offvalue = "OFF", text = "Agree our Terms and Conditions.", font = ("arial", 15, "bold"))
check_btn.grid(row = 4, column = 1, pady = 10, sticky = W)
check_var.set("OFF")

#Button
btn = Button(main_frame, text = "Show Data", width = 20, font = ("arial", 15, "bold"), bg = "blue", fg = "white", activebackground = "blue", command = show_data)
btn.grid(row = 5, column = 1, pady = 10, sticky = W)

# My Data

my_data = Label(main_frame, text = "", font = ("arial", 15, "bold"))
my_data.grid(row = 6, column = 1, pady = 10, sticky = W)


root.mainloop()