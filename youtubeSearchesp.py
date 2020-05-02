def youtube_search(query):
    import random
    from googleapiclient.discovery import build
    from googleapiclient import discovery
    DEVELOPER_KEY = 'AIzaSyAhTGmRtQ_MOyEUZXqY2ywOhMAxWpHnSms'
    YOUTUBE_API_SERVICE_NAME = 'youtube'
    YOUTUBE_API_VERSION = 'v3'
    youtube = build(YOUTUBE_API_SERVICE_NAME, YOUTUBE_API_VERSION,
    developerKey=DEVELOPER_KEY)
    

  # Call the search.list method to retrieve results matching the specified
  # query term.
    search_response = youtube.search().list(
    q=query,
    part='id,snippet',
    maxResults=20
    ).execute()

    videos = []
  

  # Add each result to the appropriate list, and then display the lists of
  # matching videos, channels, and playlists.
    for search_result in search_response.get('items', []):
        if search_result['id']['kind'] == 'youtube#video':
            videos.append((search_result['snippet']['title'],
                                 search_result['id']['videoId'],search_result["snippet"]["thumbnails"]["medium"]["url"]))
    return random.choice(videos)

k=youtube_search('abck')