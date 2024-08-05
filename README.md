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
        - store AWS credentials as github secrets
        - pass AWS credentials as environment variables to script
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
\
&nbsp;

---
### Getting Started

I highly recommend using some sort of Python version management such as Pyenv. Using Pyenv allows the user to generate an environment tied to a specific version of Python. At the very least, start with a virtual environment.

Using Pyenv:
```
# Create virtual environment
pyenv virtualenv 3.10 ml-template

# Activate virtual environment
pyenv activate ml-template
```
```
pyenv           - use Pyenv to create the virtual environemnt
virtualenv      - actual command to create the environment
3.10            - Python version to use, any can be specified
ml-template     - name of the virtual environment
activate        - activate the virtual environment
```

Using virtualenv:
```
# Create virtual environment
python -m venv ml-template

# Activate virtual environment
source ml-template/bin/activate
```
```
python          - use python
-m              - execute python code from the command line via modulename (more or less)
venv            - command to create virtual environment
ml-template     - name of the virtual environment
```

Both of the above are highly recommended and great options but I personally prefer Pyenv.

**NOTE: This is for bash/zsh**
\
&nbsp;

### Data

Use this folder to store data.
\
&nbsp;

---
### Data Processing

All of the data processing scripts are here. Add all of the preferred processing steps to the subsections listed in the main file.

- #### Contents:
    ##### cleaning.py
    - Put all the code used for cleaning the data in this file. This is not called in the training pipeline so it can be empty and is a placeholder to put any tranformative code.

    ##### exploration.py
    - This file can be used for the EDA process. It isn't a requirement as many people prefer using Jupyter notebooks but it is available.

    ##### preprocessing.py
    - This file is called in the training pipeline and must NOT be left empty. Add all the transformation functions to this file to prepare data for training.
\
&nbsp;

---
### Model

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
    - These are the imports used for training the preferred model. These libraries are installed in the docker container when it is built.
\
&nbsp;

---
### Serve
This folder contains the core API used to serve the model. This API is model agnostic (mostly) and is able to handle a variety of model types.
\
&nbsp;

---
### Test
Here are all the testing scripts. The scripts present in this file will be called during the CI/CD process.
\
&nbsp;

## Steps:
The steps involved with model building, testing, and deployment are define below.

1. Data handling

    The first step in any ML project is handling your data. There are 3 scripts made available to perform the intial cleaning of the data, along with exploratory analysis and preprocessing. Only of the provided scripts is required for the workflow, that is preprocessing.py. This is the first script called when the pipeline initiates and is responsible for transforming the supplied data into the correct features and format for model training.
\
&nbsp;

2. Model building

    This is the center piece of any ML project, the actual model development. Here the "model" folder is used to hold all of the required base scripts and utilities for setting up the model. The main focus of this folder is runner.py, the script called by the training pipeline to initiate the model training. When this happens, a training job will be created in AWS with the supplied files. train.py is the file AWS Sagemaker calls to initiate model training and this is where all of the required code will go. Here the model architecture is defined and all necessary steps around it such as train-test-split, are performed - all happening inside a docker container provided to AWS. The output from the training job is a tar file stored in S3. The model object is then downloaded from S3 and validated against a small subset of provided held-out data.
\
&nbsp;

3. Serving

    The final core step in the process is deploying the model to an endpoint. 