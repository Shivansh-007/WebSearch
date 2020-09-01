from GoogleNews import GoogleNews
gn = GoogleNews()
def news_search(main_topic):
    '''
    Called by start_fetching() function in main_search_topic.py
    Import and print topic chosen by the user using Google News API.

    - main_topic: str
    '''
    print('============\nGOOGLE NEWS\n============')
    try:
        ## take title and link of the first 8 results
        gnews_dict = {}
        container_title = []
        container_link = []

        gn.search(main_topic)
        for el in gn.result():
            container_title.append(el['title'])
            container_link.append(el['link'])

        gnews_dict = list(zip(container_title, container_link))
        return gnews_dict
#        return [val for val in gnews_dict.values()]
    except Exception as exception:
        print(type(exception).__name__)

if __name__ == "__main__":
    topic = input("what is your topic?: ")
    print(news_search(topic))
