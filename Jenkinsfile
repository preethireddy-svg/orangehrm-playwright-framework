pipeline {
    agent any

    stages {

        stage('Clone Repo') {
            steps {
                git 'https://github.com/preethireddy-svg/orangehrm-playwright-framework'
            }
        }

        stage('Setup Python') {
            steps {
                sh 'python3 -m venv venv'
                sh 'source venv/bin/activate && pip install -r requirements.txt'
            }
        }

        stage('Install Playwright Browsers') {
            steps {
                sh 'source venv/bin/activate && playwright install'
            }
        }

        stage('Run Tests') {
            steps {
                sh 'source venv/bin/activate && pytest -v'
            }
        }
    }
}