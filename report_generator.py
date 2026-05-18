def calculate_average(backend, frontend, design):
    return (backend + frontend + design) / 3


def get_grade(average):
    if average >= 80:
        return "A"
    elif average >= 70:
        return "B"
    elif average >= 60:
        return "C"
    elif average >= 50:
        return "D"
    else:
        return "E"


def create_report(name, backend, frontend, design):
    avg = calculate_average(backend, frontend, design)
    grade = get_grade(avg)


    return {
        "name": name,
        "Backend": backend,
        "Frontend": frontend,
        "Design": design,
        "average": avg,
        "grade": grade,
    }



name = input("Enter student name: ")
backend = float(input("Enter Backend marks: "))
frontend = float(input("Enter Frontend marks: "))
design = float(input("Enter Design marks: "))


report = create_report(name, backend, frontend, design)
print("Report: ")
print(report)
