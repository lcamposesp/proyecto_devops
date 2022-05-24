pipeline{
    agent any
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
        stage('Finalizando'){
            steps{
                echo 'probando'
                echo 'agregando para el PR'
            }
        }
        stage('Deployment'){
            steps{
                echo 'Deployment'

            }
        
        }
    }
}