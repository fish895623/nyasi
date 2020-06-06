node {
    stage('Preparation') {
        git 'https://github.com/fish895623/nyasi.git'
    }
    stage('Build') {
        sh '''
            docker build . -f ${WORKSPACE}/.devcontainer/Dockerfile -t fish895623/db:latest
            docker build . -f ${WORKSPACE}/.devcontainer/Dockerfile -t fish895623/db:${BUILD_ID}
        '''
    }
    stage('Push') {
        withCredentials([[$class: 'UsernamePasswordMultiBinding', credentialsId:'fish895623docker', usernameVariable: 'USERNAME', passwordVariable: 'PASSWORD']]) {
            sh '''
                docker login -u $USERNAME -p $PASSWORD
                docker push fish895623/db:latest
                docker push fish895623/db:${BUILD_ID}
                '''
        }
    }
}