import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import pickle, requests, json
import sys, os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from src.utils import get_project_root, get_path

def receive_model_input():
    return pd.read_csv(get_path('\\bin\dataset.csv'))

class ModelExample(object):
    def __init__(self):
        pass

    def warmup_model(self):
        # Load saved Model
        """initially loading a model is by path, but it depends on the model storage convention by the team"""

        self.model = pickle.load(open(get_path('\\bin\model.pkl'),'rb'))
        print("[Progress]: Warm Up.")
    

    def pre_process(self, inputs):
        # Pre-process Input Data
        """it could be dataset filtering, PCA, Image pre-processing, Kernels, data-splits"""

        X = inputs.iloc[:, :-1].values
        y = inputs.iloc[:, 1].values
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.33, random_state = 0)

        print("[Progress]: Post Process.")
        return [X_train, X_test, y_train, y_test]


    def predict(self, inputs):
        print("[Progress]: Predict.")
        # Predict output using the loaded Model
        return self.model.predict(inputs).tolist()

    
    def post_process(self, raw_output):
        # Post-process the raw output for a meaningful display
        """change output format, display in an HTML or XML, apply image post-processing functions"""

        processed_output = []
        for i in raw_output:
            processed_output.append({'label': i})

        print("[Progress]: Post Process.")
        return processed_output
    

    def custom_predict(self, inputs):
        # Custom prediction function 
        """a dedicated predction routine for testing, parameter tuning or exception handling purposes
        that can involve a model or more so it's up to the data science team what to implement here
        example here: exception if output greater than 90000 return 0"""

        output = self.model.predict(inputs)

        print("[Progress]: Custom Predict.")
        if output > 9000:
            return [0]
        return output.tolist()

    

def main():
    # Testing Model 
    model = ModelExample()
    # Warm Up 
    model.warmup_model()
    # Data Split 
    _, X_test, _, _ = model.pre_process(receive_model_input())
    # Predict 
    print(model.predict(X_test))

if __name__ == "__main__":
    main()