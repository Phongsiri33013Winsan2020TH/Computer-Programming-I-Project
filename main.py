# Lang Config
id_error = "National ID is invalid"
univ_name = "Tunyathep University"
foregroundColor = "#FFFFFF"
backgroundColor = "#FD6E03"

# Student List (to be write in file)
student = {
    "6604062636453": {"Name": "Phongsiri Loedphongthai", "Score": "80"},
    "6604062636321": {"Name": "Tunyathep Ananthanapong", "Score": "120"}
}

from tkinter import *

# ID Card Check
def idCheck(inputID):
    i = 0
    k = 13
    result = 0
    inputID = str(inputID)
    if len(inputID) != 13:
        print(id_error)
    else:
        while i < 12:
            result = result+(int(inputID[i])*k)
            k -= 1
            i += 1
        result = result%11
        result = 11-result
        outputID = result
        outputID = outputID%10
        outputID = bool(int(inputID[12]) == outputID)
        return outputID

def scoreCheck():
    inputID = studentID.get()
    outputID = idCheck(inputID)
    if outputID == True:
        score = student[inputID]["Score"]
        name = student[inputID]["Name"]
        output.config(text=f"{inputID} {name}\nHave score of {score}")
    else:
        output.config(text="Invalid Student ID\n")

def none():
    output.config(text=f"The button isn't implemented yet\n")

main = Tk()

studentID = StringVar()
std_score = IntVar()

main.minsize(750, 250)
main.title("Student Scoring System")
Label(main, text = f"{univ_name}", font = ("TH SarabunPSK", "36", "bold"), fg = f"{foregroundColor}", bg = f"{backgroundColor}").grid(row=0,column=0,columnspan=3)
Label(main, text = f"Student Scoring System", font = ("TH SarabunPSK", "24"), fg = f"#000000", bg = f"#FFC89F").grid(row=1,column=0,columnspan=3)
output = Label(main, text = "\n", font = ("TH SarabunPSK", "18"))
output.grid(row=2,column=0,columnspan=3)
Label(main, text = "Please enter student ID", font = ("TH SarabunPSK", "18", "bold")).grid(row=3,column=0)
sID = Entry(main, textvariable=studentID)
sID.grid(row=3,column=1, columnspan=2)
sID.focus()
Label(main, text = "Score to add/minus", font = ("TH SarabunPSK", "18", "bold")).grid(row=4,column=0)
sc = Entry(main, textvariable=std_score)
sc.grid(row=4,column=1, columnspan=2)
Button(main, text="Add Score", font = ("TH SarabunPSK", "18"), fg = f"#FFFFFF", bg = f"#FD5033", command = none).grid(row=5,column=0)
Button(main, text="Check Score", font = ("TH SarabunPSK", "18"), fg = f"#000000", bg = f"#FFD30B", command = scoreCheck).grid(row=5,column=1)
Button(main, text="Remove Score", font = ("TH SarabunPSK", "18"), fg = f"#FFFFFF", bg = f"#0F8436", command = none).grid(row=5,column=2)
Button(main, text="×", font = ("TH SarabunPSK", "20", "bold"), fg = f"#FFFFFF", bg = f"#830000", command = main.destroy).grid(row=6,column=2)
main.mainloop()