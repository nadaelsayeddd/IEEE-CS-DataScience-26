try:
    with open(r"C:\Users\Nada\Downloads\students.txt", "r") as file:
        lines = file.readlines()
except:
    print("File not found")
    lines = []

if len(lines) == 0:
    print("File is empty")
else:
    student_names = []
    student_hours = []
    subject_names = []
    subject_hours = []

    for line in lines:
        line = line.strip()
        if line == "":
            continue

        parts = line.split(",")
        if len(parts) != 3:
            continue

        name = parts[0].strip()

        try:
            hours = float(parts[1].strip())
        except:
            continue

        subject = parts[2].strip()

        if name in student_names:
            index = student_names.index(name)
            student_hours[index] += hours
        else:
            student_names.append(name)
            student_hours.append(hours)

        if subject in subject_names:
            index = subject_names.index(subject)
            subject_hours[index] += hours
        else:
            subject_names.append(subject)
            subject_hours.append(hours)

    max_hours = 0
    top_student = ""

    for i in range(len(student_hours)):
        if student_hours[i] > max_hours:
            max_hours = student_hours[i]
            top_student = student_names[i]

    max_sub = 0
    top_subject = ""

    for i in range(len(subject_hours)):
        if subject_hours[i] > max_sub:
            max_sub = subject_hours[i]
            top_subject = subject_names[i]

    with open(r"C:\Users\Nada\Downloads\summary.txt", "w") as file:
        file.write("Total Hours Per Student:\n")
        for i in range(len(student_names)):
            file.write(f"{student_names[i]}: {int(student_hours[i])}\n")

        file.write("\nTotal Hours Per Subject:\n")
        for i in range(len(subject_names)):
            file.write(f"{subject_names[i]}: {int(subject_hours[i])}\n")

        file.write(f"\nTop Student: {top_student} ({int(max_hours)} hours)\n")
        file.write(f"Most Studied Subject: {top_subject}\n")

    print("summary.txt created successfully")