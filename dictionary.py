#DICTIONARIES!!!!!!!!!

monthDictionary={
   "jan": "january",
   "feb": "february",
   "mar": 3 ,# this is just to try is the key can print a number or an expression result 😊 
   "apr": "april",
   "ma": "may",
   "jun": "june",
   "jul": " this is jully",
   "aug": "august",
   "sep": "this month is called september", #just trying to diversify the output
   "oct": "october",
   "nov": "november",
   "dec": "december",
#here in this dictionary : "jan" is a key and "january is it's value"
#these keys can also be numbers like 1: "january" or 2:"february"

   
}

#this is the first way to access the dictionary content
print(monthDictionary["mar"])
print(monthDictionary["feb"])

#the second way is: 
print(monthDictionary.get("nov","not a valid key"))
#the cool thing with this is that we can set a default value that 
#  we can use if the key is not found: eg. print(monthDictionary.get("luv","not a valid key"))
# "luv" which is not in the key set... 
# here the default value will be "not a valid key" 


def change(num):
    return -1*num
    
result=change(4)
print(result)