pipeline {
    agent none 
    stages {
        stage('Build') { 
            agent {
                docker {
                    image 'twitterbot' 
                }
            }
            steps {
                sh 'python setup.py install'
            }
        }
    }
}
