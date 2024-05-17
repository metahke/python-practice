# PART I

class Member:
    def __init__(self, full_name: str) -> None:
        self.full_name: str = full_name

    def introduce(self) -> None:
        print(f"Hi, my name is {self.full_name}")


class Student(Member):
    def __init__(self, full_name: str, reason: str) -> None:
        super().__init__(full_name)
        self.reason: str = reason


class Instructor(Member):
    def __init__(self, full_name: str, bio: str) -> None:
        super().__init__(full_name)
        self.bio: str = bio
        self.skills: list[str] = []

    def add_skill(self, skill: str) -> None:
        self.skills.append(skill)


# PART II

class Workshop:
    def __init__(self, date: str, subject: str) -> None:
        self.date: str = date
        self.subject: str = subject
        self.students: list[Student] = []
        self.instructors: list[Instructor] = []

    def add_participant(self, member: Member) -> None:
        if isinstance(member, Student):
            self.students.append(member)
        elif isinstance(member, Instructor):
            self.instructors.append(member)

    def print_details(self) -> None:
        print("=>")
        print(f"Workshop - {self.date} - {self.subject}")
        print("")

        print("Students")
        for i, student in enumerate(self.students):
            print(f"{i + 1}. {student.full_name} - {student.reason}")
        print("")

        print("Instructors")
        for i, instructor in enumerate(self.instructors):
            print(f"{i + 1}. {instructor.full_name} - {', '.join(instructor.skills)}\n   {instructor.bio}")
        print("")


# Test Your Code

def main() -> None:
    workshop = Workshop("12/03/2014", "Shutl")

    jane = Student("Jane Doe", "I am trying to learn programming and need some help")
    lena = Student("Lena Smith", "I am really excited about learning to program!")
    vicky = Instructor("Vicky Python", "I want to help people learn coding.")
    vicky.add_skill("HTML")
    vicky.add_skill("JavaScript")
    nicole = Instructor("Nicole McMillan", "I have been programming for 5 years in Python and want to spread the love")
    nicole.add_skill("Python")

    workshop.add_participant(jane)
    workshop.add_participant(lena)
    workshop.add_participant(vicky)
    workshop.add_participant(nicole)
    workshop.print_details()


if __name__ == "__main__":
    main()
