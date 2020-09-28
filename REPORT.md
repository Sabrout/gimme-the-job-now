# Report

The purpose of this document is to provide a quick overview over the work done for the Inarix technical exam. It also serves as a manual to run the scripts
and show results.


## Personal Note
First of all, I would like to thank the Inarix team for giving me the oppurtinity to do this exercise. Trying to shy away from clichés but I truly had 
an amazing chance to learn something new. Probably the first time since I graduated a year ago. Also, I would like to state that this is the first
time I have ever used Flask and built a class wrapper. Finally, I am a little disappointed I couldn't have more time to give a higher quality of a project.


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


### Database & storage choice

**Q1.1: Based on the provided information, which type(s) of database(s) would you consider to store our informations ? Explain your choice.**
As a start with a database of roughly 100 users and 50,000 images a year, the main focus would be probably on collecting information about the images without 
the need for a support for a wide base of users. My intuition in this case is to reduce the operation into image storage aside from selecting a database.
For example, most of the data about the images such as label_instances, label_templates, scenarios, user_pridictions are the main focus and the part to be
optimized with a database for mobile applications. Such database could be straightforward as a MySQL base or similar that can be easily managed by one or two admins
in the team.

On the other hand, it is better to store images in plain or compressed files rather than in a database. This way we will minimize the CPU usage and the number of operations
on uploading and downloading images. Also, training models would be directly on these folders which is a bonus to have an overall simpliciy.

**Q1.2: What if we will soon have 1000 users, 100 scenario and 50 label templates?**
With such scale, the focus will shift to be more analytical since a larger collection of label templates would be tempting to explore and discover patterns across clusters
of aquistions or groups of images. This process, which is the main player of a member of the data science team, requires a high transaction rate of executing a query multiple
times for pattern detection and implementing more sophoisticated models across the large base of users.

It is critical at this stage to select the kind of database since we don't want to be restricted by a database that can't scale up later. My opinion at this case
is to use HDFS on a Spark cluster. This way, we treat the problem of having the data scientist to excute a huge number of queries and occupy a lot of server usage by having
him or her analyze offline on Spark clusters. By doing this, we support a larger base of clients while not comprmising the abilities of data scientists to improve the platform.

**Q1.3: What if we will soon have 10 000 users, 500 scenario and 300 label templates?**
Coming to this stage of popularity where the transaction rate is massively increasing, the issue of down-time is becoming more and more important. So availability is a big
concern. However, the ability to quickly provide predictions or perform scenarios is equally important when a platform is that popular. In my humble opinion, I believe staying
on Spark while investing in more data engineers to optimize the platform is definitely an option especially when migrating a platform with that many users, scenarios and templates
can be a really expensive task.

Another option, which might be a bit overestimated, would be using Apache Cassandra, In this stage, managing massive data will be a never-ending task especially for a company
of the size of Inarix. Apache Cassandra is known to ease managing large amounts of data across many commodity servers, providing high availability with no single point of failure.
Nevertheless, I would be guessing more than providing a well-thoughtout solution since I have no experience regarding Apache Cassandra.


### GPS Data-processing

**Q2.1 What would you suggest to do to implement the previous feature?**

**Q2.2 What if all clients want this feature?**

**Q2.3 About once every 2 years a client change its locations. How should we handle this event?**


### Image normalization & data augmentation

**Q3.1 What would you suggest to do to implement the normalization ?**

**Q3.2 What would you suggest to do to implement data-augmentation ?**


## Conclusion
