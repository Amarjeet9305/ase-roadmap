# Write a program for vehcile to inhertince properties

class School:
    def __init__(self,management,Department):
        self.management = management
        self.Department = Department
    def control(self):
        print("Management handle system..")
        
class CSE(School):
    
    def tech(self):
        
        print("Classes is running by management by department")

room = CSE("POC Management", "Computer Science")
room.control()
room.tech()        
                
        
        