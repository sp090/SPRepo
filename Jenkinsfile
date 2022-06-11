pipeline {
   agent any

   stages{
     stage('build'){
         steps{
             bat 'python -m venv env'
             bat 'call ./env/Scripts/activate.bat'
//              bat 'call ./env/Scripts/activate'
             bat 'pip install -r requirement.txt'
             bat 'python -m pytest tests -v -s'
         }
     }
   }
}