pipeline {
  agent any
  environment {
      PATH = "C:/WINDOWS/SYSTEM32;C:/Users/famil/AppData/Local/Programs/Python/Python311;C:/Program Files/Docker/Docker/resources/bin;C:/Program Files/Git/cmd"
  }
  stages {
    stage('Testing app') {
      steps {
        bat 'python -m pip install --upgrade pip'
        bat 'python -m pip install -r requirements.txt'
//         bat 'python app.py'
        bat 'python test_main.py'
      }
    }
    stage('Docker deploy') {
      steps {
        bat 'docker build -t my-app .'
        bat 'docker run -d -p 8081:5000  my-app'
      }
    }
  }
}
