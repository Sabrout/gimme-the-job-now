import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import pickle, requests, json
import sys, os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from src.utils import get_project_root, get_path
from model.model import MyModel, receive_model_input
from model.model_example import ModelExample, receive_model_input


class Wrapper(object):
    """ This class encapsulates any provided model that follows the conventions provided by Inarix
    such as warmup_model, pre_process, predict, post_process, custom predict, receive_model_input """

    def __init__(self,wrapped_class):
        # Initiate Wrapper 
        self.wrapped_class = wrapped_class()

        # Model Warm-up 
        self.wrapped_class.warmup_model()
        # Model Input
        self.inputs = receive_model_input()
    

    def __getattr__(self,attr):
        # introspection for returning a new wrapped function when the original attribute is callable
        orig_attr = self.wrapped_class.__getattribute__(attr)
        if callable(orig_attr):
            def hooked(*args, **kwargs):
                # functions to execute before
                self.pre()
                result = orig_attr(*args, **kwargs)
                # prevent wrapped_class from becoming unwrapped
                if result == self.wrapped_class:
                    return self
                # functions to execute after
                self.post(result) # added result as an argument to use raw output from predict
                return result
            return hooked
        else:
            return orig_attr


    def pre(self):
        # Pre-process Input Data
        self.preprocessed_data = self.wrapped_class.pre_process(self.inputs)


    def custom_predict(self, inputs):
        # Custom Predict function to be executed without pre() before it or post() after it
        return self.wrapped_class.custom_predict(inputs)
        

    
    def post(self, raw_output):
        # Post-process the raw output for a meaningful display
        self.processed_output = self.wrapped_class.post_process(raw_output)
        return self.processed_output
    

def main():
    # Test for Model by Inarix
    model = Wrapper(MyModel)
    model.predict([{'fileId': 1}, { 'fileId': 2}, {'fileId': 3}, {'fileId': 4}])

    # Test for Model Example by Me 
    model2 = Wrapper(ModelExample)
    model2.predict([[4.0]])
    model2.custom_predict([[7.0]])

if __name__ == "__main__":
    main()