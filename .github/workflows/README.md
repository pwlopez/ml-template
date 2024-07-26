The steps taken in the actions workflow along with explanations of each stepp are define here.

### Steps:

#### Training pipeline triggered by pull request to main branch
    1. Login to AWS
    2. call preprocessing.py
    3. Upload processed data to S3
    4. build and push training dockerfile to AWS ECR
    5. call runner.py to initiate training job 
        - NOTE: default github timeout is 6 hours unless using a self-hosted runner
    6. download model object from S3
    7. call validate.py to run performance tests and write output as comment on PR
    
#### Deployment pipeline triggered by push to main branch
    1. build and push containerized Flask app to AWS ECR
    2. Deploy Flask app to ECS
    3. Call test_endpoint.py to validate deployment and model