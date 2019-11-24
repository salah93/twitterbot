pipeline {
    agent { dockerfile true }
    stages {
        stage('Run Test') {
            steps {
                sh 'env/bin/python setup.py test'
            }
        }
    }
}
