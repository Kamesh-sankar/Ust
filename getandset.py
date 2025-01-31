class Person:
  # def __init__(self,name,age):
  #   self.name = name
  #   self.age = age
  # #setter method
  # def set_Age(self,age):
  #   if age<=0:
  #     raise ValueError("Age cannot be zero or negative")
  #   self.age = age
  # def get_Age(self):
  #   return self.age
  def __init__(self,name,age):
    self.name=name
    self.age=age
    
  @property
  def age(self):
    return self._age
  
  @age.setter
  def age(self,value):
    if value<=0:
      raise ValueError("Age cannot be zero or negative")
    self._age = value
    
  @property
  def name(self):
    return self._name
    
  @name.setter
  def name(self,value):
    if value == "":
      raise ValueError("Name cannot be empty")
    self._name = value
    
p1 = Person("John",36)
print(p1.name)
print(p1.age)
p1.name=""
