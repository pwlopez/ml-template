# Use boto3 to initiate the training job here. This script is called locally (or whatever machine you're working on). 
# Objects created from the training job will be stored in S3 as a tar file. Here we download the files from S3

import os
from sagemaker.estimator import Estimator

# These variables are passed from Github Secrets to this script in the Github Actions workflow
ROLE = os.env["AWS_ROLE"]
TRAINING_URI = os.env["ECR_REGISTRY"]
TRAINING_INSTANCE = os.env["TRAINING_INSTANCE"]

estimator = Estimator(
    image_name=TRAINING_URI,
    role=ROLE,
    train_instance_count=1,
    train_instance_type=TRAINING_INSTANCE,
)

estimator.fit(wait=True)