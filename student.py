class Student:

  
  def __init__(self, oEN, num, nam0, nam1, dOB, address, contact, emergencyContact, medical):
    # Ontario Education Number
    self.__oEN = oEN
    # Student number
    self.num = num
    # First name
    self.__nam0 = nam0
    # Last name
    self.__nam1 = nam1
    # Date of birth
    self.__dOB = dOB
    self.__address = address
    # Contact information
    self.__contact = contact
    # Emergency contact information
    self.__emergencyContact = emergencyContact
    # Medical information
    self.__medical = medical


  # Getters and setters

  def getOEN(self):
    return self.__oEN

  def getNum(self):
    return self.num

  def getNam0(self):
    return self.__nam0

  def setNam0(self, nam):
    self.__nam0 = nam

  def getNam1(self):
    return self.__nam1

  def setNam1(self, nam):
    self.__nam1 = nam

  def getDOB(self):
    return self.__dOB

  def getAddress(self):
    return self.__address

  def setAddress(self, address):
    self.__address = address

  def getContact(self):
    return self.__contact

  # Placeholder - will update after creating Contact class
  def setContact(self, contact):
    self.__contact = contact

  def getEmergencyContact(self):
    return self.__emergencyContact

  # Placeholder - will update after creating Emergency Contact class
  def setEmergencyContact(self, emergencyContact):
    self.__emergencyContact = emergencyContact

  def getMedical(self):
    return self.__medical

  # Placeholder - will update after creating Medical class
  def setMedical(self, medical):
    self.__medical = medical
