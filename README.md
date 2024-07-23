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



## Data

Use this folder to store data.

## Data Processing

All of the data processing scripts are here. Add all of the preferred processing steps to the subsections listed in the main file.

## Model

Here we build our model. In this folder you should put any scripts, configs, etc for constructing your model. Additionally include the model training and validation scripts.

## Serve

This folder contains the core API used to serve the model. This API is model agnostic (mostly) and is able to handle a variety of model types.

## Test

Here are all the testing scripts. The scripts present in this file will be be called during the CI/CD process.