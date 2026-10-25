pipeline {
    agent any
    triggers { pollSCM('H/5 * * * *') }
    stages {
        stage('Build') { 
         steps { bat 'echo Build completed.' } 
        }
        stage('Test')  { 
         steps { bat 'echo Tests completed.' } 
        }
    }
    post {
        success { echo 'Pipeline completed successfully!' }
        failure { echo 'Pipeline failed; check Console Output.' }
    }
}
