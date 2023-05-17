# WELCOME SCREEN
print("--------------------------------------------------")
print("Chromosome Count Analysis")
print("\n")
print("--------------------------------------------------")

true = 1
while (true):
  print("\n")
  # Accept user input for the chromosome_count
  user_input = str(
    input("Enter in the number of chromosomes and press ENTER: "))
  print("\n\n")

  #--------------- Utilization of OOP - Inheritence ------------------------#

  # ------- Create a Parent Class ---------------------#
  # Create a Parent Class named Person, with chromosome count property  and a printresults method
  class Person:

    def __init__(self, chromosome_count):
      self.chromosomecount = chromosome_count

      # Determine Sex/ possible Down Syndrome and Turner's Syndrome based on chromosome count
      if (self.chromosomecount == '44'):
        self.sex = "The individual is a female."
        self.downsyndrome = "The individual does not have Down Syndrome."
        self.turnerssyndrome = "The individual does not have Turner's Syndrome."
      elif (self.chromosomecount == '45'):
        self.sex = "The individual's sex is unknown, additional karyotyping required."
        self.downsyndrome = "The individual does not have Down Syndrome."
        self.turnerssyndrome = "The individual may have Turner's Syndrome."
      elif (self.chromosomecount == '46'):
        self.sex = "The individual is a male."
        self.downsyndrome = "The individual does not have Down Syndrome."
        self.turnerssyndrome = "The individual does not have Turner's Syndrome."
      elif (self.chromosomecount == '47'):
        self.sex = "The individual's sex is unknown, additional karyotyping required."
        self.downsyndrome = "The individual may have Down Syndrome."
        self.turnerssyndrome = "The individual does not have Turner's Syndrome."
      else:
        self.sex = "Cannot be determined, invalid chromosome count!"
        self.downsyndrome = ""
        self.turnerssyndrome = ""

    # Return Results
    def printresults(self):
      print(self.sex)
      print(self.downsyndrome)
      print(self.turnerssyndrome)

  # ------- Create a Child Class ---------------------#
  # Child class named Patient, which will inherit the properties and methods from the Person class
  class Patient(Person):

    def __init__(self, chromosome_count):
      # super() function that will make the child class inherit all the methods and properties from its parent
      super().__init__(chromosome_count)

  # Use the Patient class to create an object, and then execute the printresults method:
  x = Patient(user_input)
  x.printresults()

  continue
