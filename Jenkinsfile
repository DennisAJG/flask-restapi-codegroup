pipeline {
    agent any

    environment {
        AWS_REGION = 'us-east-1'
        ECR_REPO_URL = '891612581071.dkr.ecr.us-east-1.amazonaws.com/flask-restapi-apps-codegroup'
        IMAGE_NAME = 'flask-restapi-example'
        IMAGE_TAG = 'latest'
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

        stage('Push Image to ECR') {
            steps {
                withCredentials([[
                    $class: 'AmazonWebServicesCredentialsBinding',
                    credentialsId: 'aws-credentials',
                    accessKeyVariable: 'AWS_ACCESS_KEY_ID',
                    secretKeyVariable: 'AWS_SECRET_ACCESS_KEY'
                ]]) {
                    sh '''
                    aws ecr get-login-password --region $AWS_REGION | docker login --username AWS --password-stdin $ECR_REPO_URL
                    docker push $ECR_REPO_URL:$IMAGE_TAG
                    '''
                }
            }
        }

        stage('Deploy to EC2') {
            steps {
                sshagent(['ssh-key-jenkins']) {
                    sh '''
                    ssh -o StrictHostKeyChecking=no ubuntu@ec2-54-196-122-229.compute-1.amazonaws.com << EOF
            
                    # Entrar no diretório de trabalho
                    cd /opt/apps
            
                    # Parar e remover qualquer container existente
                    docker-compose down || true
            
                    # Iniciar o serviço com Docker Compose
                    docker-compose up --build -d
                    EOF
                    '''
                }
            }
        }
    }
}
