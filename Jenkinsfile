pipeline {

    agent any

    stages {

        stage('Build Docker Image') {
            steps {
                bat 'docker build -t tut5 .'
            }
        }

        stage('Deploy') {
            steps {
                bat 'docker stop containertut5 || exit 0'
                bat 'docker rm containertut5 || exit 0'
                bat 'docker run -d -p 5000:5000 --name containertut5 tut5'
            }
        }
    }
}
