node {
    stage('Preparation') {
        git 'https://github.com/fish895623/nyasi.git'
    }
    stage('Build') {
        sh 'docker build . -f ${WORKSPACE}/.devcontainer/Dockerfile -t fish895623/db:latest'
    }
    stage('Push') {
        withCredentials([[$class: 'UsernamePasswordMultiBinding', credentialsId:'fish895623docker', usernameVariable: 'USERNAME', passwordVariable: 'PASSWORD']]) {
            sh 'cf login some.awesome.url -u $USERNAME -p $PASSWORD'
            sh 'docker login -u $USERNAME -p $PASSWORD'
            sh 'docker push fish895623/db:latest'
            sh 'docker push fish895623/db:${BUILD_ID}'
        }
    }
}