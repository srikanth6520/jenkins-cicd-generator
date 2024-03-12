import argparse
from jinja2 import Environment, FileSystemLoader
import os

def generate_build_pipeline(repo_url, branch, language, build_tool, namespace, deploy=True):
    # Set up Jinja environment
    template_dir = os.path.join(os.path.dirname(__file__), 'templates')
    env = Environment(loader=FileSystemLoader(template_dir))
    # Load Jinja template based on language
    if language == 'java':
        template = env.get_template('java_pipeline.j2')
    elif language == 'javascript':
        template = env.get_template('nodejs_pipeline.j2')
    else:
        raise ValueError(f'Unsupported language: {language}')

    # Render template with provided inputs
    pipeline_script = template.render(
        repo_url=repo_url,
        branch=branch,
        build_tool=build_tool,
        namespace=namespace,
        deploy=deploy
    )

    return pipeline_script

def main():
    # Parse command-line arguments
    parser = argparse.ArgumentParser(description='Generate Jenkins pipeline file')
    parser.add_argument('-r', '--repo-url', type=str, help='Repository URL', dest='repo_url', required=True)
    parser.add_argument('-b', '--branch', type=str, help='Branch', dest='branch', default='main')
    parser.add_argument('-l', '--language', type=str, help='Language', dest='language', required=True, choices=['java', 'javascript'])
    parser.add_argument('-t', '--build-tool', type=str, help='Build tool', dest='build_tool', required=True, choices=['maven', 'gradle', 'npm', 'yarn'])
    parser.add_argument('-n', '--namespace', type=str, help='Namespace', dest='namespace', required=True)
    parser.add_argument('-d', '--deploy', action='store_true', help='Deploy Helm chart', dest='deploy')
    parser.add_argument('-o', '--output-file', type=str, help='Output file', dest='output_file', default='default_pipeline.groovy')
    
    args = parser.parse_args()

    # Generate Jenkins pipeline script
    pipeline_script = generate_build_pipeline(
        args.repo_url,
        args.branch,
        args.language,
        args.build_tool,
        args.namespace,
        args.deploy
    )

    # Write the generated pipeline script to the output file
    with open(args.output_file, 'w') as f:
        f.write(pipeline_script)

if __name__ == "__main__":
    main()
