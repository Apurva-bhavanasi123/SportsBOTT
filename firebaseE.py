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
##x=[('ISL',240),('I-league',241),('Calcutta Premier Division',242),('federation cup',243),('santosh trophy',9667),
  # ('hero super cup',9668),('Durand cup',10028)]
#x=[('jamshedpur',9723),('northeastutd',9722),("mumbai city",9068),('ATK',9714),('Hyderabad',16597),('Delhi dynamos',9831),
 #  ('goa',9071),('chennaiyin',9728),('Kerala blasters',9713),('Bengaluru',3906)
 #  ]
#x=[('Aizawl', '3901', 'https://allsportsapi.com/logo/3901_aizawl.png'), ('Mohun Bagan', '3902', 'https://allsportsapi.com/logo/3902_mohun-bagan.png'), ('Chennai City', '3903', 'https://allsportsapi.com/logo/3903_chennai-city.png'), ('Minerva', '3905', 'https://allsportsapi.com/logo/3905_minerva.png'), ('Churchill Brothers', '3907', 'https://allsportsapi.com/logo/3907_churchill-brothers.png'), ('East Bengal', '3909', 'https://allsportsapi.com/logo/3909_east-bengal.png'), ('Gokulam', '9856', 'https://allsportsapi.com/logo/9856_gokulam.png'), ('NEROCA', '9889', 'https://allsportsapi.com/logo/9889_neroca.png'), ('Indian Arrows', '9940', 'https://allsportsapi.com/logo/9940_indian-arrows.png'), ('Real Kashmir', '13794', 'https://allsportsapi.com/logo/13794_real-kashmir.png'), ('TRAU FC', '17223', 'https://allsportsapi.com/logo/17223_trau-fc.png')]
#x=[('Bengaluru', '3906', 'https://allsportsapi.com/logo/3906_bengaluru.png'), ('Mumbai City (Ind)', '9068', 'https://allsportsapi.com/logo/9068_mumbai-city-(ind).png'), ('Goa (Ind)', '9071', 'https://allsportsapi.com/logo/9071_goa-(ind).png'), ('Kerala Blasters', '9713', 'https://allsportsapi.com/logo/9713_kerala-blasters.png'), ('ATK', '9714', 'https://allsportsapi.com/logo/9714_atk.png'), ('North East Utd', '9722', 'https://allsportsapi.com/logo/9722_north-east-utd.png'), ('Jamshedpur', '9723', 'https://allsportsapi.com/logo/9723_jamshedpur.png'), ('Chennaiyin', '9728', 'https://allsportsapi.com/logo/9728_chennaiyin.png'), ('Delhi Dynamos', '9831', 'https://allsportsapi.com/logo/9831_delhi-dynamos.png'), ('Hyderabad', '16597', 'https://allsportsapi.com/logo/16597_hyderabad.png')]
#x=[('Mohun Bagan', '3902', 'https://allsportsapi.com/logo/3902_mohun-bagan.png'), ('East Bengal', '3909', 'https://allsportsapi.com/logo/3909_east-bengal.png'), ('Peerless', '3925', 'https://allsportsapi.com/logo/3925_peerless.png'), ('Calcutta Customs', '3928', 'https://allsportsapi.com/logo/3928_calcutta-customs.png'), ('Southern Samity', '3929', 'https://allsportsapi.com/logo/3929_southern-samity.png'), ('Rainbow', '3930', 'https://allsportsapi.com/logo/3930_rainbow.png'), ('Mohammedan', '3931', 'https://allsportsapi.com/logo/3931_mohammedan.png'), ('George Telegrapher', '11942', 'https://allsportsapi.com/logo/11942_george-telegrapher.png'), ('Aryan', '12066', 'https://allsportsapi.com/logo/12066_aryan.png'), ('BSS Sporting', '16015', 'https://allsportsapi.com/logo/16015_bss-sporting.png'), ('Kalighat', '16016', 'https://allsportsapi.com/logo/16016_kalighat.png'), ('Bhawanipore', '16017', 'https://allsportsapi.com/logo/16017_bhawanipore.png')]
#x=[('West Bengal', '11946', 'https://allsportsapi.com/logo/11946_west-bengal.png'), ('Delhi', '14644', 'https://allsportsapi.com/logo/14644_delhi.png'), ('Meghalaya', '14645', 'https://allsportsapi.com/logo/14645_meghalaya.png'), ('Goa FT', '14646', 'https://allsportsapi.com/logo/14646_goa-ft.png'), ('Services', '14647', 'https://allsportsapi.com/logo/14647_services.png'), ('Punjab', '14651', 'https://allsportsapi.com/logo/14651_punjab.png'), ('Karnataka', '14652', 'https://allsportsapi.com/logo/14652_karnataka.png'), ('Kerala FC', '17277', 'https://allsportsapi.com/logo/17277_kerala-fc.png'), ('Jharkhand', '17278', 'https://allsportsapi.com/logo/17278_jharkhand.png'), ('Mizoram', '17279', 'https://allsportsapi.com/logo/17279_mizoram.png')]
x=[('Chennai City', '3903', 'https://allsportsapi.com/logo/3903_chennai-city.png'), ('Bengaluru', '3906', 'https://allsportsapi.com/logo/3906_bengaluru.png'), ('Goa (Ind)', '9071', 'https://allsportsapi.com/logo/9071_goa-(ind).png'), ('ATK', '9714', 'https://allsportsapi.com/logo/9714_atk.png'), ('North East Utd', '9722', 'https://allsportsapi.com/logo/9722_north-east-utd.png'), ('Jamshedpur', '9723', 'https://allsportsapi.com/logo/9723_jamshedpur.png'), ('Chennaiyin', '9728', 'https://allsportsapi.com/logo/9728_chennaiyin.png'), ('Delhi Dynamos', '9831', 'https://allsportsapi.com/logo/9831_delhi-dynamos.png')]
for i in x:
    
    data =  {i[0]:i[1],
             'teamUrl':i[2]
         
          }
    result = firebase.post('/bot/SupercupTeams/', data)