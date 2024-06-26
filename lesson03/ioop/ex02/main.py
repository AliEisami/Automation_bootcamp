from city import City
from history_student import HistoryStudent
from student import Student

def main():
    # student_a = Student("123456", "Ali")
    # student_b = Student("654321", "Eisami")
    # print(student_a.get_help())
    # print(student_a.other_get_help(student_b))

    # city_a = City("3005600", "Daliat El-Carmel")
    # print(f"{city_a.name} {city_a.postcode}")

    history_student_a = HistoryStudent("123456","Ali")
    print(f"{history_student_a.name}-{history_student_a.grade_a}")

main()