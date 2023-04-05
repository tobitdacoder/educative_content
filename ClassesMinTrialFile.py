"""
so here we want to create a student(and we will use our student class that we created in the classesAndObject.py file), in that file we just defined the student datatype like, "hey, the student has: a name, a major, a gpa, is or is not on probation"... that is the template of what a student really is...

so with that we can actually create an actual "student" and give it some info... that is called an object 

!! THE CLASS ONLY DEFINES WHAT A STUDENT IS(a template of what a student is ) OR AN OVERVIEW OF WHAT A STUDENT DATATYPE IS AND AN OBJECT IS AN ACTUAL STUDENT (with all those diffents parameters like name,age,gpa,major,on or not on aprobation)
"""

#So in order to use that class and create a student object we need to import the class from that file (classesAndObject.py) containing the class "student", let's do that:

from classesAndObect import student  
#this basically mean "from the file"classesAndObect", import the class "student"

#now we can create a student object just like we would create a variable:

student1=student("toby","computer science",4.2,False)
student2=student("samuel","law",3.6,False)
student3=student("david","business",4.3,False)

#we can create as many student as want...
#here:

#student=class
#student1=object
#toby=name
#computer science=major
#4.2=gpa
#False=is or is not_on_probation

#an objct is just an intance of a class
print(student1.name) #to access the name in the object.. we can do it for the gpa etc
