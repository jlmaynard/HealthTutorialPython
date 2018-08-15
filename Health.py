# First tutorial in python for a health care application
# This is a simple object oriented tutorial that can be built upon to
# add multiple patients, put them in hospitals, have doctors work on them,
# and collect data for further processing.

# First make a class for the patient. The class is like a blueprint that defines
# what a patient looks like and what you can do with the patient. 
class Patient:  # This is name of the class
    """
    This class is like a blueprint for a patient.
    
    Methods:
    
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
        if (self.meds == "wine"):
            self.symptoms = "Kicks easy"            
        
# here we create a new object from the class patient called lyssa
# we give the object values to put in the data members
        # This is the constructor in action.
# making objects in object oriented languages is called "instantiating" an object
# each object is an instance of a class. 
lyssa = Patient("Alyssa", 21, "Kicks too hard")

# now we are going to interact with the object and call the methods to get the name,
# age, and symptoms we originally set. 
print ("Her name is {}".format(lyssa.getName()))
print ("She is {}".format(lyssa.getAge()))
print ("Her symptoms are: {}".format(lyssa.getSymptoms()))

# Next we are going to interact with the patient and give medicine.
# Once we give medicine the object changes state and we print that out 
print ("Give her medicine")
lyssa.giveMedicine("wine")
print ("Her symptoms after medicine are: {}".format(lyssa.getSymptoms()))


        