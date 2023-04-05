""" here we want to use CLASSES to represent a student in the program we want to create. it is for a unniversity or colege. in this program we want to model a real student (or a real world object)... and we don't have a student datatype and we can't represent him in just a string or number. SO!! for that we create a class for a student and it is a student datatype 😃"""

#FOR THAT:
#we do: class [name of class]:

class student:
   #in this class we can define a bunch of atributes about a student(here we are modeling a student prototype)
   
   #so, in the function we first create an initialized function like this:
   def __init__(self,name,major,gpa,is_on_probation):
      
      #here we will map out what atributes student should have, like: name, major(because they are at the colege), a GPA(their Grade Point Average or marks average), is_on_probation (this is a bolean... and all of these are going to be putted next to "self"
      
      #what we are doing here is, we are defining who is a student in our program.. he has a name,a gpa,a major, and can be on aprobation.. THAT IS THE STUDENT DATATYPE we created 🥳🥳🥳 
      
      #now let's assign some values to  
      self.name=name
      self.malor=major
      self.gpa=gpa
      self.is_on_probation=is_on_probation
      #Now we have our student class defined and we can use it in other python files