node {
    withCredentials([usernameColonPassword(credentialsId: 'fish895623docker', passwordVariable: 'PWD', usernameVariable: 'USR')]) {
        stage('Preparation') {
            git 'https://github.com/fish895623/nyasi.git'
        }
        stage('Build') {
            sh 'docker build . -f ${WORKSPACE}/.devcontainer/Dockerfile -t fish895623/db:latest'
        }
        stage('Push') {
            sh 'docker login -u $USERPASS_USR -p $USERPASS_PWD'
            sh 'docker push fish895623/db:latest'
            sh 'docker push fish895623/db:${BUILD_ID}'
        }
    }
}