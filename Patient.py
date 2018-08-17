class Patient:  # This is name of the class
    """
    These comments describe what the class does and will pop up with
    mouse overs when writing code.
    
    This class is like a blueprint for a patient.
    
    Methods:
    getName()
    getAge()
    getSymptoms()
    giveMedicine()
    
    Data Members:
    name
    age
    symptoms
    """
    def __init__ (self, name, age, symptoms):  # This is a constructor to make a patient
        # these are the "data member variables that store information for each object"
        self.name = name
        self.age = age
        self.symptoms = symptoms
        
    # These are the "methods" or actions you can take on a patient object once created    
    def getName(self):
        return self.name
    
    def getAge(self):
        return self.age
    
    def getSymptoms(self):
        return self.symptoms
    
    def giveMedicine(self, meds):
        self.meds = meds
        if (self.meds == "Losartan"):
            self.symptoms = "Normal BP"  