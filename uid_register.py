import time
import random
from selenium import webdriver
from bs4 import BeautifulSoup
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException

def letter_values():
    # Generate a list of letter combinations from 'aa' to 'zz'
    letter_values = [chr(i) for i in range(ord('a'), ord('z') + 1)]
    new_letter_values = []
    for first in letter_values:
        for sec in letter_values:
            new_letter_values.append(f"{first}{sec}")
    return letter_values + new_letter_values

def get_proxy():
    # Define your list of proxies
    proxies = ["http://proxyuser:llxXB7NlzVT92wtLI8CaMa9H@101.53.132.243:1984"]
    # Select a random proxy from the list
    proxy = random.choice(proxies)
    return proxy

def create_driver(proxy):
    # Set up Chrome options
    chrome_options = webdriver.ChromeOptions()
    # Add proxy to Chrome options
    chrome_options.add_argument(f'--proxy-server={proxy}')
    # Initialize Chrome webdriver with options
    driver = webdriver.Chrome(options=chrome_options)
    return driver

def getData(url, letters):
    # Initialize Chrome webdriver
    driver = webdriver.Chrome()
    # If you want to use proxy, uncomment the following lines
    # proxy = get_proxy()
    # driver = create_driver(proxy)
    for letter in letters:
        all_rows = []
        # Open the URL
        driver.get(url)
        time.sleep(3)
        # Find the input field for entering letters
        elementID = driver.find_element(By.XPATH, '/html/body/form/div[6]/div[2]/div[2]/div/div[3]/div/div/div/div[5]/div/div[1]/div[2]/div[1]/div/div/div/input')
        elementID.send_keys(letter)
        # Click the search button
        driver.find_element(By.XPATH, """//*[@id="cphContent_btnSearch"]""").click()
        time.sleep(10)
        # Find the page count element
        page_count = driver.find_element(By.XPATH, "/html/body/form/div[6]/div[2]/div[2]/div/div[3]/div/div/div/div[7]/div/div/table/tfoot/tr/td/table/tbody/tr/td/div[5]/span[3]")
        # Extract the number of pages
        number = int(page_count.text.split()[-1]) if page_count.text else 2
        count = 0
        while True:
            count += 1
            try : 
                # Find the table containing data
                table_tag = driver.find_element(By.XPATH, '/html/body/form/div[6]/div[2]/div[2]/div/div[3]/div/div/div/div[7]/div/div/table/tbody')
                spage_source = table_tag.get_attribute("innerHTML")
                soup = BeautifulSoup(spage_source, 'lxml')
                # Find all rows in the table
                rows = soup.find_all("tr")
                all_rows = all_rows + rows
                if count == number:
                    break
                # Click the next page button
                driver.find_element(By.XPATH, "/html/body/form/div[6]/div[2]/div[2]/div/div[3]/div/div/div/div[7]/div/div/table/tfoot/tr/td/table/tbody/tr/td/div[3]/input[1]").click()
                time.sleep(4)
            except NoSuchElementException as e:
                print("Error : ", e)
                break
        for row in all_rows:
            # Find all table detail tags
            table_detail_tag = row.find_all("td")
            # Skip rows with less than 2 detail tags
            if len(table_detail_tag) <= 2:
                continue
            uid = table_detail_tag[1].text
            # Skip if UID is empty
            if not uid:
                continue
            try:
                new_url = f"https://www.uid.admin.ch/Detail.aspx?uid_id={uid}"
                # Open the new URL
                driver.get(new_url)
                time.sleep(10)
            except NoSuchElementException as e:
                print("Error : ", e)
                time.sleep(15)
                break

        time.sleep(10)  # Adjust the delay as needed

def main():
    url = "https://www.uid.admin.ch/Search.aspx"
    letters = letter_values()
    getData(url, letters)

# Main block
if __name__ == "__main__":
    main()
