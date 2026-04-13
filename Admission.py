# Checks admission eligibility and scholarship based on age, score, and income
name = input("Enter name: ")
age = int(input("Enter age: "))
exam_score = int(input("Enter exam score: "))
family_income = float(input("Enter family income: "))

if age < 16:
    print(name, "Sorry, too young.")
elif exam_score < 60:
    print(name, "Exam score too low.")
else:
    
    if family_income < 30000:
        print(name, "Admitted with full scholarship")
    elif family_income < 80000:
        print(name, "Admitted with partial scholarship")
    else:
        print(name, "Admitted without scholarship")