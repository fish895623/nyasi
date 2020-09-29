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
        DOCKER = credentials('docker')
    }
    stages{
        stage("Git clone"){
            steps{
                // git 'https://github.com/fish895623/nyasi.git'
                sh "echo $DOCKER_USR $DOCKER_PSW"
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