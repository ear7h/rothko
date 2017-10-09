from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains



import requests as r

driver = webdriver.Chrome()
actions = ActionChains(driver)

driver.get("https://www.wikiart.org/en/mark-rothko")

try:
	WebDriverWait(driver, 1).until(
		EC.presence_of_element_located((By.CLASS_NAME, "st-masonry-tile"))
	)
finally:
	pass

while True:
	try:
		button = driver.find_element_by_class_name('btn-more')
		driver.execute_script("arguments[0].scrollIntoView();", button)
		WebDriverWait(driver, 1).until(
			EC.visibility_of(button)
		)
		button.click()
		continue
	except Exception:
		print('at bottom of page')
	break


tiles = driver.find_elements_by_class_name('st-masonry-tile')


def save_image(year, url):
	print('getting', url)
	arr = url.split("/")
	filename = "images/" + year + "-" + arr[len(arr) - 1]
	print('called', filename)

	res = r.get(url)
	with open(filename, 'wb') as fd:
	    for chunk in res.iter_content(chunk_size=128):
	        fd.write(chunk)

for tile in tiles:
	img_thumb_url = tile.find_element_by_tag_name('img').get_attribute('src')
	img_url = img_thumb_url.split("!")[0]
	img_url = img_url.replace('https', 'http')

	ul = tile.find_elements_by_tag_name('li')
	year = ul[1].get_attribute('innerHTML').split('·')[1].strip()

	save_image(year, img_url)

driver.close()