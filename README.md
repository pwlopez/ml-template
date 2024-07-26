This is a template for ML projects including pipeline creation, CI/CD, and deployment.


### To Do:
- add data version control tools
    - write a guide for using DVC (Data Version Control)
    - include how to setup remote storage ex. AWS S3
- add data processing template: Partially Done
- add model building template
    - training
    - validation
- build github actions workflow for:
    - training
    - serving
- create Flask app for serving
    - include options for API Key
    - write deployment guide
- build dockerfile
- write tests scripts template for:
    - data format
    - data features
    - model info
    - API
- add config for destinations
    - AWS (start here)
    - AZURE
    - etc



### Data
---

Use this folder to store data.

### Data Processing
---
All of the data processing scripts are here. Add all of the preferred processing steps to the subsections listed in the main file.

- #### Contents:
    ##### cleaning.py
    - Put all the code used for cleaning the data in this file. This is not called in the training pipeline so it can be empty and is a placeholder to put any tranformative code.

    ##### exploration.py
    - This file can be used for the EDA process. It isn't a requirement as many people prefer using Jupyter notebooks but it is available.

    ##### preprocessing.py
    - This file is called in the training pipeline and must NOT be left empty. Add all the transformation functions to this file to prepare data for training.
---
### Model
---
Here we build our model. In this folder you should put any scripts, configs, etc for constructing your model. Additionally include the model training and validation scripts.

- #### Contents:

    ##### Deployment via AWS:
    * In order to run training jobs on AWS Sagemaker, we need:
        - container image
            * training script, which holds that actual model training steps and will vary depending on model used.
        - training script
            * this is to initiate the training job via the Sagemaker SDK and boto3 SDK.
        - shell script
            * this script accepts AWS credentials as input to build and push the container image to AWS ECR
        - dockerfile
            * blueprint for buidling the container image
    
    *NOTE: Currently, only AWS is supported for training jobs. Other options include Github runners (paid) and self hosted runners on preferred hyperscaler (also paid). 
    
    NOTE: These scripts are tailored to AWS*

    ##### train.py
    - This file holds the actual model training as if you were training a model locally. This is the main script run for the training job on AWS.

    ##### validate.py
    - Validate the model with held out data.

    ##### runner.py
    - This script intiates the training job on AWS.

    ##### dockerfile
    - Blueprint to build the training container image onto.

    ##### requirements.txt
    - These are the imports used for training the preferred model.
---
### Serve
---
This folder contains the core API used to serve the model. This API is model agnostic (mostly) and is able to handle a variety of model types.
---
### Test
---
Here are all the testing scripts. The scripts present in this file will be called during the CI/CD process.
