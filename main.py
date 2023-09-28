def idCheck(inputID):
    i = 0
    k = 13
    result = 0
    if len(inputID) != 13:
        print("The ID card digit is invalid.")
    else:
        while i < 12:
            result = result+(int(inputID[i])*k)
            k -= 1
            i += 1
        result = result%11
        result = 11-result
        outputID = result
        if outputID > 9: # เอาหลักหน่วยออก
            outputID = 1
        outputID = bool(int(inputID[12]) == outputID)
        return outputID

idExample = "ลองเลขบัตรที่นี้"
test = idCheck(idExample)
if test != None:
  print(test)
