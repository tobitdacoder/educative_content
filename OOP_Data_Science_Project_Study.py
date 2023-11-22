

"""
Here, we have defined the Titanic class and an init method that takes the path to the Titanic dataset as input.
 When we try to create an object of the Titanic class, the following steps will happen:

- the class definition will be used to create an instance of the Titanic class
- the init method will read the Titanic dataset into a pandas dataframe and store it as an instance variable self.data.

"""
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, recall_score, precision_score, f1_score, roc_auc_score

class Titanic:

    # Load the Titanic dataset
    df = pd.read_csv("https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv")
    
    def __init__(self, df):
        self.df = df
        
    def clean_data(self):
        self.df.dropna(inplace=True)
        
    def engineer_features(self):
        self.df['family_size'] = self.df['SibSp'] + self.df['Parch'] + 1
        self.df = pd.get_dummies(self.df, columns=['Embarked', 'Sex', 'Cabin']) # convert categorical to numerical
        #self.df['TicketAlpha'] = df['Ticket'].str.extract('(\D+)')
        #self.df['TicketNum'] = df['Ticket'].str.extract('(\d+)')
        
        # drop unused columns
        self.df = self.df.drop(columns=['Name', 'Ticket'])
        
    def evaluate_model(self):
        X = self.df.drop(['Survived'], axis=1)
        y = self.df['Survived']
        
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)
        
        model = RandomForestClassifier(n_estimators=100, random_state=42)
        model.fit(X_train, y_train)
        y_pred = model.predict(X_test)
        
        accuracy = accuracy_score(y_test, y_pred)
        precision = precision_score(y_test, y_pred)
        recall = recall_score(y_test, y_pred)
        f1 = f1_score(y_test, y_pred)
        roc_auc = roc_auc_score(y_test, y_pred)
        
        print("Accuracy:", accuracy)
        print("Precision:", precision)
        print("Recall:", recall)
        print("F1 Score:", f1)
        print("AUC:", roc_auc)
        print(roc_auc)

        
######
import pandas as pd

# Create an instance of the Titanic class
titanic = Titanic(df)

# Clean the data
titanic.clean_data()

# Engineer features
titanic.engineer_features()

# Train and evaluate the model
titanic.evaluate_model()


        
