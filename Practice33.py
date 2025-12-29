sub1= int(input("Enter Marks of subject : "))
sub2= int(input("Enter Marks of subject : "))
sub3= int(input("Enter Marks of subject : "))
pass_marks=40
print("Marks in first subject   = " , sub1)
print("Marks in Second subject  = " , sub2)
print("Marks in Third subject = " , sub3)
Ttlmakrs=sub1+sub2+sub3
avgmarks=sub1+sub2+sub3/3
print("Average Marks = " , avgmarks)
print("Total Marks = " , Ttlmakrs)
if avgmarks>=pass_marks:
    print("Passed !")
elif avgmarks<pass_marks:
    print("Failed!")
