# here we want to read the content of the "employees file"

#we use the comand "open( name of the file )" ... we can put in a relative or absolute path to the file or just the files name and "the mode that we want to open the file in"

employees_file=open("employees.txt","r")

#‼️‼️‼️ here we've stored the open function in a variable so that we can use it latter!!!


#but also, always check if a file is readable by using:
print(employees_file.readable())
 #this will return a bolean value telling us if its readable or not(here it will be true because we choosed the read mode, but it could be false if we chosed the write mode and check if it is readable)

#we can use the for loop to access the content of the list:

#for employee in employees_file.readlines():
#   print(employee)


#then print:
#print(employees_file.read())


print(employees_file.readline()) #this gonna read only the first line..

#we can use that "readline() twice to print the two first lines "

#we can use "readlines()" and put them in a list and use readlines()[index of the word we want to access in the list]... this will not only print the character at that statement but all the sentence of that index

#also, always close the opened file by using a close function
employees_file.close()


#the "r"(which means "read only" and and not modify it or change it) ,this is the mode that we want to open the file in... there are many different modes that we can open our file in,

#another mode is "w"(which means "write", use to add new informations and even change the existing ones)

#another one is "a"(which means "append") and it means that you can append information at the end of the file, but you can't modify or change the existing content of the file but you can only add new information at the end of the file

#another one is "r+" (which means read and write) and this mode gives you all the power of reading and modifying the file at the same time.

