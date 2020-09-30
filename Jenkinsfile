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
        }
        stage("Docker Login"){
            steps{
                sh '''
                    docker run hello-world
                '''
            }
        }
    }
}