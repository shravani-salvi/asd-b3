pipeline {
 agent any
 triggers { pollSCM('H/5 * * * *') }
 stages {
 stage('Checkout') {
 steps { echo 'Pipeline checks out the configured repository.' }
 }
 stage('Build') {
 steps { echo 'Build stage'; bat 'echo Build completed' }
 }
 stage('Test') {
 steps { bat 'echo Tests completed' }
 }
 }
 post {
 success { echo 'Pipeline completed successfully.' }
 failure { echo 'Pipeline failed; inspect Console Output.' }
 }
}
