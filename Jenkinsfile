pipeline {
    agent {
        docker {
            image 'twitterbot'
        }
    }
    stages {
        stage('Run Test') {
            steps {
                sh 'echo hello'
            }
        }
    }
}
