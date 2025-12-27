pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Build & Test in Docker') {
            steps {
                sh 'docker build -t calculator-ci:${BUILD_NUMBER} .'
            }
        }
    }
}

