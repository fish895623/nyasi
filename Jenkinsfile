// node {
//     stage('Preparation') {
//         git 'https://github.com/fish895623/nyasi.git'
//     }
//     stage('Build') {
//         sh '''
//             echo "hello World"
//             echo "TEST2"
//         '''
//     }
// }
// pipeline{
//   // agent {
//   //     docker { image 'debian:latest' }
//   // }
//   // agent any
//   environment {
//     DOCKER = credentials('github.fish895623')
node {
  environment {
    DOCKER = credentials('github.fish895623')
  }
  stage('Parallel-test') {
    parallel 'Build-test-1' : {
      echo "build job : $DOCKER"
    }, 'Build-test-2' : {
      echo "build job : 'Build-test-2'"
    }, 'Build-test-3' : {
      echo "build job : 'Build-test-3'"
    }
  }
  stage('Build-test-4') {
    echo "build job : 'Build-test-4'"
  }
}