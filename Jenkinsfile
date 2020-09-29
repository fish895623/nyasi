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
pipeline{
    agent any
    environment {
        DOCKER_NAME = credentials('docker')
    }
    stages{
        stage("Git clone"){
            steps{
                git 'https://github.com/fish895623/nyasi.git'
            }
            post{
                always{
                    echo "========always========"
                }
                success{
                    echo "========A executed successfully========"
                }
                failure{
                    echo "========A execution failed========"
                }
            }
        }
    }
    post{
        always{
            echo "========always========"
        }
        success{
            echo "========pipeline executed successfully ========"
        }
        failure{
            echo "========pipeline execution failed========"
        }
    }
}