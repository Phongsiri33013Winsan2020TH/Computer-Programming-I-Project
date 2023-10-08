# Import Items
from tkinter import *
import csv
import datetime

# Score List
radio_score = ([1, "ไม่ทำการบ้าน", "-2"],
               [2, "ไม่ตั้งใจเรียน", "-2"],
               [3, "ไม่ส่งใบลาป่วย/กิจธุระ", "-3"],
               [4, "วิ่งเล่นบนทางเดิน", "-5"],
               [5, "กิริยามารยาทไม่เหมาะสม", "-5"],
               [6, "รับประทานอาหารในห้องเรียน", "-5"],
               [7, "ไม่เข้าแถวเคารพธงชาติ", "-10"],
               [8, "โดดเรียน", "-20"],
               [9, "ช่วยเหลือครู", "5"],
               [10, "ทำความดีระดับประเทศ", "10"])

# ID Card Validation Check
def id_validate(entry):
    i = 0
    k = 13
    result = 0
    entry = str(entry)
    if len(entry) != 13:
        print("Invalid ID")
    else:
        while i < 12:
            result = result+(int(entry[i])*k)
            k -= 1
            i += 1
        result = result%11
        result = 11-result
        result = result%10
        result = bool(int(entry[12]) == result)
        return result

# Loop student.csv to check ID score
def score_check():
    entry_id = student_id_input.get()
    valid_id = id_validate(entry_id)
    if valid_id:
        try:
            with open("student.csv", "r", encoding="utf-8") as student_list:
                read = csv.reader(student_list)
                student_score = list(read)
        except Exception:
            output_sum.config(text="ไม่พบไฟล์นักเรียน")
        none = True
        for student_score in student_score:
            if entry_id == student_score[1]:
                none = False
                if int(student_score[3]) > 50:
                    status = "ปกติ"
                else:
                    status = "ติดทัณฑ์บน"
                student_name_display.config(text=f"{student_score[2]}")
                output_sum.config(text=f"คะแนนคงเหลือ {student_score[3]}")
                output_latest.config(text=f"สถานะ: {status}")
        if none:
            student_name_display.config(text=f"ไม่พบรหัสนักเรียนในระบบ")
    else:
        student_name_display.config(text="รหัสนักเรียนไม่ถูกต้อง")

def score_edit():
    entry_id = student_id_input.get()
    valid_id = id_validate(entry_id)
    score_index = score_select.get()
    score = radio_score[score_index-1][2]
    score = int(score)
    if valid_id == True:
        if score_index == 0:
            student_name_display.config(text=f"กรุณาเลือกประเภทคะแนน")
            return
        try:
            with open("student.csv", "r", encoding="utf-8") as student_list:
                read = csv.reader(student_list)
                student_score_list = list(read)
        except Exception:
            output_sum.config(text="ไม่พบไฟล์นักเรียน")
        none = True
        found = False
        for student_score in student_score_list:
            if entry_id == student_score[1]:
                current = student_score[3]
                done = int(current) + score
                none = False
                found = True
                student_score[3] = str(done)
                student_name_display.config(text=f"{student_score[2]}")
                output_sum.config(text=f"คะแนนที่เพิ่ม/หัก {score:d}")
                output_latest.config(text=f"คะแนนคงเหลือ {done}")
                break
        if found:
            try:
                with open("student.csv", "w", newline="", encoding="utf-8") as student_list_file:
                    writer = csv.writer(student_list_file)
                    writer.writerows(student_score_list)
            except Exception:
                student_name_display.config(text="เกิดข้อผิดพลาดในการบันทึกคะแนน")
            current = datetime.datetime.now()
            with open("log.txt", "a", encoding="utf-8") as log:
                log.write(f"at {current} > {student_score[1]} {student_score[2]} has been add/deduct score of {score}, score left of {done}\n")
        if none:
            student_name_display.config(text=f"ไม่พบรหัสนักเรียนในระบบ")
    else:
        student_name_display.config(text="รหัสนักเรียนไม่ถูกต้อง")

# Main Menu Definition
main = Tk()

# Variables
student_id = StringVar()
score_select = IntVar()

# GUI Main Screen
main.title("ระบบจัดการคะแนนความประพฤตินักเรียน")
Label(main, text = "ระบบคะแนนความประพฤตินักเรียน\nโรงเรียนศึกษาพิทยาคมกันยายน", font = ("TH SarabunPSK", "30", "bold"), fg = f"#000000", bg = f"#ccfff0", width = 65).grid(row=0,column=0,columnspan=3)

# Student ID Input / Name Display
student_name_display = Label(main, text = "รหัสนักเรียน 13 หลัก", font = ("TH SarabunPSK", "20", "bold"), width=20)
student_name_display.grid(row=1,column=0)
student_id_input = Entry(main, textvariable=student_id, width=40)
student_id_input.grid(row=1,column=1)
student_id_input.focus()

# Add or Minus Score Title
Label(main, text = "กรุณาเลือกคะแนน\nที่จะหัก/เพิ่มจากตรงนี้", font = ("TH SarabunPSK", "20", "bold")).grid(row=1,column=2)

# Display Score
output_sum = Label(main, text = "", font = ("TH SarabunPSK", "18"))
output_sum.grid(row=2,column=0)

# Display Latest Menu
output_latest = Label(main, text = "", font = ("TH SarabunPSK", "18"))
output_latest.grid(row=3,column=0)

# Action Buttons
Button(main, text="ตรวจสอบคะแนนและสภาพ", font = ("TH SarabunPSK", "18"), fg = f"#FFFFFF", bg = f"#126D42", command = score_check, width = 20, height=1).grid(row=2,column=1)
Button(main, text="เพิ่ม/หักคะแนนนักเรียน", font = ("TH SarabunPSK", "18"), fg = f"#FFFFFF", bg = f"#8F100C", command = score_edit, width = 20, height=1).grid(row=3,column=1)

# Radio Button Score List
row_radio = 2
for score_list, score_label, score_todo in radio_score:
    score_type = Radiobutton(main, text=score_label, variable=score_select, value=score_list, font = ("TH SarabunPSK", "18"),height=1,anchor=W)
    score_type.grid(row=row_radio,column=2)
    row_radio += 1

# Open Main Menu
main.mainloop()