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
                python setup.py install
            }
        }
    }
}
