pipeline {
    agent any

    environment {
        PYTHON_PATH = tool name: 'Python3'
        PATH = "${PYTHON_PATH}/bin:${PATH}"
    }

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Setup Python Environment') {
            steps {
                sh '''
                    python -m venv venv
                    . venv/bin/activate
                    pip install -r requirements.txt
                '''
            }
        }

        stage('Run Tests') {
            steps {
                sh '''
                    . venv/bin/activate
                    pytest tests/ \
                        --html=reports/report.html \
//                         --junitxml=reports/junit.xml \
                        -v
                '''
            }
        }
    }

    post {
        always {
//             junit 'reports/junit.xml'
            publishHTML([
                allowMissing: false,
                alwaysLinkToLastBuild: true,
                keepAll: true,
                reportDir: 'reports',
                reportFiles: 'report.html',
                reportName: 'HTML Test Report'
            ])
        }
    }
}