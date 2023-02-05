pipeline {
  agent any
  environment {
      PATH = "C:/WINDOWS/SYSTEM32;C:/Users/famil/AppData/Local/Programs/Python/Python311;C:/Program Files/Docker/Docker/resources/bin;C:/Program Files/Git/cmd"
  }
  stages {
    stage('Train model') {
      steps {
        bat 'python -m pip install --upgrade pip'
        bat 'python -m pip install Flask'
        bat 'python -m pip install requests'
        bat 'python -m pip install numpy'
        bat 'python -m pip install keras'
        bat 'python -m pip install https://storage.googleapis.com/tensorflow/mac/cpu/tensorflow-1.8.0-py3-none-any.whl'
        bat 'python app.py'
        bat 'python test_main.py'
      }
    }
    stage('Run flask app') {
      steps {
        bat 'python app.py'
      }
    }
    stage('Test API') {
      steps {
        bat 'python test_api.py'
      }
    }
  }
}
