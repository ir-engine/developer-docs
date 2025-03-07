## Create IAM Roles for S3/SES/SNS (or a single admin role)

iR Engine interfaces with several AWS services and requires credentials for these purposes. You could make
one admin role with full access to all AWS services, but we recommend making separate, scoped roles for
each individual service. To create a role, do the following:

### Creating an IAM role
Go to IAM->Users, and click on the Add User button. For User Name, enter `<service>-admin`, e.g. `S3-admin`.
Check the box for Programmatic Access, the click on the Next:Permissions button.
Click on 'Attach existing policies directly'. In the Filter Policies text box, you'll want to
enter the name of the service to narrow down the policy list significantly. Then, look for the FullAccess
policy for that service and select that, and click the Next:Tags button. You don't need to tag it with
anything, just click the Next:Review button, then the Create User button.

The following screen should show Success and have the user listed. Copy the 'Access key ID' somewhere, and
also click the Show toggle under 'Secret access key' and copy that elsewhere as well. You will put these
into the Helm config file later.

### IAM Roles to create
Here are the services you want to create IAM admin users for, and the associated permissions you want to
grant them:
 
* S3: `AmazonS3FullAccess, CloudFrontFullAccess`
* SNS: `AmazonSNSFullAccess`

You'll also need to create an IAM user that GitHub Actions can use to access the cluster and push/pull
Docker images from ECR. By convention, we call this user 'EKSUser', and it needs these
permissions: `AmazonEKSClusterPolicy, AmazonEKSWorkerNodePolicy, AmazonEKSServicePolicy, AmazonElasticContainerRegistryPublicFullAccess, AmazonEC2ContainerRegistryFullAccess`

### Creating new credentials for an IAM user
If you ever lose the secret to a user, or want to make new credentials for whatever reason, go to
IAM->Users and click on that user. Click on the 'Security credentials' tab, and under 'Access keys' you
should see a button 'Create access key' and, underneath that, 0-2 existing keys with some information
about them and an 'x' on the far right to delete it. If there are two keys for that user, you 
must deactivate and delete one of them before making a new one.

Click the Create button, then make sure to save the public and secret keys somewhere and put them into
the Helm config file.

### Apply aws-auth with EKS user ARN to cluster

Only the IAM user who created the EKS cluster initially has access to the cluster, even if another
user has all of the required policies/permissions, up to and including the Admin policy. In order
for other users to have access to the cluster, the aws-auth ConfigMap in the cluster needs to be
modified to explicitly grant them permission to access the cluster.

There is an [`aws-auth.yaml`](https://github.com/ir-engine/ir-engine-ops/blob/master/configs/aws-auth-template.yml) file template in the configs folder of the [ir-engine-ops](https://github.com/ir-engine/ir-engine-ops/) repository.  
Make a copy of this template, shorten its name to `aws-auth.yml`, and run this command to get the current copy of the aws-auth ConfigMap:
```bash
kubectl describe configmap aws-auth -n kube-system
```

It should look something like this:
```yaml title="aws-auth.yml" showLineNumbers
Data
====
mapRoles:
----
- groups:
  - system:bootstrappers
  - system:nodes
  rolearn: arn:aws:iam::<accountId>:role/eksctl-ir-engine-test-nodegro-NodeInstanceRole-dXwOpisgTD1e
  username: system:node:{{EC2PrivateDNSName}}

mapUsers:
----
- groups:
  - system:masters
  userarn: arn:aws:iam::<accountId>:user/ir-engine-eks
  username: ir-engine-eks
```

Copy the value of `rolearn` in the entry for mapRoles and paste that in the template copy to replace `<rolearn>`.

In the mapUsers section, you'll need to make as many copies of the following as you want users to have access to the cluster:

```yaml
- groups:
  - system:masters
  userarn: arn:aws:iam::<account_id>:user/ir-engine-eks
  username: ir-engine-eks
```

:::important
Make sure to have an entry for the user who made the cluster.  
In the example above, that's `ir-engine-eks`.
:::

Replace `<account_id>` with the AWS account ID, and both instances of `<IAM_username>` with the username you want to grant access.

:::danger
You should NOT add any value for `{{EC2PrivateDNSName}}`. It will be evaluated by AWS in real-time.
:::

After the ConfigMap is ready, run this command to update the ConfigMap with the contents of `aws-auth.yml`.
```bash
kubectl apply -f <path/to/aws-auth.yml>
```

If you want to add a new user to the cluster, you will need to make another entry in the mapUsers section with their username and run:
 ```bash
 kubectl apply -f <path/to/aws-auth.yml>
 ```

You have to keep all of the other user entries, as the contents of the ConfigMap get replaced wholesale with whatever is in `aws-auth.yml`.
To remove a user's access from the cluster, remove their entry from mapUsers and run the above command to reapply the file.
