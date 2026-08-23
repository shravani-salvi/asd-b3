pipeline {
    agent any

    stages {
        stage('hello') {
            steps {
                echo "hello"
            }
        }

        stage('hello2') {
            steps {
                echo "hi"
            }
        }
    }
}
