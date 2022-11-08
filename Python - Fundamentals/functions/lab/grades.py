def grade():
    current_grade = float(input())

    if 2 <= current_grade < 3:
        return "Fail"
    elif 3 <= current_grade < 3.5:
        return "Poor"
    elif 3.5 <= current_grade < 4.5:
        return "Good"
    elif 4.5 <= current_grade < 5.5:
        return "Very Good"
    elif 5.5 <= current_grade <= 6:
        return "Excellent"


print(grade())
