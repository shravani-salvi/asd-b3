pipeline{
  agent any
   stages{
    stage('hello'){
      steps{
        echo "hello"
      }
     stage('hello'){
      steps{
        echo "hi"
      }
    }
  }
}
}
