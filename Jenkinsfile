pipeline {
    agent { docker { image 'python:3.9-buster' } }
    stages {
        stage('build') {
            steps {
                sh 'python --version'
            }
        }
    }
}