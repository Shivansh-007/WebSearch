import time
import webbrowser
import selenium
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver import ActionChains


def youtube_topic(yt_search):

	print('============\nYOUTUBE\n============')
	
	PATH = "C:\Program Files (x86)\chromedriver.exe"	## chrome executable on Windows
	options_chrome = Options()
	options_chrome.add_argument('headless')   ## no UI  
	#yt_search = input('What are you looking for in YouTube? ')

	## initialise the driver to youtube and open filters.
	DRIVER = webdriver.Chrome(PATH, options=options_chrome)
	DRIVER.get(f'https://www.youtube.com/results?search_query={yt_search}')
	time.sleep(3)
	filters = DRIVER.find_element_by_xpath('//*[@id="container"]/ytd-toggle-button-renderer')
	ActionChains(DRIVER).click(filters).perform()

	## try to locate the "last hour" button and click it.
	try:
	    filter_box = WebDriverWait(DRIVER, 10).until(EC.presence_of_element_located((By.XPATH,'//*[@id="collapse-content"]/ytd-search-filter-group-renderer[1]')))
	    news = filter_box.find_elements_by_xpath('//*[@id="collapse-content"]/ytd-search-filter-group-renderer[1]')

	    DRIVER.find_element_by_link_text('Last hour').click()
	finally:
	    pass

	## find into the page all vids and print title and url.
	main = WebDriverWait(DRIVER,10).until(EC.presence_of_element_located((By.ID, 'contents')))
	time.sleep(5)
	videos = main.find_elements_by_tag_name('ytd-video-renderer')

	##==========================
	container_titles = []
	container_urls = []
	vids = {}
	##==========================

	for video in videos[:10]:
	    video_title = video.find_element_by_id('video-title')
	    container_titles.append(video_title.text)
	    url = video.find_element_by_tag_name('a').get_attribute('href')
	    container_urls.append(url)

	vids = dict(zip(container_titles,container_urls))
	return vids

if __name__ == "__main__":
    topic = input("what is your topic?: ")
    print(youtube_topic(topic))
