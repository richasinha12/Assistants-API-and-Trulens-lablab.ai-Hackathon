from googleapiclient.discovery import build

def search_youtube_videos(query, max_results):
    api_key = "AIzaSyBxrj0UGS5pUrDXP5YRRlGsLpLYHirhC6s"
    youtube = build('youtube', 'v3', developerKey=api_key)

    request = youtube.search().list(
        q=query,
        part='snippet',
        type='video',
        maxResults=max_results
    )

    response = request.execute()

    video_links = []
    for item in response['items']:
        video_id = item['id']['videoId']
        video_links.append(f'https://www.youtube.com/watch?v={video_id}')

    return video_links


# query = "factorial of a number"
 
# max_results = 5

# videos = search_youtube_videos(query, max_results)
# for video in videos:
#     print(video)