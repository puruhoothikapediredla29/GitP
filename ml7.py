class Student:

    def __init__(self):
        self.name = "Puru"       # public
        self._age = 21           # protected
        self.__marks = 90        # private

    def show_inside(self):
        print(self.name)         # ✅
        print(self._age)         # ✅
        print(self.__marks)      # ✅


class CollegeStudent(Student):

    def show_from_child(self):
        print(self.name)         # ✅
        print(self._age)         # ✅
        print(self.__marks)      # ❌


s = CollegeStudent()

print("Inside parent:")
s.show_inside()

print("\nInside child:")
s.show_from_child()

print("\nOutside:")
print(s.name)       # ✅
print(s._age)       # ⚠️ technically works
print(s.__marks)    # ❌