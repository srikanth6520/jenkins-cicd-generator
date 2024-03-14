import argparse
from jinja2 import Environment, FileSystemLoader
import os

def generate_build_pipeline(repo_url, branch, build_tool, docker_image, docker_tag, dockerhub_credentials_id, namespace, job_name, manifests_dir, kube_credentials_id):
    # Set up Jinja environment
    template_dir = os.path.join(os.path.dirname(__file__), 'templates')
    env = Environment(loader=FileSystemLoader(template_dir))
    
    # Load Jinja template
    template = env.get_template('template_file.j2')

    # Render template with provided inputs
    pipeline_script = template.render(
        GIT_REPO=repo_url,
        GIT_BRANCH=branch,
        BUILD_TOOL=build_tool,
        DOCKER_IMAGE=docker_image,
        DOCKER_TAG=docker_tag,
        DOCKERHUB_CREDENTIALS_ID=dockerhub_credentials_id,
        NAMESPACE=namespace,
        JOB_NAME=job_name,
        MANIFESTS_DIR=manifests_dir,
        KUBE_CREDENTIALS_ID=kube_credentials_id
    )

    return pipeline_script

def main():
    # Parse command-line arguments
    parser = argparse.ArgumentParser(description='Generate Jenkins pipeline file')
    parser.add_argument('-r', '--repo-url', type=str, help='Repository URL', dest='repo_url', required=True)
    parser.add_argument('-b', '--branch', type=str, help='Branch', dest='branch', default='main')
    parser.add_argument('-t', '--build-tool', type=str, help='Build tool', dest='build_tool', required=True, choices=['maven', 'gradle', 'npm', 'yarn'])
    parser.add_argument('--docker-image', type=str, help='Docker Image', dest='docker_image', default='my-docker-image')
    parser.add_argument('--docker-tag', type=str, help='Docker Tag', dest='docker_tag', default='latest')
    parser.add_argument('--dockerhub-credentials-id', type=str, help='Docker Hub Credentials ID', dest='dockerhub_credentials_id', default='dockerhub-credentials')
    parser.add_argument('-n', '--namespace', type=str, help='Namespace', dest='namespace', required=True)
    parser.add_argument('--job-name', type=str, help='Job Name', dest='job_name', default='test')
    parser.add_argument('--manifests-dir', type=str, help='Directory to store manifest files', dest='manifests_dir', default='manifests')
    parser.add_argument('--kube-credentials-id', type=str, help='Kubernetes Credentials ID', dest='kube_credentials_id', default='k8s-credentials')
    parser.add_argument('-o', '--output-file', type=str, help='Output file', dest='output_file', default='default_pipeline.groovy')
    
    args = parser.parse_args()

    # Generate Jenkins pipeline script
    pipeline_script = generate_build_pipeline(
        args.repo_url,
        args.branch,
        args.build_tool,
        args.docker_image,
        args.docker_tag,
        args.dockerhub_credentials_id,
        args.namespace,
        args.job_name,
        args.manifests_dir,
        args.kube_credentials_id
    )

    # Write the generated pipeline script to the output file
    with open(args.output_file, 'w') as f:
        f.write(pipeline_script)

if __name__ == "__main__":
    main()
