class Student:
    def __init__(self, name, matrikel):
        self.name = name
        self.matrikel = matrikel
    
    def print_name(self):
        print("Name " + self.name)
    
    def print_matrikel(self):
        print("Matrikel " + str(self.matrikel))
    
    def print(self):
        self.print_name()
        self.print_matrikel()

# Usage:
Suse = Student("Suse", 192837465)
Suse.print()

Max = Student("Max", 987654321)
Max.print()