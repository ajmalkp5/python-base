all_stud=open("C:\\Users\\ASUS\\Desktop\\my python\\fileio\\students.txt","r")
faild_stud=open("C:\\Users\\ASUS\\Desktop\\my python\\fileio\\failed.txt","r")

all_stud_set={st.rstrip("\n") for st in all_stud}

faild_stud_set={st.rstrip("\n") for st in faild_stud}

passes_stud=all_stud_set-faild_stud_set
print(passes_stud)
