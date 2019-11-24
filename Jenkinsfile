pipeline {
    agent { dockerfile true }
    stages {
        stage('Run Test') {
            steps {
                sh 'cd /twitterbot'
                sh 'env/bin/python setup.py test'
            }
        }
    }
}
