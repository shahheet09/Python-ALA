print("Exam Result Analyzer")
subjects = int(input("Enter number of subjects: "))
i = 0
total = 0
fail_count = 0
while i < subjects:  # Loop starts
marks = int(input("Enter marks: "))  # ❌ Indentation error
total = total + marks  # ❌ Indentation error
if marks < 35:  # ❌ Indentation error
fail_count = fail_count + 1  # ❌ Indentation error
i = i + 1  # ❌ Indentation error
percentage = total / subjects  # ❌ No zero check (may cause ZeroDivisionError)
print("Total:", total)
print("Percentage:", percentage)
print("Fail count:", fail_count  # ❌ Missing closing parenthesis
if fail_count > 0:
print("Result: Fail")  # ❌ Indentation error
elif percentage >= 75:
print("Distinction")  # ❌ Indentation error
elif percentage >= 60:
print("First Class")  # ❌ Indentation error
else:
print("Pass")  # ❌ Indentation error
if percentage > 90  # ❌ Missing colon
print("Excellent performance")
else:
print("Keep improving")