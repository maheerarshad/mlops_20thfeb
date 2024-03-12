pipeline {
    agent any

    stages {
        stage('Build') {
            steps {
                echo 'Building the project...'
                sh 'make install'
            }
        }
        stage('Test') {
            steps {
                echo 'Running tests...'
                sh 'make test'
            }
        }
    }
}
