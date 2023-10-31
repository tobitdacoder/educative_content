
import pandas as pd 

class Titanic:

    def __init__(self,data_path):
        self.data=pd.read_csv(data_path)
        
