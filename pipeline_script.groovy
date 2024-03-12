pipeline {
    agent any

    parameters {
        string(name: 'GIT_REPO', defaultValue: 'https://github.com/srikanth6520/your-repo.git', description: 'Git Repository URL')
        string(name: 'GIT_BRANCH', defaultValue: 'main', description: 'Branch')
        choice(name: 'LANGUAGE', choices: ['java', 'javascript'], description: 'Language')
        choice(name: 'BUILD_TOOL', choices: ['maven', 'gradle', 'npm'], description: 'Build Tool')
        booleanParam(name: 'DEPLOY', defaultValue: false, description: 'Deploy Helm Chart')
    }

    stages {
        stage('Generate CI/CD Pipeline') {
            steps {
                script {
                    // Execute the Python script to generate the CI/CD pipeline script
                    def cmd = "python generate_pipeline.py -r ${params.GIT_REPO} -b ${params.GIT_BRANCH} -l ${params.LANGUAGE} -t ${params.BUILD_TOOL} -d ${params.DEPLOY} -o pipeline_script.groovy"
                    sh cmd
                }
            }
        }

        stage('Build and Deploy') {
            steps {
                // Load the generated pipeline script
                load 'pipeline_script.groovy'
            }
        }
    }
}
