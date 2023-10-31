

"""
Here, we have defined the Titanic class and an init method that takes the path to the Titanic dataset as input.
 When we try to create an object of the Titanic class, the following steps will happen:

- the class definition will be used to create an instance of the Titanic class
- the init method will read the Titanic dataset into a pandas dataframe and store it as an instance variable self.data.

"""
import pandas as pd 

class Titanic:

    def __init__(self,data_path):
        self.data=pd.read_csv(data_path)

    def preprocess_data(self):
        """Preprocess the data to handle missing values and convert categorical variables to numerical"""
        self.data.fillna(self.data.mean(), inplace=True) # fill missing values with mean
        self.data = pd.get_dummies(self.data, columns=['Embarked', 'Sex']) # convert categorical to numerical

        """
        With this class method defined, all we have to do in future to preprocess our data is to simply call 
        the function called preprocess_data and pass the object name as the argument. The entire logic and code
          of cleaning and preparing the data is now “abstracted” in the form of a simple to use method.
          
        """


        
