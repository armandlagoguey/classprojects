#I'm so sorry for those horrible variable names...

grades = open('grades.txt', "r")
str1 = grades.readline()
str2 = grades.readline()
str3 = grades.readline()
grades.close()
str1 = str1.strip()
str2 = str2.strip()
str3 = str3.strip()

str1 = str1.split(',')
str1_student_id = str1[0]
str1_score1 = int(str1[1])
str1_score2 = int(str1[2])
str1_score3 = int(str1[3])

str2 = str2.split(',')
str2_student_id = str2[0]
str2_score1 = int(str2[1])
str2_score2 = int(str2[2])
str2_score3 = int(str2[3])

str3 = str3.split(',')
str3_student_id = str3[0]
str3_score1 = int(str3[1])
str3_score2 = int(str3[2])
str3_score3 = int(str3[3])

average1 = float((str1_score1+str1_score2+str1_score3)/3)
average2 = float((str2_score1+str2_score2+str2_score3)/3)
average3 = float((str3_score1+str3_score2+str3_score3)/3)

results= open('results.txt', "w")

if average1 >= 70.0:
    results.writelines(f"{str1_student_id} {average1:.2f} Pass\n")
elif average1 >= 60.0 and str1_score3 >  65:
    results.writelines(f"{str1_student_id} {average1:.2f} Pass\n")
else:
    results.writelines(f"{str1_student_id} {average1:.2f} Fail\n")



if average2 >= 70.0:
    results.writelines(f"{str2_student_id} {average2:.2f} Pass\n")
elif average2 >= 60.0 and str2_score3 >  65:
    results.writelines(f"{str2_student_id} {average2:.2f} Pass\n")
else:
    results.writelines(f"{str2_student_id} {average2:.2f} Fail\n")



if average3 >= 70.0:
    results.writelines(f"{str3_student_id} {average3:.2f} Pass\n")
elif average3 >= 60.0 and str3_score3 >  65:
    results.writelines(f"{str3_student_id} {average3:.2f} Pass\n")
else:
    results.writelines(f"{str3_student_id} {average3:.2f} Fail\n")

results.close()
