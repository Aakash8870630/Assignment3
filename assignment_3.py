from selenium import webdriver
from selenium.webdriver.common.by import By

# Create a new instance of the Chrome driver
driver = webdriver.Chrome()

# Open YouTube.com
driver.get("https://www.youtube.com/")

# Test 1: Search for a video
search_box = driver.find_element(By.NAME, "search_query")
search_box.send_keys("Python tutorials")
search_box.submit()

# Test 2: Click on a video
video_link = driver.find_element(By.XPATH, '/html/body/ytd-app/div[1]/ytd-page-manager/ytd-search/div[1]/ytd-two-column-search-results-renderer/div/ytd-section-list-renderer/div[2]/ytd-item-section-renderer/div[3]/ytd-video-renderer[1]/div[1]/ytd-thumbnail/a')
video_link.click()
driver.implicitly_wait(20)

# Test 3: Check if the Like button is present
like_button = driver.find_element(By.XPATH, "/html/body/ytd-app/div[1]/ytd-page-manager/ytd-watch-flexy/div[5]/div[1]/div/div[2]/ytd-watch-metadata/div/div[2]/div[2]/div/div/ytd-menu-renderer/div[1]/ytd-segmented-like-dislike-button-renderer/yt-smartimation/div/div[1]/ytd-toggle-button-renderer/yt-button-shape/button")
if like_button.is_displayed():
    print("Like button is present")
else:
    print("Like button is not present")

# Test 4: Click on the skip button
skip_button = driver.find_element(By.CLASS_NAME, 'ytp-ad-skip-button-container')
skip_button.click()

# Close the browser
driver.quit()
