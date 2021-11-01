# AWS - CCP (Amazom Web Services - Certified Cloud Practitioner)

These notes were taken when I was studying for my [certification](https://github.com/ibrahima1289/kura-labs-academy/blob/main/certifications/aws-ccp/AWS-CCP-Certificate-Udemy.pdf) in Udemy tought by [Stephane M.](https://www.udemy.com/course/aws-certified-cloud-practitioner-new/)

## Types of Cloud

* **IaaS (Infrastructure as a Service)**
  * Provides networking, computers, data storage space
  * More flexible
  * Easy parallel with traditional on-premises IT
  
* **PaaS (Platform as a Service)**
  * No need for your organization to manage the underlying infrastructure
  * Focus on the deployment and management of your applications

* **SaaS (Software as a Service)**
  * Completed product that is run and managed by the service provider

## IAM 

* Users: have a password to access the AWS Console
* Groups: have users only
* Policies: JSON document that outlines permissions for users or groups
* Roles: are for EC2 instances or AWS services
* Security: MFA and Password Policy
* AWS CLI: manage your AWS services using the command-line
* AWS SDK: manage your AWS services using a programming language
* Access Keys: access AWS using the CLI or SDK
* Audit: IAM Credential Reports & IAM Access Advisor

## Computing

* **EC2**: Elastic Compute Service
* **ECS**: Elastic Container Service: Docker as a Service
* **EKS**: Elastic Kubernetes Service: Kubernetes as a service
* **Fargate**: [Fargate](https://docs.aws.amazon.com/AmazonECS/latest/userguide/what-is-fargate.html) is used to run containers in AWS
* **Lambda**: serveless [function](https://docs.aws.amazon.com/lambda/latest/dg/welcome.html) 
* **Elastic Beanstalk**: orchestrate AWS services
* **AWS Batch**: run [batch](https://docs.aws.amazon.com/batch/latest/userguide/what-is-batch.html) computing workloads.

## Storage

* **S3**: Simple Storage Service - object storage
* **S3 Glacier**: low cost storage for archieving long-term backup
* **Storaage Gateway**: hibrid cloud storage with local caching
* **EBS**: Elastic Block Storage: SSD, HDD
* **EFS**: Elastic File Storage
* **Snowball**: physically migrate massive data by using a computer suitcase: 50-80TB capacity
 * **Snowball Edge**: an improved verison of Snowball: 100TB capacity
 * **Snowmobile**: shipping container: pulled by a semi-trailer truch: 100PB capacity
 
## 
