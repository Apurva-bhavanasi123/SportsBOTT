from firebase import firebase


firebase = firebase.FirebaseApplication('https://sports-chatbot-267305.firebaseio.com/', None)
data =  { 'url': 'John Doe',
          
          }
result = firebase.post('/python-example-f6d0b/memes/',data)
print(result)