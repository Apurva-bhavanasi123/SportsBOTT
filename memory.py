from firebase import firebase


firebase = firebase.FirebaseApplication('xxxxxxxxxxxxxxxx', None)
data =  { 'url': 'John Doe',
          
          }
result = firebase.post('/python-example-f6d0b/memes/',data)
print(result)
