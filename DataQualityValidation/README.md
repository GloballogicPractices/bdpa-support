# GlobalLogic Data Platform - Data Quality & Validation Accelerator
The Data Quality and Validation Accelerator is a module under GL Data Platform which provides the component library required to perform different validation and quality checks. The components in the library are PySpark code that can be deployed and executed in any Spark environment like AWS Glue.

The accelerator allows the user to provide the required source, sink, transformations and validations on a source & target datasource through a simple YAML based configuration file. This module can help considerably reduce the effort required in developing custom integration and validation solutions.

In the following sections, we will explore deploying and running the GlobalLogic Data Quality & Validation Accelerator using the AWS CloudFormation template.

## Architecture
The accelerator includes a library of components that help perform data quality checks and validations across the source and target data sources. 

![template]( https://github.com/GloballogicPractices/bdpa-support/blob/dqv/images/DQV_Accelerator.png )

Following are some of the validations that can be performed:
- Check Data Completeness
- Check Schema / Metadata
- Check Data transformations
- Check Data Quality
- Check Data Integrity Constraints
- Validate Data Pipeline

## Prerequisites
Following are the pre-requisites that are required for deploying the accelerator.
- An AWS Account
- AWS Glue Spark cluster
- Amazon S3 bucket to store the raw data
- Access to the DQVA binary

## Deploy Automated Data Validation Pipeline using AWS CloudFormation
We will use the CloudFormation templates to create the necessary resources. Following topology architecture describes the services that will be deployed and consumed through the CloudFormation script.

![template]( https://github.com/GloballogicPractices/bdpa-support/blob/dqv/images/DPA_Topography_Architecture.drawio.png )

- Login to AWS management console and select the S3 service.
- Launch the AWS CloudFormation template with the following Launch stack button.

[![ ]( https://github.com/GloballogicPractices/bdpa-support/blob/dqv/images/cloudformation-launch-stack.png )]( https://console.aws.amazon.com/cloudformation/home?region=us-east-2#/stacks/new?stackName=create-glue-job&templateURL=https://s3.amazonaws.com/gl-dpa-dqva-bin/template/cfn_template.yaml )

- Choose the region e.g. US East (N. Virginia) Region (us-east-1)
- Add the details to the relevant parameters

|  Parameter Name | Description  |
| --------------- | ------------ |
|  CFNGlueAssetsS3Home | The S3 Bucket that will store the logs & temporary files. Update the AWS account number as applicable. *e.g. aws-glue-assets-123456789000-us-east-2* |
|  CFNJobName | Name of the Glue Job to be created. *e.g. dpa-validate-job* |
|  CFNPythonLibs | Path to the S3 bucket containing the accelerator binary. Dont change the default path. *e.g. s3://gl-dpa-dqva-bin/libs/dpa_fwk-1.2.0-min-py3-none-any.whl* |
|  CFNScriptLocation | Path to the script that will be executed in Glue. Dont change the default path. *e.g. s3://gl-dpa-dqva-bin/scripts/spark_validate_job.py* |

- Acknowledge the IAM resource creation and click on "Create" to create the CloudFormation stack.
- This AWS CloudFormation template creates the following resources in your AWS account:
  - An AWS Identity and Access Management (IAM) roles for accessing AWS Glue and Amazon S3.
  - An AWS Glue Job to validate the data across source (CSV files in S3) and target (Parquet files also in S3)
- When the AWS CloudFormation stack shows the status "CREATE_COMPLETE", you should be able to see the Glue Job "dpa-validate-job" in Glue Console
- In AWS Glue Console, update the script path to a bucket the user's account has access to and Save the job.
- Then click on the Run button to execute the Glue Job
- On successful completion of the job, follow the link to view "All Logs" to view the execution logs in CloudWatch.
- The validation results will be the last log record present in CloudWatch which details the validation done is a JSON format.

## Next Steps
The GL Data Quality and Validation accelerator provides a modular and scalable framework that can be deployed on cloud serverless Spark environments to validate a variety of sources. Reach out to us at dpa@globallogic.com on your needs and we would be happy to discuss with you on the next steps.
