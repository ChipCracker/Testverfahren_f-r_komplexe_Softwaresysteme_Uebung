from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException, StaleElementReferenceException
from urllib.parse import urljoin, urlparse
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

class WebCrawler:
    def __init__(self, base_url):
        self.base_url = base_url
        self.visited_urls = set()
        self.url_tree = {}
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.implicitly_wait(10)

    def crawl(self, url, parent=None):
        self.driver.get(url)
        self.visited_urls.add(url)
        if parent is None:
            current_node = self.url_tree[url] = {}
        else:
            current_node = parent[url] = {}

        # Use a loop with a retry mechanism for handling StaleElementReferenceException
        attempts = 0
        while attempts < 3:
            try:
                all_links = self.driver.find_elements(By.TAG_NAME, "a")
                for link in all_links:
                    href = link.get_attribute('href')

                    # continue if link has already been visiteds
                    if href in self.visited_urls:
                        continue

                    if href and self.is_valid_url(href):
                        full_url = urljoin(url, href)
                        if full_url not in self.visited_urls:
                            self.crawl(full_url, current_node)

                            if parent is not None:
                                self.driver.get(list(parent.keys())[0])
                break  # If all operations are successful, break out of the loop
            except StaleElementReferenceException:
                time.sleep(1)  # Wait for a second before retrying
                attempts += 1  # Increment the attempt counter

    def is_valid_url(self, url):
        parsed_url = urlparse(url)
        return bool(parsed_url.scheme) and bool(parsed_url.netloc) and url.startswith(self.base_url)

    def close(self):
        self.driver.quit()

    def display_url_tree(self, tree=None, indent=0):
        if tree is None:
            tree = self.url_tree
        for url in sorted(tree):  # Sort URLs for consistent order
            print(' ' * indent + url)
            self.display_url_tree(tree[url], indent + 4)  # Correctly pass the nested dictionary

if __name__ == "__main__":
    BASE_URL = 'https://www.gym-oberasbach.de/start/aktuelles/'
    crawler = WebCrawler(BASE_URL)
    try:
        crawler.crawl(BASE_URL)
        crawler.display_url_tree()
        print(f"Total URLs visited: {len(crawler.visited_urls)}")
    finally:
        crawler.close()
