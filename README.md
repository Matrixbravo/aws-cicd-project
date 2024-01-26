## AWS CI/CD Project

## Overview
This repository contains an AWS CI/CD project that leverages AWS CDK and Lambda functions to build a simple serverless application. The application, written in Python, increments a visit count stored in DynamoDB every time it receives a request.

## CI/CD Workflow: Deploy to AWS (CDK)

- Workflow Overview
The included GitHub Actions workflow automates the deployment of the AWS CDK stack on the main branch. The workflow consists of the following steps:

1. Checkout code:
    - Action: actions/checkout@v2
    - Purpose: Retrieve the source code for the workflow.
2. Set up Node.js:
    - Action: actions/setup-node@v2
    - Purpose: Set up Node.js for executing subsequent steps.
3. Cache Node.js dependencies:
    - Action: actions/cache@v2
    - Purpose: Cache Node.js dependencies to optimize subsequent builds.
4. Install CDK dependencies:
    - Action: Custom script
    - Purpose: Install AWS CDK dependencies using npm.
5. Deploy CDK stack:
    - Action: Custom script
    - Purpose: Deploy the AWS CDK stack with the specified configuration.
    - Conditions: Executes only if there is no cache hit.

## Prerequisites

Before deploying this project, make sure you have the following prerequisites installed and configured and ensure you have the necessary AWS credentials set up as GitHub secrets:

- BETA_AWS_ACCESS_KEY_ID
- BETA_AWS_SECRET_ACCESS_KEY_ID:

1. Node.js, npm, and AWS CDK:
    - Install Node.js
    - Install npm
    - Install AWS CDK globally:
        npm i -g aws-cdk
    - Initialize a new AWS CDK app in TypeScript:
        cdk init app --language typescript
    - Bootstrap the CDK environment in the desired AWS region (e.g., us-east-1):
        cdk bootstrap --region us-east-1

2. If you encounter an AWS account resolution error, ensure you have the AWS CLI installed and configured:

- Install AWS CLI
- Configure AWS CLI: `aws configure`
- Create an Access Key in AWS IAM and save the Access Key and Secret Access Key.
- Run `cdk bootstrap --region us-east-1` again.

- Bootstrapping creates necessary resources for AWS CLI and needs to be run only once per region.

## Lambda Function Code

The Python code in main.py defines a Lambda function that increments a visit count stored in DynamoDB and returns a response.

## CDK Stack Code

The CDK stack is defined in lib/aws-cicd-project.ts. It creates a DynamoDB table and a Lambda function, granting the necessary permissions.

## Deployment Output
After successfully deploying the stack, the CDK output will provide the URL endpoint for the Lambda function.