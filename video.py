# -*- coding: utf-8 -*-
"""
Created on Tue Apr 21 08:13:05 2020

@author: Apoorva
"""
import requests

def video(eventId):
    k=eventId
    resp=requests.get("https://allsportsapi.com/api/football/?&met=Videos&eventId="+k+"&APIkey=2d272f5e7de38dcbe3c76361b9b16559b7cdea75940781642daeb76f1a48c341")

    return resp

def get_eventId(awayteam,hometeam,dateT):
    resp=requests.get("https://allsportsapi.com/api/football/?met=Fixtures&APIkey=2d272f5e7de38dcbe3c76361b9b16559b7cdea75940781642daeb76f1a48c341&from="+dateT+"&to="+dateT)
    print([x["event_key"] for x in resp.json()["result"]])
    from firebase import firebase
    firebase = firebase.FirebaseApplication('https://sports-chatbot-267305.firebaseio.com/', None)
    res=firebase.get('/bot/ISLTeams', '')
    res=[x for x in res.values() if(hometeam in x.keys())][0]
    print(res)

    print(res["Bengaluru"])
    print(res["teamUrl"])
    print(resp.json()["result"][0]["event_key"])
    videoId=resp.json()["result"][0]["event_key"]
    resp=requests.get("https://allsportsapi.com/api/football/?&met=Videos&eventId=306509&APIkey=2d272f5e7de38dcbe3c76361b9b16559b7cdea75940781642daeb76f1a48c341")
    print(resp.json())
get_eventId('Bengaluru','Bengaluru','2019-10-21')