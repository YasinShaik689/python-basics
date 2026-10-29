
def print_student_details(**details):
    for key, value in details.items():
        print(f"{key.capitalize()}: {value}")

print_student_details(name="Eva", grade="A", subject="Math")

print_student_details(name="Frank", age=22, university="Tech University", major="CS")
