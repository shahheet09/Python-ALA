print("Exam Result Analyzer")
try:
    subjects = int(input("Enter number of subjects: "))

    if subjects <= 0:
        print("Subjects must be greater than zero.")
    else:
        i = 0
        total = 0
        fail_count = 0

        while i < subjects:
            marks = int(input("Enter marks: "))
            total = total + marks

            if marks < 35:
                fail_count = fail_count + 1

            i = i + 1

        percentage = total / subjects

        print("Total:", total)
        print("Percentage:", percentage)
        print("Fail count:", fail_count)

        if fail_count > 0:
            print("Result: Fail")
        elif percentage >= 75:
            print("Distinction")
        elif percentage >= 60:
            print("First Class")
        else:
            print("Pass")

        if percentage > 90:
            print("Excellent performance")
        else:
            print("Keep improving")

except ValueError:
    print("Please enter valid numeric input.")