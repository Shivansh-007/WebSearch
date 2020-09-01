from Fetch_contents.news_topic_single_return import news_search
#import Fetch_contents.news_topics_single_return as nk
#import wiki_topic_single_return as wk
from Fetch_contents.wiki_topic_single_return import wiki_search
from Fetch_contents.google_images import get_images
from Fetch_contents.dictionaryAPI_search import json_definition
from Fetch_contents.youtube_singleReturn import yt_searchtopic


# importing the module 
import wikipedia  
  
def summary_ex(topic):
    result = wikipedia.summary(topic) 
    return result 

def start_fetching(topic):
    '''
    Calls new_search() and wiki_search() functions
    '''
    topic = topic[0].upper() + topic[1:]
    my_dict = {"topic":topic}
    my_dict["google_news"] = news_search(topic)
    my_dict["wikipedia"] = wiki_search(topic)
    get_images(topic)
    my_dict["images"] = list(get_images(topic))
    my_dict["definition"] = json_definition(topic)
#    yt_searchtopic(topic)
    my_dict["youtube"] = yt_searchtopic(topic)
    my_dict["summary"] = summary_ex(topic)
    return my_dict

if __name__ == "__main__":
    topic = input('What argument are you looking for today? ')
    print(start_fetching(topic))
