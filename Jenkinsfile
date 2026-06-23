pipeline {
    agent any

    triggers {
        githubPush()
        // 每5分钟检查一次PR变化
        pollSCM('H/5 * * * *')
    }
    
    environment {
        PYTHONPATH = "${WORKSPACE}"
    }
    
    stages {
        stage('Checkout') {
            steps {
                echo "Checkout complete - using Branch Source, code already available"
            }
        }
        
        stage('Simple Test') {
            steps {
                sh '''
                    echo "Running simple test..."
                    python --version
                    ls -la
                    echo "Test completed successfully!"
                '''
            }
        }
    }
    
    post {
        success {
            echo 'Pipeline succeeded!'
        }
        failure {
            echo 'Pipeline failed!'
        }
    }
}
