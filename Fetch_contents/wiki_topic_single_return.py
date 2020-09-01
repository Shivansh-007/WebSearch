import wikipediaapi, wikipedia


def wiki_search(main_topic):
    '''
    Called by start_fetching() function in main_search_topic.py
    Import and print topic chosen by the user using Wikipedia API and wikipedia.

    - main_topic: str
    '''

    print('============\nWIKIPEDIA\n============')
    wiki_main = wikipediaapi.Wikipedia('en')
    w = wikipedia.search(main_topic)[0]    ## use search to the chosen topic
#    print(w)

    page = wiki_main.page(w)
    sections = []
    for s in page.sections:
        sections.append(s.title)
    sections_list = []
    for n,s in enumerate(sections):
        if s.lower() == "see also":
            # TODO: Get links to other pages
            break
        sections_list.append(n)
    mylist = []
    total_list = []
    for x in range(0,len(sections_list)):
        temp = str(page.section_by_title(sections[x]))
        try:
            location = temp.index(".")
            temp = temp[0:location+1]
            if len(temp) <= 250:
                if temp.count("\n") <= 1:
                    temp_list = temp.split("\n")
                    total_list.append(temp_list)
        except:
            print("bad section(not text)")
    return total_list

if __name__ == "__main__":
    topic = input("what is your topic?: ")
    print(wiki_search(topic))
