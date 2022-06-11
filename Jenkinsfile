pipeline {
   agent any

   stages{
     stage('build'){
         steps{
             bat 'call ./env/Scripts/activate.bat'
             bat 'pip install -r requirement.txt'
             bat 'python -m pytest tests -v -s'
         }
     }
   }
}