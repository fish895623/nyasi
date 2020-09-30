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
    // agent {
    //     docker { image 'debian:latest' }
    // }
    agent any
    environment {
        DOCKER = credentials('github.fish895623')
    }
    stages{
        stage("Git clone"){
            steps{
                // git 'https://github.com/fish895623/nyasi.git'
                sh '''
                    echo $DOCKER_USR $DOCKER_PSW
                '''
                script {
                    docker.build aa/abcd
                }
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
        stage("Docker Login"){
            steps{
                sh '''
                    docker run hello-world
                '''
            }
            post{
                always{
                    echo "====++++always++++===="
                }
                success{
                    echo "====++++only when successful++++===="
                }
                failure{
                    echo "====++++only when failed++++===="
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