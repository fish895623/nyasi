node {
    stage('Preparation') {
        git 'https://github.com/fish895623/nyasi.git'
    }
    stage('Build') {
        sh 'docker build . -f ${WORKSPACE}/.devcontainer/Dockerfile -t db:latest'
    }
    stage('Push') {
        sh 'docker push fish895623/DB:latest'
        sh 'docker push fish895623/DB:${BUILD_ID}'
    }
}
