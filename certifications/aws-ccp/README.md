# AWS - CCP (Amazom Web Services - Certified Cloud Practitioner)

These notes were taken when I was studying for my [certification](https://github.com/ibrahima1289/kura-labs-academy/blob/main/certifications/aws-ccp/AWS-CCP-Certificate-Udemy.pdf) in Udemy tought by [Stephane M.](https://www.udemy.com/course/aws-certified-cloud-practitioner-new/) and from [Coursera](https://www.coursera.org/learn/aws-cloud-practitioner).

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

## Definitions

* An **edge location** is a site that Amazon CloudFront uses to store cached copies of your content closer to your customers for faster delivery.
* **Elastic Beanstalk** deploys the resources necessary to perform the following tasks:

  * Adjust capacity
  * Load balancing
  * Automatic scaling
  * Application health monitoring

* **AWS CloudFormation** provisions your resources in a safe, repeatable manner, enabling you to frequently build your infrastructure and applications without having to perform manual actions or write custom scripts.

* **AWS Outposts** is an extend AWS infrastructure and services to your on-premises data center. 

* **Amazon VPC** enables you to provision an isolated section of the AWS Cloud.

* A **subnet** is a section of a **VPC** in which you can group resources based on security or operational needs. Subnets can be **public** or **private**.
  
  * **Public subnets** contain resources that need to be accessible by the public, such as an online store’s website.
  * **Private subnets** contain resources that should be accessible only through your private network

* A **network access control list** (**ACL**) is a virtual firewall that controls inbound and outbound traffic at the subnet level.

  * **Network ACLs** perform **stateless** packet filtering. They remember nothing and check packets that cross the subnet border each way: inbound and outbound.

* A **security group** is a virtual firewall that controls inbound and outbound traffic for an Amazon EC2 instance.  
  
  * **Security groups** perform **stateful** packet filtering. They remember previous decisions made for incoming packets.

* [Amazon Route 53](https://aws.amazon.com/route53/) is a **DNS web service**. It gives developers and businesses a reliable way to route end users to internet applications hosted in AWS. 


## IAM and Security

* **Users:** have a password to access the AWS Console
* **Groups:** have users only
* **Policies:** JSON document that outlines permissions for users or groups
* **Roles:** are for EC2 instances or AWS services
* **Security:** MFA and Password Policy
* **AWS CLI:** manage your AWS services using the command-line
* **AWS SDK:** manage your AWS services using a programming language
* **Access Keys:** access AWS using the CLI or SDK
* **Audit:** IAM Credential Reports & IAM Access Advisor

* [AWS Artifact](https://aws.amazon.com/artifact/) is a service that provides on-demand access to AWS security and compliance reports and select online agreements.

* A **denial-of-service (DoS)** attack is a deliberate attempt to make a website or application unavailable to users.

* **AWS Shield** is a service that protects applications against DDoS attacks. AWS Shield provides two levels of protection: Standard and Advanced.

   * AWS Shield Standard automatically protects all AWS customers at no cost. It protects your AWS resources from the most common, frequently occurring types of DDoS attack. 

   * AWS Shield Advanced is a paid service that provides detailed attack diagnostics and the ability to detect and mitigate sophisticated DDoS attacks. 

* [AWS WAF](https://aws.amazon.com/waf/) is a web application firewall that lets you monitor network requests that come into your web applications.

* [AWS Key Management Service (AWS KMS)](https://aws.amazon.com/kms/) enables you to perform encryption operations through the use of cryptographic keys.

* [Amazon Inspector](https://aws.amazon.com/inspector/) helps to improve the security and compliance of applications by running automated security assessments.

* [Amazon GuardDuty](https://aws.amazon.com/guardduty/) is a service that provides intelligent threat detection for your AWS infrastructure and resources.

## Computing

* **EC2**: Elastic Compute Service
* **ECS**: Elastic Container Service: Docker as a Service
* **EKS**: Elastic Kubernetes Service: Kubernetes as a service
* **Fargate**: [Fargate](https://docs.aws.amazon.com/AmazonECS/latest/userguide/what-is-fargate.html) is used to run containers in AWS
* **Lambda**: serveless [function](https://docs.aws.amazon.com/lambda/latest/dg/welcome.html) 
* **Elastic Beanstalk**: orchestrate AWS services
* **AWS Batch**: run [batch](https://docs.aws.amazon.com/batch/latest/userguide/what-is-batch.html) computing workloads.

## Storage and Databases

* **S3**: Simple Storage Service - object storage (SSD)
* **S3 Glacier**: low cost storage for archieving long-term backup
* **Storaage Gateway**: hibrid cloud storage with local caching
* **EBS**: Elastic Block Storage: SSD, HDD
* **EFS**: Elastic File Storage
* **Snowball**: physically migrate massive data by using a computer suitcase: 50-80TB capacity
 * **Snowball Edge**: an improved verison of Snowball: 100TB capacity
 * **Snowmobile**: shipping container: pulled by a semi-trailer truch: 100PB capacity
 
* **Amazon Elastic Block Store (Amazon EBS - HDD)** is a service that provides block-level storage volumes that you can use with Amazon EC2 instances. If you stop or terminate an Amazon EC2 instance, all the data on the attached EBS volume remains available.

* **Amazon Elastic File System (Amazon EFS)** is a scalable file system used with AWS Cloud services and on-premises resources. As you add and remove files, Amazon EFS grows and shrinks automatically.  

* Comparing Amazon **EBS** and Amazon **EFS**: 
  
  * Amazon **EBS**:
    * An Amazon EBS volume stores data in a single Availability Zone. 
    * To attach an Amazon EC2 instance to an EBS volume, both the Amazon EC2 instance and the EBS volume must reside within the same Availability Zone.
  * Amazon EFS
    * Amazon EFS is a regional service. It stores data in and across multiple Availability Zones. 
    * The duplicate storage enables you to access data concurrently from all the Availability Zones in the Region where a file system is located. Additionally, on-premises servers can access Amazon EFS using AWS Direct Connect.

* **Amazon Relational Database Service (Amazon RDS)** is a service that enables you to run relational databases in the AWS Cloud.

* **Amazon DynamoDB** is a key-value database service. Serverless, Automatic Scaling.

* **AWS Database Migration Service (AWS DMS)** enables you to migrate relational databases, nonrelational databases, and other types of data stores.  

For more information, visit [AWS Database Blog](https://aws.amazon.com/blogs/database/).


## Monitoring and Analytics

* [Amazon CloudWatch](https://aws.amazon.com/cloudwatch/) is a web service that enables you to monitor and manage various metrics and configure alarm actions based on data from those metrics.

* [AWS CloudTrail](https://aws.amazon.com/cloudtrail/) records API calls for your account. The recorded information includes the identity of the API caller, the time of the API call, the source IP address of the API caller, and more. You can think of CloudTrail as a “trail” of breadcrumbs (or a log of actions) that someone has left behind them. 

* [AWS Trusted Advisor](https://aws.amazon.com/premiumsupport/technology/trusted-advisor/) is a web service that inspects your AWS environment and provides real-time recommendations in accordance with AWS best practices.
 

## Pricing and Support

* [AWS Free Tier](https://aws.amazon.com/free/)
* [AWS Pricing Calculator](https://calculator.aws/#/) lets you explore AWS services and create an estimate for the cost of your use cases on AWS. 
* The [consolidated billing](https://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/consolidated-billing.html) feature of AWS Organizations enables you to receive a single bill for all AWS accounts in your organization. 
* In [AWS Budgets](https://aws.amazon.com/aws-cost-management/aws-budgets/), you can create budgets to plan your service usage, service costs, and instance reservations.
* [AWS Cost Explorer](https://aws.amazon.com/aws-cost-management/aws-cost-explorer/) is a tool that enables you to visualize, understand, and manage your AWS costs and usage over time.
* [AWS Support Plans](https://aws.amazon.com/premiumsupport/plans/) help you troubleshoot issues, lower costs, and efficiently use AWS services. 


## Migration and Innovation

* [AWS Cloud Adoption Framework (AWS CAF)](https://d1.awsstatic.com/whitepapers/aws_cloud_adoption_framework.pdf) organizes guidance into six areas of focus, called Perspectives.
* Six of the most common [Migration Strategies](https://aws.amazon.com/blogs/enterprise-strategy/6-strategies-for-migrating-applications-to-the-cloud/).
* [ AWS Snow Family](https://aws.amazon.com/snow/) is a collection of physical devices that help to physically transport up to exabytes of data into and out of AWS.

## The Cloud Journey

* The [AWS Well-Architected Framework](https://d1.awsstatic.com/whitepapers/architecture/AWS_Well-Architected_Framework.pdf) helps you understand how to design and operate reliable, secure, efficient, and cost-effective systems in the AWS Cloud.

* Operating in the AWS Cloud offers many benefits over computing in on-premises or hybrid environments.<br>
There are (about) six advantages of cloud computing:

  * Trade upfront expense for variable expense.
  * Benefit from massive economies of scale.
  * Stop guessing capacity.
  * Increase speed and agility.
  * Stop spending money running and maintaining data centers.
  * Go global in minutes.

## Exam Details

* [Exam Guide](https://d1.awsstatic.com/training-and-certification/docs-cloud-practitioner/AWS-Certified-Cloud-Practitioner_Exam-Guide.pdf).

* [ AWS Certified Cloud Practitioner website](https://aws.amazon.com/certification/certified-cloud-practitioner/).



# Sources:

1. https://www.udemy.com/course/aws-certified-cloud-practitioner-new/
2. https://www.coursera.org/
