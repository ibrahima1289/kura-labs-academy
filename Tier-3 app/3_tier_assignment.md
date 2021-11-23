<h1 align=center>3 Tier assignment</h1>

## Goal:
The goal of this project is to create a [three-tier](https://docs.aws.amazon.com/whitepapers/latest/serverless-multi-tier-architectures-api-gateway-lambda/three-tier-architecture-overview.html) architecture application in an AWS VPC (Virtual Private Cloud). <br>

In the three-tier architecture, we have:
* **Data layer:** is the database where the data is stored.
* **Application layer:** This application layer is a [phpMyAdmin](https://www.phpmyadmin.net/) appication: it will manage the MySQL database hosted on AWS. 
* **Presentation layer:** Here, we have an NGINX application that act as a [reverse proxy](https://www.nginx.com/resources/glossary/reverse-proxy-server/) which helps the client access the backend.
* We will use [bastion](https://aws.amazon.com/quickstart/architecture/linux-bastion/) hosts to provide a secure access to the instances located in the private and public subnets of the VPC.

## Architecture:

## Software Tools Used:
In this project, we used AWS services listed below.
* EC2
* Internet Gateway
* Load Balancer
* Nat Gateway
* MySQL Database

## Precedure:

### Task 1

1. Create a VPC with a public subnet and private subnet using cloudFormation; here is the [yaml](https://docs.aws.amazon.com/codebuild/latest/userguide/cloudformation-vpc-template.html) file.<br>
Create **yaml** file named **base.yaml**; copy the content of the [yaml](https://docs.aws.amazon.com/codebuild/latest/userguide/cloudformation-vpc-template.html) file and paste it into the **base.yaml** file.<br>

  * The **base.yaml** file template will deploy:
    * a VPC, with a pair of public and private subnets spread across two Availability Zones 
    * an internet gateway, with a default route on the public subnets
    * a pair of NAT gateways (one in each AZ), and default routes for them in the private subnets
    
2. Now, save the **base.yaml** file locally.
3. Create a stack on cloudFormation.
```
CloudFormation -> Stacks -> Create stack
```
![](images/tier3-1.PNG)

4. Upload the **base.yaml** file.

![](images/tier3-2.PNG)

5. In the next page, give the stack a name

![](images/tier3-3.PNG)

6. We can see the parameters are the same as in the **base.yaml** file.
7. Select the **key pair** that will allow you to **ssh** into the differents **EC2**.

![](images/tier3-4.PNG)


* Create a new phpmyadmin EC2 and make sure it’s secure
* Create a Web proxy for caching and make sure it’s secure

### Task 2:

* Create an AWS load balancer to connect to your reverse proxy.
* 
### Task 3:

* Create a MySQL database on AWS by first creating a subnet group
* Select your vpc and subnets
* 
### Task 4:


## Sources:

1. https://jennapederson.com/blog/2021/6/21/provisioning-an-ec2-instance-with-cloudformation-part-1/
2. https://rdspg-monitoring.workshop.aws/en/prep/env/own-account.html
3. https://dev.classmethod.jp/articles/cloudformation-template-for-creating-ec2-with-load-balancer/
4. 
