# Import Items
from tkinter import *

# ID Card Check
def idCheck(inputID):
    i = 0
    k = 13
    result = 0
    inputID = str(inputID)
    if len(inputID) != 13:
        print("Invalid ID")
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
    inputID = student_id_input.get()
    outputID = idCheck(inputID)
    if outputID == True:
        score = student[inputID]["Score"]
        name = student[inputID]["Name"]
        output_sum.config(text=f"{inputID} {name}\nHave score of {score}")
    else:
        output_sum.config(text="Invalid Student ID")

def none():
    output_sum.config(text=f"DO NOT PRESS ME")

main = Tk()

studentID = StringVar()
std_score = IntVar()

# Variables
student_id = StringVar()
score_select = IntVar()

# Score List
radio_score = ([1, "ไม่ทำการบ้าน", -2],
               [2, "ไม่ตั้งใจเรียน", -2],
               [3, "ไม่ส่งใบลาป่วย/กิจธุระ", -3],
               [4, "วิ่งเล่นบนทางเดิน", -5],
               [5, "กิริยามารยาทไม่เหมาะสม", -5],
               [6, "รับประทานอาหารในห้องเรียน", -5],
               [7, "ไม่เข้าแถวเคารพธงชาติ", -10],
               [8, "โดดเรียน", -20],
               [9, "ช่วยเหลือครู", 5],
               [10, "ทำความดีระดับประเทศ", 10])

# GUI Main Screen
main.title("ระบบจัดการคะแนนความประพฤตินักเรียน")
Label(main, text = "ระบบคะแนนความประพฤตินักเรียน\nโรงเรียนศึกษาพิทยาคมกันยายน", font = ("TH SarabunPSK", "30", "bold"), fg = f"#000000", bg = f"#ccfff0", width = 50).grid(row=0,column=0,columnspan=4)

# Student ID Input / Name Display
student_name_display = Label(main, text = "รหัสนักเรียน 13 หลัก", font = ("TH SarabunPSK", "20", "bold"), width=20)
student_name_display.grid(row=1,column=0)
student_id_input = Entry(main, textvariable=student_id, width=25)
student_id_input.grid(row=1,column=1)
student_id_input.focus()

# Add or Minus Score Title
Label(main, text = "รายการหัก/เพิ่มคะแนน\nที่ผ่านมาของนักเรียน", font = ("TH SarabunPSK", "20", "bold")).grid(row=1,column=2)
Label(main, text = "กรุณาเลือกคะแนน\nที่จะหัก/เพิ่มจากตรงนี้", font = ("TH SarabunPSK", "20", "bold")).grid(row=1,column=3)

# Display Score
output_sum = Label(main, text = "", font = ("TH SarabunPSK", "18"))
output_sum.grid(row=2,column=0)

# Display Latest Menu
output_latest = Label(main, text = "", font = ("TH SarabunPSK", "18"))
output_latest.grid(row=3,column=0)

# Action Buttons
Button(main, text="ตรวจสอบคะแนนและสภาพ", font = ("TH SarabunPSK", "18"), fg = f"#FFFFFF", bg = f"#126D42", command = scoreCheck, width = 20, height=1).grid(row=2,column=1)
Button(main, text="เพิ่ม/หักคะแนนนักเรียน", font = ("TH SarabunPSK", "18"), fg = f"#FFFFFF", bg = f"#8F100C", command = none, width = 20, height=1).grid(row=3,column=1)

# Student Log
student_log = Label(main, text = "", font = ("TH SarabunPSK", "18"))
student_log.grid(row=2,column=2)

# Radio Button Score List
row_radio = 2
for score_list, score_label, score_todo in radio_score:
    score_type = Radiobutton(main, text=score_label, variable=score_select, value=score_list, font = ("TH SarabunPSK", "18"),height=1,anchor=W)
    score_type.grid(row=row_radio,column=3)
    row_radio += 1

# Open Main Menu
main.mainloop()