pipeline{
    agent any
    stages{
        stage('Build'){
            steps{
                sh 'python3 -V'
                echo 'Building'
                sh 'pip3 -V'
                sh 'pip install flask'
            }
        }
        stage('Unit tests'){
            steps{
                echo 'Running unit tests'
            }
        }
        stage('Integration tests'){
            steps{
                echo 'Integration'
            }
        }
        stage('Deployment'){
            steps{
                echo 'Deployment'
            }
        }
    }
}