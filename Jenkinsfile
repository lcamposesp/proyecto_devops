pipeline{
    stages{
        stage('Build'){
            steps{
                sh 'python3 -V'
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