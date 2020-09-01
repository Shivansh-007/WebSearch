from googleapiclient.discovery import build

try:
	api_key = input("PASTE YOUR YOUTUBE API KEY HERE: ")
except:
	print("Youtube API Key Error. The API key hasn't been entered in yet, isn't correctly formatted as a string, or is invalidated.")
youtube = build('youtube', 'v3', developerKey= api_key)

def yt_searchtopic(topic, key=api_key, build_yt=youtube):

	request = youtube.search().list(
    part='snippet',
    maxResults=10,
    order='date',
    q=topic,
    relevanceLanguage='en')

	response = request.execute()	## stored as dictionary
	response_extracted = response['items']	## extract this key

	vids_urls = []
	for r in response_extracted[:9]:
		vid_url = r['id']['videoId']	## 'videoId' location in each response dictionary'\
		vid_title = r['snippet']['title']

		vids_urls.append(['https://www.youtube.com/embed/' + vid_url,vid_title])
	return vids_urls


test_api = True

if __name__ == '__main__':
	while test_api == True: 
		try:
			print('PASTE YOUR YOUTUBE API KEY HERE (no quotes needed): ')
			api_key = input()
			youtube = build('youtube', 'v3', developerKey= api_key)

			topic = input('>> Insert topic: ')
			print(yt_searchtopic(topic, api_key, build_yt=youtube))

			test_api = False

		except:
			print("Youtube API Key Error. The API key hasn't been entered in yet, isn't correctly formatted as a string, or is invalidated.\n")
