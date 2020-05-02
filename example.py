import requests
#resp=(requests.get("https://allsportsapi.com/api/football/?met=Leagues&APIkey=2d272f5e7de38dcbe3c76361b9b16559b7cdea75940781642daeb76f1a48c341"))
k=''
#print(resp.json())
'''resp=resp.json()
for i in resp["result"]:
    if(i['country_name']=='India'):
        print(i['league_name'],i['league_key'],sep=' ')
#resp=(requests.get("https://allsportsapi.com/api/football/?met=Standings&APIkey=2d272f5e7de38dcbe3c76361b9b16559b7cdea75940781642daeb76f1a48c341&countryId=62"))
#resp=requests.get("https://allsportsapi.com/api/football/?met=Fixtures&APIkey=2d272f5e7de38dcbe3c76361b9b16559b7cdea75940781642daeb76f1a48c341&from=2019-10-21&to=2020-02-13&leagueId=240")
#resp=requests.get("https://allsportsapi.com/api/football/?met=H2H&APIkey=2d272f5e7de38dcbe3c76361b9b16559b7cdea75940781642daeb76f1a48c341&firstTeamId=2616&secondTeamId=2617"
#print(resp.json())
#resp=requests.get("https://allsportsapi.com/api/football/?met=H2H&APIkey=2d272f5e7de38dcbe3c76361b9b16559b7cdea75940781642daeb76f1a48c341&firstTeamId=9714&secondTeamId=3906")
#resp=requests.get("https://allsportsapi.com/api/football/?&met=Standings&leagueId=240&APIkey=2d272f5e7de38dcbe3c76361b9b16559b7cdea75940781642daeb76f1a48c341")
#resp=requests.get("https://allsportsapi.com/api/football/?&met=Videos&eventId=306171&APIkey=2d272f5e7de38dcbe3c76361b9b16559b7cdea75940781642daeb76f1a48c341")
resp=requests.get("https://allsportsapi.com/api/football/?&met=Odds&APIkey=2d272f5e7de38dcbe3c76361b9b16559b7cdea75940781642daeb76f1a48c341&countryid=62&from=2020-02-13&to=2020-02-13&leagueid=240")
print(resp.json())    

resp=requests.get("https://allsportsapi.com/api/football/?&met=Teams&leagueId=241&APIkey=2d272f5e7de38dcbe3c76361b9b16559b7cdea75940781642daeb76f1a48c341")
#print(resp.json())
res=resp.json()["result"]
c=[]
for i in res:
    c.append(i["team_name"])
print(c)
'''
def get_eventId(awayteam,hometeam,dateT,dateT1):
    
    resp=requests.get("https://allsportsapi.com/api/football/?met=Fixtures&APIkey=2d272f5e7de38dcbe3c76361b9b16559b7cdea75940781642daeb76f1a48c341&from="+dateT+"&to="+dateT1+"&countryId=62")
    
    
    print(resp)
    #print([(x["event_key"],x["event_date"],x["event_home_team"],x["event_away_team"],x["event_halftime_result"].encode('ascii', 'replace').decode('utf-8').replace('?',''),x["event_final_result"].encode('ascii', 'replace').decode('utf-8').replace('?','')) for x in resp.json()["result"]])
   
get_eventId('a','b','2019-11-27','2019-11-27')
'''
import argparse

from googleapiclient.discovery import build
from googleapiclient.errors import HttpError


# Set DEVELOPER_KEY to the API key value from the APIs & auth > Registered apps
# tab of
#   https://cloud.google.com/console
# Please ensure that you have enabled the YouTube Data API for your project.
DEVELOPER_KEY = 'REPLACE_ME'
YOUTUBE_API_SERVICE_NAME = 'youtube'
YOUTUBE_API_VERSION = 'v3'

def youtube_search(options):
  youtube = build(YOUTUBE_API_SERVICE_NAME, YOUTUBE_API_VERSION,
    developerKey=DEVELOPER_KEY)

  # Call the search.list method to retrieve results matching the specified
  # query term.
  search_response = youtube.search().list(
    q=options.q,
    part='id,snippet',
    maxResults=options.max_results
  ).execute()

  videos = []
  channels = []
  playlists = []

  # Add each result to the appropriate list, and then display the lists of
  # matching videos, channels, and playlists.
  for search_result in search_response.get('items', []):
    if search_result['id']['kind'] == 'youtube#video':
      videos.append('%s (%s)' % (search_result['snippet']['title'],
                                 search_result['id']['videoId']))
    elif search_result['id']['kind'] == 'youtube#channel':
      channels.append('%s (%s)' % (search_result['snippet']['title'],
                                   search_result['id']['channelId']))
    elif search_result['id']['kind'] == 'youtube#playlist':
      playlists.append('%s (%s)' % (search_result['snippet']['title'],
                                    search_result['id']['playlistId']))

  print 'Videos:\n', '\n'.join(videos), '\n'
  print 'Channels:\n', '\n'.join(channels), '\n'
  print 'Playlists:\n', '\n'.join(playlists), '\n'


if __name__ == '__main__':
  parser = argparse.ArgumentParser()
  parser.add_argument('--q', help='Search term', default='Google')
  parser.add_argument('--max-results', help='Max results', default=25)
  args = parser.parse_args()

  try:
    youtube_search(args)
  except HttpError, e:
    print 'An HTTP error %d occurred:\n%s' % (e.resp.status, e.content)
    '''
