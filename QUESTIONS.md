# General guideline

The purpose of the following questions is to assess your current knowledge in data engineering / database etc and your ability to come up with leads when you don't have experience.

In each case, motivate your suggestions by explaining why it fits the case. If you know popular solution which are NOT good fits for the problem at hand, please mention it since in practice, knowing a road is wrong has also a lot of value.

Don't only think and detail what you would be personally capable of implementing, put yourself in the shoes of a team member: you can count on the rest of the team so don't limit yourself to what you could do right now. We want to know what we should do as a team.

Overall, you should spend 2 to 4h answering this cases. If it takes you more time, it is that you're going into too much detail.

## Background information

### Vocabulary

A `sample` represents a physical sample of grain. They have a global reference in our system and a "client organization" reference (the reference in their own system)

An `acquisition` is a series of images taken on a sample at a given time with a given smartphone. Typical acquisition are composed of 4 .JPG (20% crompression) 12Mpx images, but some can have more images or larger ones.

A `label_instance` is some elementary information related to a particular sample. It can be a category (string in a pre-defined collection), a free text, a float, a json. The nature of the information is defined by its template

A `label_template` defines some possible information that users can _input_ about a sample. For example, a label template called "species" might define a categorical label that can take values in `{'wheat', 'soy', 'barley', 'rice'}` another template called "barley_specific_weight" can define a label which value is in Kg/L and contain any real value from 1 to 50.

A `scenario` is a pre-defined list of steps a user can do in our app. Steps include identification one (e.g. manual input of a sample reference, or barcode based), declaration steps (i.e. providing information about the sample, like the species or the specific weight), image capture steps (where images are taken) and result display steps where our models predictions are returned to the user.

A `prediction` is the result of running one of our models on a given acquisition. Outputs can be text, real numbers, json or pictures.

A `user_prediction` is the "summarized" value presented to the user following a prediction. It is a string (e.g. "species: SOY" or "Avg size: 42.0 mm")

### Core use-cases

Pocket Lab User (smartphone app), usually in a grain storage facility or at a farm

- The user opens the app and chooses a scenario
- The user identifies a sample he wants to measure
- The user inputs various label_instances
- The user takes pictures which are uploaded
- Our API runs predictions on the images and returns the user_predictions that are displayed to the user.

Inarix Data Science department, using a notebook or an automated pipeline script

- Connects through the pnx custom python library
- Looks for all samples of wheat uploaded by the client S*outh Agro. Corp* that have an associated label_instance deriving from the template "species" and have the value "barley".
- Lauches an overnight model training on this data (images + labels)

Portal User (web app)

- the client administrator wants to look at the whole activity for his company (number of samples per day, fraction of prediction under a given threshold etc.)
- the admin wants to be able to search for a specific sample and edit this information

## Cases

### Database & storage choice

Assume we have 100 users, each generating around 500 samples per year, through 10 scenarios and filling on average 3 label instance per samples (based on different 25 label templates)

**Q1.1: Based on the provided information, which type(s) of database(s) would you consider to store our informations ? Explain your choice.**

**Q1.2: What if we will soon have 1000 users, 100 scenario and 50 label templates?**

**Q1.3: What if we will soon have 10 000 users, 500 scenario and 300 label templates?**

### GPS Data-processing

When a user has uploaded its first image for a given scenario, the GPS position is uploaded in our database.

We want to use this GPS coordinates to be able to assign a "location" to the related acquisition. Locations are points of interest for our clients (like their plants, storage facilities, headquarters etc.). This location information will be used in the portal to be able to filter / organize their data by location.

Assume we have 100 out of 1000 clients that require this feature

**Q2.1 What would you suggest to do to implement the previous feature?**

**Q2.2 What if all clients want this feature?**

**Q2.3 About once every 2 years a client change its locations. How should we handle this event?**

### Image normalization & data augmentation

Because different smartphone have different sensors and image processing algorithms, we need to _normalize_ their images before sending them for prediction to our deep learning models. Normalization steps are a series of polynomial color correction, image rescaling, image compression and image cropping. The core normalizing functions only rarely change, but each smartphone type has a specific set of normalization parameters. Also, the normalization process is non-invertible (i.e. we cannot apply an inverse transform and recover the initial image)

When training/retraining models, we need to apply data augmentation to our input images to obtain stronger models. Data augmentation is a process where our regular standard images will be used to generate other "synthetic" images (usually, much more). Here we consider that for each image in the initial dataset we want to apply 5 random "denormalizations" (i.e. similar operations to normalization, but to generate more diverse images) and to create 5 artificial composites where 4 different images from different samples are mixed

Data normalization and augmentation operations do not require GPU. The transformation prototypes are given as python snippets by the Data Science team. Consider that a data augmentation step takes 5 second per image and that a normalization step takes 1 second (excluding file I/O).

**Q3.1 What would you suggest to do to implement the normalization ?**

**Q3.2 What would you suggest to do to implement data-augmentation ?**
