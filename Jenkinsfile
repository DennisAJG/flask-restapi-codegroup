pipeline {
    agent any

    environment {
        ECR_REPO_URL = "891612581071.dkr.ecr.us-east-1.amazonaws.com/flask-restapi-apps-codegroup" // Substituído automaticamente pelo Terraform
        IMAGE_NAME = 'flask-restapi-example'
        IMAGE_TAG = 'latest'
        AWS_REGION = 'us-east-1'
    }

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Build Docker Image') {
            steps {
                sh 'docker build -t $IMAGE_NAME:$IMAGE_TAG .'
            }
        }

        stage('Tag Image') {
            steps {
                sh 'docker tag $IMAGE_NAME:$IMAGE_TAG $ECR_REPO_URL:$IMAGE_TAG'
            }
        }

        stage('Login to ECR') {
            steps {
                sh '''
                aws ecr get-login-password --region $AWS_REGION | docker login --username AWS --password-stdin $ECR_REPO_URL
                '''
            }
        }

        stage('Push Image to ECR') {
            steps {
                sh 'docker push $ECR_REPO_URL:$IMAGE_TAG'
            }
        }

        stage('Deploy to EC2') {
            steps {
                sshagent(['ssh-key-jenkins']) {
                    sh '''
                    ssh -o StrictHostKeyChecking=no ubuntu@ec2-54-196-122-229.compute-1.amazonaws.com << EOF
                    aws ecr get-login-password --region $AWS_REGION | docker login --username AWS --password-stdin $ECR_REPO_URL
                    docker pull $ECR_REPO_URL:$IMAGE_TAG
                    docker stop flask-app || true
                    docker rm flask-app || true
                    docker run -d --name flask-app -p 5000:5000 $ECR_REPO_URL:$IMAGE_TAG
                    EOF
                    '''
                }
            }
        }
    }

    post {
        always {
            cleanWs()
        }
    }
}