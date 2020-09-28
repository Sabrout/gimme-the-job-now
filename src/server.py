import numpy as np
from flask import Flask, request, jsonify
import pickle
import sys, os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from src.utils import get_project_root
from model.wrapper import Wrapper
from model.model import MyModel
from model.model_example import ModelExample

'''
This script takes the JSON data so POST requests and it performs the prediction using loaded model and returns
the results in JSON format. It also shows how to use the Wrapper for the data science team.
'''

app = Flask(__name__)


# Load a MyModel by Inarix in the Wrapper
# model = Wrapper(MyModel)

# Load ModelExample by Me in the Wrapper
model = Wrapper(ModelExample)


@app.route('/api/predict',methods=['POST'])
def predict():
    # Get the data from the POST request.
    data = request.get_json(force=True)

    # Make prediction using model loaded using the Wrapper.
    prediction = model.predict([[np.array(data['x'])]])

    # Take the first value of prediction
    output = prediction
    
    return jsonify(output)


@app.route('/api/custom_predict',methods=['POST'])
def custom_predict():
    # Get the data from the POST request.
    data = request.get_json(force=True)
    
    # Make prediction using model loaded using the Wrapper.
    prediction = model.custom_predict([[np.array(data['x'])]])

    # Take the first value of prediction
    output = prediction

    return jsonify(output)


def main():
    try:
    	app.run(port=5000, debug=True)
    except:
    	print("[Error]: Server is shutdown unexpectedly.")

if __name__ == "__main__":
    main()
    