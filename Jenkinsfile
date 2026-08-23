pipeline{
  agent any
  stages{
    stage('checkout'){
      steps{
        checkout scm
      }
    }
    stage('build docker image'){
      steps{
        bat 'docker build -t tuts .'
      }
    }
    stage('deploy'){
      steps{
        bat 'docker stop containertuts || exit 0'
        bat 'docker rm containertut5 || exit 0'
        bat 'docker run -d -p 5400:5400 --name containertut5 tut5'
      }
    }
  }
}
