pipeline {
    agent { dockerfile true }
    stages {
        stage('Run Test') {
            steps {
                'env/bin/python setup.py test'
            }
        }
    }
}
