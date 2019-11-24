pipeline {
    agent {
        docker {
            image 'twitterbot'
        }
    }
    stages {
        stage('Run Test') {
            steps {
                sh 'env/bin/python setup.py test'
            }
        }
    }
}
