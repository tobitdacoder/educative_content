

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
        
