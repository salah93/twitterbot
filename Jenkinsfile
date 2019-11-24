pipeline {
    agent { dockerfile true }
    stages {
        stage('Run Test') {
            steps {
                sh 'cd /twitterbot'
                sh 'ls -l'
                sh 'pwd'
                sh 'ls -l /'
            }
        }
    }
}
