# UID-Register@FSO Scrapper
This Python script performs web scraping on a specific website using Selenium and BeautifulSoup. 
It automates the process of entering letters into a search field, navigating through multiple pages of search results, and extracting data from each page.

# Installation:

## 1. Python
 You can install python 3 from https://www.python.org

## 2. Selenium

You can install selenium using Python Package manager.

command: pip install selenium


## 3. Chrome Webdriver

You can install webdriver for chrome browser for selenium from here : https://chromedriver.chromium.org/downloads

Note: Check your Chrome version before download


## 4. BeautifulSoup

You can install BeautifulSoup using Python Package manager.

command: pip install beautifulsoup4

# Script Overview

* The letter_values function generates a list of letter combinations from 'a' to 'z' and 'aa' to 'zz'.
* The get_proxy function retrieves a random proxy from a predefined list of proxies.
* The create_driver function sets up Chrome options and initializes a Chrome webdriver with proxy settings.
* The getData function performs the actual web scraping by entering letters into a search field, navigating through pages, and extracting data.
* he main function defines the URL and initiates the scraping process.

# Notes

* Adjust the delays (time.sleep) in the script according to your internet speed and website responsiveness.
* Uncomment the lines related to proxy usage if you want to use proxies for scraping.

# USE:
### step 1 : Clone the repository or download the script.

### step 2 : Install all the above modules.

### step 3 : Run the script using the following command: `python3 uid_register.py` and enjoy.


