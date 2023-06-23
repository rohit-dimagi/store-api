pipeline {
    agent any
    environment {
        ECR_REGISTRY="521558197391.dkr.ecr.ap-south-1.amazonaws.com"
        APP_REPO_NAME="store-api"
        AWS_REGION="ap-south-1"
        PATH="/usr/local/bin/:${env.PATH}"
    }
    stages {
        stage('Create ECR Repo') {            
            steps {
                echo "Creating ECR Repo for python app"
                sh 'aws ecr get-login-password --region ${AWS_REGION} | docker login --username AWS --password-stdin "$ECR_REGISTRY"'
                sh '''
                aws ecr describe-repositories --region ${AWS_REGION} --repository-name ${APP_REPO_NAME} || \
                         aws ecr create-repository \
                         --repository-name ${APP_REPO_NAME} \
                         --image-scanning-configuration scanOnPush=true \
                         --image-tag-mutability MUTABLE \
                         --region ${AWS_REGION}
                '''
            }
        }
        stage('Build Docker Image') {
            steps {
                sh 'docker build -t store-api .'
                sh 'docker image ls'
                sh 'docker tag store-api:latest "$ECR_REGISTRY/$APP_REPO_NAME":""$BUILD_ID""'
            }
        }
        stage('Push Image to ECR Repo') {
            steps {
                sh 'aws ecr get-login-password --region ${AWS_REGION}| docker login --username AWS --password-stdin "$ECR_REGISTRY"'
                sh 'docker push "$ECR_REGISTRY/$APP_REPO_NAME":""$BUILD_ID""'
            }
        }
    }

    post {
        always {
            echo 'Deleting all local images'
            sh 'docker image prune -af'
        }
    }
}
