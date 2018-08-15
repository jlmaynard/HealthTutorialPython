class Patient:
    """
    This class is like a blueprint for a patient.
    
    Methods:
    
    Data Members:
    name
    age
    symptoms
    """
    def __init__ (self, name, age, symptoms):
        self.name = name
        self.age = age
        self.symptoms = symptoms
        
    def getName(self):
        return self.name
    
    def getAge(self):
        return self.age
    
    def getSymptoms(self):
        return self.symptoms
    
    def giveMedicine(self, meds):
        self.meds = meds
        if (self.meds == "wine"):
            self.symptoms = "Kicks easy"            
        
    
lyssa = Patient("Alyssa", 21, "Kicks too hard")

print ("Her name is {}".format(lyssa.getName()))
print ("She is {}".format(lyssa.getAge()))
print ("Her symptoms are: {}".format(lyssa.getSymptoms()))

print ("Give her medicine")
lyssa.giveMedicine("wine")
print ("Her symptoms after medicine are: {}".format(lyssa.getSymptoms()))


        