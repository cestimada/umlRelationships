
# 1. INHERITANCE
class Vehicle:
    def __init__(self, brand: str):
        self.brand = brand

    def start_engine(self):
        return f"{self.brand} engine started."

class ElectricCar(Vehicle):  # ElectricCar "is a" Vehicle
    def charge(self):
        return f"{self.brand} is charging its battery."


# 2. COMPOSITION 
class Engine:
    def __init__(self, horsepower: int):
        self.horsepower = horsepower

    def ignite(self):
        return f"Engine roaring with {self.horsepower} HP!"

class Car:
    def __init__(self, brand: str, horsepower: int):
        self.brand = brand
        self.engine = Engine(horsepower)

    def drive(self):
        return f"{self.brand} is driving. {self.engine.ignite()}"

# 3. AGGREGATION 
class Professor:
    def __init__(self, name: str):
        self.name = name

class Department:
    def __init__(self, name: str):
        self.name = name
        self.professors = []  # Aggregation: container holding independent objects

    def add_professor(self, professor: Professor):
        self.professors.append(professor)

    def show_faculty(self):
        return [p.name for p in self.professors]

# 4. ASSOCIATION

class Patient:
    def __init__(self, name: str):
        self.name = name

class Doctor:
    def __init__(self, name: str):
        self.name = name

    def consult(self, patient: Patient):
        return f"Dr. {self.name} is treating patient {patient.name}."



# 5. DEPENDENCY 

class Document:
    def __init__(self, content: str):
        self.content = content

class Printer:
    
    def print_document(self, document: Document):
        return f"Printing content: '{document.content}'"



if __name__ == "__main__":
    print("1. Inheritance ")
    ev = ElectricCar("Tesla")
    print(ev.start_engine())  
    print(ev.charge())        

    print("2. Composition ")
    my_car = Car("Ford", 450)
    print(my_car.drive())     

    print("3. Aggregation ")
    prof1 = Professor("Dr. Smith")
    prof2 = Professor("Dr. Turing")
    cs_dept = Department("Computer Science")
    cs_dept.add_professor(prof1)
    cs_dept.add_professor(prof2)
    print(f"{cs_dept.name} faculty:", cs_dept.show_faculty())

    print("4. Association")
    doc = Doctor("House")
    pat = Patient("John Doe")
    print(doc.consult(pat))   

    print("5. Dependency ")
    doc_to_print = Document("Hello, Object-Oriented Python!")
    laser_printer = Printer()
    print(laser_printer.print_document(doc_to_print))  