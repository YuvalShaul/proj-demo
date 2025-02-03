pipeline {
    agent any
    
    stages {
        stage('Build') {
            steps {
                echo "Building for ${env.BRANCH_NAME}"
                // Common build steps
            }
        }
        stage ('Moshe'){
            steps{
                echo "This is step: Moshe"
                echo "(only a demo)"
            }
        }
        
        stage('Test') {
            agent {
                docker {
                    image 'python:3.9-slim'
                    args '-v $WORKSPACE:/scripts'  // Maps Jenkins workspace to /app in container
                }
            }
            steps {
                // Run on all branches
                sh """
                    pwd
                    ls -a
                    python /scripts/hello.py
                """


                    echo "Running unit tests for branch  ${env.BRANCH_NAME}"
            }

        }
        
        stage('Deploy') {
            when {
                branch 'main'
            }
            steps {
                // Production deployment steps
                echo "Deploying, branch: ${env.BRANCH_NAME}"
            }
        }
    }
}