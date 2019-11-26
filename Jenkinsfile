pipeline {
    agent { dockerfile true }
    stages {
        stage('Run Test') {
            steps {
                sh 'ls -l'
                sh 'pwd'
                sh 'ls -l /'
                sh '/twitterbot-virtualenv/bin/python setup.py test'
            }
        }
    }
}
