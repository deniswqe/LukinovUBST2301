from mygroup import groupmates

def print_students(students):
    print("Имя".ljust(15), "Фамилия".ljust(15), "Экзамены".ljust(40), "Оценки")
    for student in students:
        print(
            student["name"].ljust(15),
            student["surname"].ljust(15),
            str(student["exams"]).ljust(40),
            str(student["marks"])
        )

def filter_by_average(students, min_avg):
    result = []
    for student in students:
        avg = sum(student["marks"]) / len(student["marks"])
        if avg >= min_avg:
            result.append(student)
    return result

def main():
    print("Все студенты:")
    print_students(groupmates)

    print("\nВведите минимальный средний балл для фильтрации:")
    try:
        min_avg = float(input("Минимальный средний балл: "))
    except ValueError:
        print("Ошибка: нужно вводить число!")
        return

    filtered = filter_by_average(groupmates, min_avg)

    print("\nСтуденты с средним баллом выше или равным", min_avg)
    print_students(filtered)

if __name__ == "__main__":
    main()
