# Report

The purpose of this document is to provide a quick overview over the work done for the Inarix technical exam. It also serves as a manual to run the scripts
and show results.


## Personal Note
First of all, I would like to thank the Inarix team for giving me the oppurtinity to do this exercise. Trying to shy away from clichés but I truly had 
an amazing chance to learn something new. Probably the first time since I graduated a year ago. Finally, I am a little disappointed I couldn't have 
more time to give a higher quality of a project.


## Manual
In order to run the app, place the desired model in the model folder while following the same structure as the Inarix given model or my model example.

Then, import your model in server.py to be variable model.
Next, run server.py
Finally, run interface.py for simple (terminal like) keyboard input commands
or write more requests in request.py for more testing.


## Implemented Files


### model_example.py
This script's purpose is to have an example model that can be manpulated to test the wrapper. It is a simple linear regression model over a dataset of a 2D array.
Such a basic model is used to show the workflow while being easy to replace or debug.
The example follows the exact function signatures as the Inarix model with further details to show how a member of the data science should distribute his model 
into multiple sections. It is important to note that either this model example or the Inarix model can be used for the Flask app but not both together.


### dataset.csv
A simple dataset that represents a linear function to be estimated by the model where f(x) = y


### model.pkl
A linear regression model trained over dataset.csv written using the module Pickle


### wrapper.py
This script is the main link between the models in the model folder or any future models and the Flask server. It works dynamically in wrapping the predict function or
any other future functions in the model. This wrapping results in having a "pre" function to be excuted before the predict function and a "post" function after the execution.

Most importantly, the output of each function (pre, predict, post) is ready to be used by the following function. For example, "post" takes the raw output of "predict" to 
do the post-processing.

Thus, the flow of warming-up the model, pre-processing input, predictionm and post-processing output is done automatically through the wrapper class.
All that is needed in the server is to call the "predict" function and the rest is handled.

Check print outputs in the model example for guidance.

Finally, the purpose of the "custom predict" function, or at least as far as I understood, is to perform a prediction wihtout the workflow (pre, predict, post). Hence, it
is defined inside the wrapper class to bypass the pre-processing and post-processing. This could come in handy for a specific model behavior that intersts the team.


### server.py
The script has a standard Flask server construction with routing URLs and POST requests to call the "predict" function of the wrapper (and not directly the model).
As written in the script, there are 2 POST functions to execute "predict" and "custom predict" which are shown in the interface commands later.


### request.py
A simple test for requests to be sent to the server and to print the reply.


### utils.py
A file that collects all trivial helper methods. Also, my plan was to put the compatibility for different operating systems but I ran out of time.


### interface.py
An input interface by written commands in the terminal for quick prediction using the server. These commands send requests to the server and then shows the output.
Examples:
    :PREDICT 5
    ...> [73545.90445964305]
    CUSTOM_PREDICT 1.8
    ...> [0]


## Answers to QUESTIONS.md

## Conclusion
