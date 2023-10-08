import csv as c

test = [["test1", "test2"],
        ["test1", "test3"],
        ["testc", "wtf"],
        ["test1", "test3"]]

filepath = "wtf.csv"

with open(filepath,'w',encoding="utf-8") as f1:
    write = c.writer(f1, lineterminator="\n")
    write.writerows(test)
