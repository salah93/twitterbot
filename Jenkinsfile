pipeline {
    agent {
        docker {
            image 'twitterbot'
        }
    }
    stages {
        stage('Run Test') {
            steps {
                'env/bin/python setup.py test'
            }
        }
    }
}
