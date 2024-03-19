import argparse
from jinja2 import Environment, FileSystemLoader
import os

def generate_build_pipeline(repo_url, branch, build_tool, dockerfile_dir, docker_image, docker_tag, dockerhub_credentials_id, namespace, job_name, manifests_dir, kube_credentials_id):
    # Set up Jinja environment
    template_dir = os.path.join(os.path.dirname(__file__), 'templates')
    env = Environment(loader=FileSystemLoader(template_dir))
    
    # Load Jinja template based on the build tool
    if build_tool == 'maven':
        template = env.get_template('java_pipeline.j2')
    elif build_tool in ['npm', 'yarn']:
        template = env.get_template('nodejs_pipeline.j2')
    else:
        raise ValueError(f'Unsupported build tool: {build_tool}')

    # Render template with provided inputs
    pipeline_script = template.render(
        GIT_REPO=repo_url,
        GIT_BRANCH=branch,
        BUILD_TOOL=build_tool,
        DOCKERFILE_DIR=dockerfile_dir,
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
    parser.add_argument('--repo-url', type=str, help='Repository URL', default='https://example.com')
    parser.add_argument('--branch', type=str, help='Branch', default='main')
    parser.add_argument('--build-tool', type=str, help='Build tool', default='maven', choices=['maven', 'gradle', 'npm', 'yarn'])
    parser.add_argument('--dockerfile-dir', type=str, help='Directory where Dockerfile is located', default='path/to/dockerfiles')
    parser.add_argument('--docker-image', type=str, help='Docker Image', default='my-docker-image')
    parser.add_argument('--docker-tag', type=str, help='Docker Tag', default='latest')
    parser.add_argument('--dockerhub-credentials-id', type=str, help='Docker Hub Credentials ID', default='dockerhub-credentials')
    parser.add_argument('--namespace', type=str, help='Namespace', default='default')
    parser.add_argument('--job-name', type=str, help='Job Name', default='test')
    parser.add_argument('--manifests-dir', type=str, help='Directory to store manifest files', default='manifests')
    parser.add_argument('--kube-credentials-id', type=str, help='Kubernetes Credentials ID', default='k8s-credentials')
    parser.add_argument('--output-file', type=str, help='Output file', default='default_pipeline.groovy')

    args = parser.parse_args()

    # Generate Jenkins pipeline script
    pipeline_script = generate_build_pipeline(
        args.repo_url,
        args.branch,
        args.build_tool,
        args.dockerfile_dir,
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
