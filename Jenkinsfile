pipeline{
    agent any
    stages{
        stage('Build'){
            steps{
                sh 'python -V'
                sh 'apt-install python-pip'
                sh 'pip install -U pytest
                echo 'Building'
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