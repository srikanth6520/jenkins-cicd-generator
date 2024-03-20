# jenkins-cicd-generator

* Purpose:
This Python script generates a Jenkins pipeline script based on user-defined parameters. The Jenkins pipeline script is rendered using Jinja templates based on the specified build tool.

* Components:
* generate_build_pipeline Function:
This function takes various parameters related to the build process and generates the Jenkins pipeline script.
It loads Jinja templates based on the specified build tool and renders the template with the provided inputs.
The rendered pipeline script is returned.

* main Function:
This function is the entry point of the script.
It parses command-line arguments using the argparse module.
The parsed arguments are used to call the generate_build_pipeline function.
The generated pipeline script is written to the specified output file.

* Command-line Arguments:
--repo-url: Repository URL (default: 'https://example.com')
--branch: Branch name (default: 'main')
--build-tool: Build tool to use (default: 'maven', choices: ['maven', 'gradle', 'npm', 'yarn'])
--dockerfile-dir: Directory where Dockerfile is located (default: 'path/to/dockerfiles')
--docker-image: Docker image name (default: 'my-docker-image')
--docker-tag: Docker image tag (default: 'latest')
--dockerhub-credentials-id: Docker Hub Credentials ID (default: 'dockerhub-credentials')
--namespace: Namespace for Kubernetes deployment (default: 'default')
--job-name: Name of the Jenkins job (default: 'test')
--manifests-dir: Directory to store manifest files (default: 'manifests')
--kube-credentials-id: Kubernetes Credentials ID (default: 'k8s-credentials')
--output-file: Output file name for the generated Jenkins pipeline script (default: 'default_pipeline.groovy')

* Usage:
Execute the script with appropriate command-line arguments to generate the Jenkins pipeline script.
The generated pipeline script will be written to the specified output file.

* Notes:
Ensure that Jinja templates for different build tools (maven_pipeline.j2, gradle_pipeline.j2, nodejs_pipeline.j2) are available in the specified template directory.
Customize the templates as per your Jenkins pipeline requirements.
Make sure to have the necessary Docker and Kubernetes configurations set up for the pipeline to function correctly.





