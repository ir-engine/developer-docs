# GitHub Fork
## Create GitHub fork of iR Engine repository.
The iR Engine codebase is most easily deployed by forking it and configuring some Secrets so that the included GitHub
Actions can run the deployment for you. You can run all of the commands that the `<dev/prod>`-deploy action runs manually
if you so choose, and in that case, you don't need to fork the GH repo.

Go to https://github.com/ir-engine/ir-engine. In the upper right-hand corner, there's a button 'Fork'. Click that,
then click the account/organization you wish to fork it to. You should be taken to your fork in a short time.

You'll need to set several Secrets (runtime variables) for GitHub Actions. By default GitHub Actions should be fully
enabled, but you can double-check by going to Settings->Actions. Allow All Actions should be selected under Actions
Permissions.

Next click on Secrets under Settings. There should be none by default. Click on New Repository Secret near the top of
this page to make a new one. You will need to make several Secrets with the following Names and Values:

* EKS_AWS_ACCESS_KEY -> The public Key of the EKSUser IAM user
* AWS_REGION -> The region of your ECR repos and EKS cluster
* EKS_AWS_SECRET -> The secret key of the EKSUser IAM user
* CLUSTER_NAME -> The name of the EKS cluster
* DEPLOYMENTS_ENABLED -> Set to `true`
* DEV_REPO_NAME -> The base name of the dev ECR repository, e.g. `ir-engine-dev` (all references to the builder and service repos will append `-builder`/`-<service>` to this value)
* DEV_REPO_URL -> The root URL for your repos, i.e. everything before the `/ir-engine-dev-builder`, e.g. `11111111111.dkr.ecr.us-west-1.amazonaws.com` or `public.ecr.aws/a1b2c3d4`. If pushing to Docker Hub, this should have `docker.io/` before the organization name, e.g. `docker.io/myorg .
* PRIVATE_REPO -> Set this to `true` if your repos are private; if they're public you don't need to set this at all.
* REPO_PROVIDER -> The provider of the container repos; currently allowed values are `aws` for ECR and `dockerhub` for Docker Hub.

If you go to the Actions Tab, you might see a few workflow runs with green checkmarks. If so, you'll be re-running the
`dev-deploy` workflow shortly; its initial run just ran a check to see if it should do a deployment based on 
`DEPLOYMENTS_ENABLED`, and since that wasn't set to true, it didn't do anything else. Now that that's set to true,
re-running it will trigger a deployment.
    
If you're asked to enable actions when going to the tab, and there are no runs listed after enabling actions, then you'll have to 
trigger the workflow by pushing new code to the dev branch.
