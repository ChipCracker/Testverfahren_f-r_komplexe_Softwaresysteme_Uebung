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

        # Falls der es die Einstiegsseite ist
        if parent is None:
            current_node = self.url_tree[url] = {}
        else:
            current_node = parent[url] = {}

        # falls eine Element stale ist, soll bis zu 3-mal wiederholt geprüft werden, ob es nicht doch da ist
        attempts = 0
        while attempts < 3:
            try:
                # Hier werden alle <a> tags gesucht und in einer List gespeichert
                all_links = self.driver.find_elements(By.TAG_NAME, "a")
                # Iteriere über alle Links
                for link in all_links:
                    href = link.get_attribute('href')

                    # falls der Link bereits besucht wurde, soll dieser übersprungen werden
                    # kann auftreten, wenn auf verschieden pages dieselbe verlinkt wird
                    if href in self.visited_urls:
                        continue

                    # falls die url valide ist
                    if href and self.is_valid_url(href):
                        full_url = urljoin(url, href)
                        # falls die URL nicht schon gecrawlt wurde
                        if full_url not in self.visited_urls:
                            # rufe crawl auf
                            self.crawl(full_url, current_node)

                            # wenn fertig mit dem crawlen der seite, soll eine seite zurücknavigiert werden
                            if parent is not None:
                                self.driver.get(list(parent.keys())[0])
                break
            except StaleElementReferenceException:
                time.sleep(1)  # 1 Sekunde warten
                attempts += 1

    def is_valid_url(self, url):
        parsed_url = urlparse(url)
        return bool(parsed_url.scheme) and bool(parsed_url.netloc) and url.startswith(self.base_url)

    def close(self):
        self.driver.quit()

    def display_url_tree(self, tree=None, indent=0):
        if tree is None:
            tree = self.url_tree
        for url in sorted(tree):
            print(' ' * indent + url)
            self.display_url_tree(tree[url], indent + 4)


if __name__ == "__main__":
    BASE_URL = 'https://www.gym-oberasbach.de/start/aktuelles/'
    crawler = WebCrawler(BASE_URL)
    try:
        crawler.crawl(BASE_URL)
        crawler.display_url_tree()
        print(f"Total URLs visited: {len(crawler.visited_urls)}")
    finally:
        crawler.close()
