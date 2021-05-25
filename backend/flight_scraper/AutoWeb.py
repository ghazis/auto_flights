import time
from dataclasses import dataclass
from transmitter import sendEmail
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.firefox.options import Options as FFOptions
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC

@dataclass()
class AutoWeb:
    url: str
    ff: bool = False
    headless: bool = False

    def start_session(self):
        options = FFOptions() if self.ff else Options()
        if self.headless: options.add_argument('--headless')
        dr = '/Users/ashhadghazi/scripts/python/webdrivers/geckodriver' if self.ff \
            else '/Users/ashhadghazi/scripts/python/webdrivers/chromedriver'
        self.br = webdriver.Firefox(executable_path=dr, options=options) if self.ff else webdriver.Chrome(dr, chrome_options=options)
        self.br.get(self.url)

    def get(self, url):
        self.br.get(url)

    def go_back(self):
        self.br.back()

    def refresh(self):
        self.br.refresh()

    def stop_session(self):
        self.br.quit()

    def get_key(self, key, only_check_if_special=False):
        key_map = {
            'up':    Keys.UP,
            'right': Keys.RIGHT,
            'down':  Keys.DOWN,
            'left':  Keys.LEFT,
            'enter': Keys.ENTER,
            'escape': Keys.ESCAPE
        }

        if only_check_if_special:
            return True if key in key_map.keys() else False
        return key_map[key] if key in key_map.keys() else key

    def get_by(self, by):
        by_map = {
            'id':                By.ID,
            'css':               By.CSS_SELECTOR,
            'name':              By.NAME,
            'xpath':             By.XPATH,
            'class':             By.CLASS_NAME,
            'link_text':         By.LINK_TEXT,
            'partial_link_text': By.PARTIAL_LINK_TEXT
        }

        return by_map[by]

    def element_exists(self, by, elem):
        by = self.get_by(by)
        return len(self.br.find_elements(by, elem))

    def get_element(self, by, elem):
        by = self.get_by(by)
        return WebDriverWait(self.br, 5).until(
                EC.presence_of_element_located((by, elem)))

    def get_elements(self, by, elem):
        by = self.get_by(by)
        return WebDriverWait(self.br, 5).until(
                EC.presence_of_all_elements_located((by, elem)))

    def get_element_text(self, elem, by):
        by = self.get_by(by)
        return WebDriverWait(self.br, 5).until(
                EC.presence_of_element_located((by, elem))).text

    def get_table_rows(self, by, elem):
        by = self.get_by(by)
        table = self.get_element(by, elem)
        return table.find_elements_by_tag_name('li')

    def notify(sbj, msg):
        email = "<email_address>"
        pwd = "<password>"
        sendEmail(email, pwd, [email], msg, sbj)

    def run_op(self, by, elem, op, op_value=''):
        by = self.get_by(by)
        if op == 'send':
            if not self.get_key(op_value, only_check_if_special=True):
                self.get_element(by, elem).clear()
            time.sleep(0.2)
            self.get_element(by, elem).send_keys(self.get_key(op_value))
        elif op == 'clear':
            self.get_element(by, elem).clear()
        elif op == 'click':
            self.get_element(by, elem).click()
        time.sleep(0.2)

    def run_ops(self, ops_map):
        for op in ops_map:
            self.run_op(op['by'], op['elem'], op['op'], op['op_value'])