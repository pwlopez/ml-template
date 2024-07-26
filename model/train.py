# imports


def train(**kwargs):

    # Train Test Split

    # Fit model

    # Save model

    pass

def main():
    # Accept arguments via CLI for model training. All of these will be provided when initiate the training job.

    train()

if __name__ == "__main__":
    main()

    """
    /opt/ml/model – Your algorithm should write all final model artifacts to this directory. SageMaker 
    copies this data as a single object in compressed tar format to the S3 location that you specified 
    in the CreateTrainingJob request. If multiple containers in a single training job write to this 
    directory they should ensure no file/directory names clash. SageMaker aggregates the result in a 
    TAR file and uploads to S3 at the end of the training job.

    https://docs.aws.amazon.com/sagemaker/latest/dg/your-algorithms-training-algo-output.html
    """