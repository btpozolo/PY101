def get_grade(g1, g2, g3):
    avg = (g1 + g2 + g3) / 3

    if avg >= 90:
        return 'A'
    elif avg >= 80:
        return 'B'
    elif avg >= 70:
        return 'C'
    elif avg >= 60:
        return 'D'
    else:
        return 'F'
    
print(get_grade(95, 90, 93) == "A")      # True
print(get_grade(50, 50, 95) == "D")      # True

def get_grade(grade1, grade2, grade3):
    average = (grade1 + grade2 + grade3) // 3

    if average in range(90, 101):
        return "A"
    elif average in range(80, 90):
        return "B"
    elif average in range(70, 80):
        return "C"
    elif average in range(60, 70):
        return "D"
    else:
        return "F"
    
get_grade(90, 90, 90.1)