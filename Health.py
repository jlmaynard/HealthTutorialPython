# We now have the Patient class in a different file to separate it from
# how we use it. We import it here so we can use it. 
import Patient
          
thePatient = Patient.Patient("Roger", 47, "High blood pressure")

print ("Patient name:", thePatient.getName())
print ("Patient age:", thePatient.getAge())
print ("{}'s symptoms are: {}".format(thePatient.getName(), thePatient.getSymptoms()))

# Next we are going to interact with the patient and give medicine.
# Once we give medicine the object changes state and we print that out 
print ("\nGive the patient medicine")
thePatient.giveMedicine("Losartan")
print ("The patient's symptoms after medicine are: ", thePatient.getSymptoms())


        