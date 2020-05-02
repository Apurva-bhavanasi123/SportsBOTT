# -*- coding: utf-8 -*-
"""
Created on Sun Apr 19 15:42:49 2020

@author: Apoorva
"""

# -*- coding: utf-8 -*-
"""
Created on Sun Apr 19 15:00:28 2020

@author: Apoorva
"""

from firebase import firebase
firebase = firebase.FirebaseApplication('https://sports-chatbot-267305.firebaseio.com/', None)
x=[('ISL',240),('I-league',241),('Calcutta Premier Division',242),('federation cup',243),('santosh trophy',9667),
   ('hero super cup',9668),('Durand cup',10028)
   ]
for i in x:
    
    data =  {'Leaguename':x[0],
         'leagueId':x[1]
          }
    result = firebase.post('/bot/leagues/', data)