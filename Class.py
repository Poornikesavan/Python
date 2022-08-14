from datetime import date
class Employee:

    def __init__(self,name,gender,joining_year,city,salary=100000):
        self.name=name
        self.gender=gender
        self.city=city
        self.salary=salary
        self.joining_year=joining_year

    def address(self):
        addr=f"Name : {self.name}\nGender : {self.gender}\nJoining_year : {self.joining_year}\ncity : {self.city}\nSalary : {self.salary}"
        return addr

    def experience(self):
        current_year=date.today().year
        exp=current_year - self.joining_year
        return f"experience : {exp}"


stu1=Employee("Poorni","Female",2005,"Chennai")

print(stu1.address())
print(stu1.experience())
