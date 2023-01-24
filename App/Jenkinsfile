pipeline {
    agent any
    environment {
	dockerhub=credentials('shinbidocker')
    }
    stages {
        stage('Checkout') {
            steps {
		bat 'git branch -d staging'
		bat 'git checkout -b staging'
		bat 'git push -u origin staging'
            }
        }
        stage('Building'){
            steps{
                bat 'pip install -r requirements.txt'
            }
        }
        stage('Testing'){
            steps{
                bat 'python -m unittest'
            }
        }
	stage('Deploying'){
            steps{
                bat 'docker build -t shinbi/mlops_tp5:latest .'
                bat 'docker run -d -p 8000:8000 shinbi/mlops_tp5:latest'
            }
        }
	stage('Pushing and Merging'){
		parallel {
			stage('Pushing Image') {
			    steps {
				bat 'docker logout'
				bat "echo $dockerhub_PWD | docker login -u $dockerhub_USR --password-stdin"
				bat 'docker push shinbi/mlops_tp5:latest'
				bat 'docker logout'
			    }
			}
			stage('Merging') {
			    steps {
				bat 'git checkout main'
				bat 'git merge origin/staging'
				bat 'git push -f origin main'
			    }
			}
		}
	}
    }
}
