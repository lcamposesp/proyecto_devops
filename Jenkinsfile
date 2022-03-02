pipeline{
    agent{ dockerfile true}
    stages{
        stage('Build'){
            steps{
                sh 'java -version'
                sh ''
                sh 'pip install -U pytest'
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