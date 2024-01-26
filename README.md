## AWS CI/CD Project

## Overview
This repository contains an AWS CI/CD project that leverages AWS CDK and Lambda functions to build a simple serverless application. The application, written in Python, increments a visit count stored in DynamoDB every time it receives a request.

## Prerequisites

Before deploying this project, make sure you have the following prerequisites installed and configured:

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