# Summary
This project was created to test the CI/CD chain. Everything will work according to the following principle: our website written in Python using Flask will be deployed to a locally deployed minikube using GitHub Actions and ArgoSD.

CI (github actions): when we push a new change to GitHub, the GitHub action is triggered and the process of building, testing and uploading a new version of the Docker Image to Docker Hub is launched.

CD (ArgoCD): ArgoCD looks at our deployment.yaml manifest and as soon as it is updated, the deployment process is launched to the minikube cluster.

‼️ Warning: this is a test project, the main purpose of which is to run this chain and see how it works. You should not use this approach in real projects, since many things were simplified here. For example, you should not keep manifest files in the same repository as the web service. ‼️

## Scheme:
![Diagram](https://i.ibb.co/TB6GWxCY/Screenshot-2.png)