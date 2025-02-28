from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from fake_useragent import UserAgent
from config import usernames,password,emails
from bs4 import BeautifulSoup
import time
import pandas as pd
ua = UserAgent(os='windows',browsers='chrome')
userAgent = ua.chrome
print(userAgent)

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
options.add_argument(f'user-agent={userAgent}')
driver = webdriver.Chrome(options=options)


def login(driver,user,pwd):

    wait = WebDriverWait(driver, 10)

    username = wait.until(
        EC.presence_of_element_located((By.CSS_SELECTOR, 'input[autocomplete=username]'))
    )

    username.send_keys(f"{user}")

    login_button = wait.until(
        EC.presence_of_element_located((By.CSS_SELECTOR, '[role=button].r-13qz1uu'))
    )

    login_button.click()

    password = wait.until(
        EC.presence_of_element_located((By.CSS_SELECTOR, '[type=password]'))
    )
    time.sleep(2)
    password.send_keys(f"{pwd}")

    login_button = wait.until(
        EC.presence_of_element_located((By.CSS_SELECTOR, '[data-testid*=Login_Button]'))
    )
    login_button.click()

    direct_message_link = wait.until(
        EC.presence_of_element_located((By.CSS_SELECTOR, '[data-testid=AppTabBar_DirectMessage_Link]'))
    )
    return driver




def post(driver,filename,text_detail):
    autotw1 = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CLASS_NAME, 'DraftEditor-root')))
    autotw1.click()

    tweet_input = driver.find_element(By.CSS_SELECTOR, "div.public-DraftStyleDefault-block")
    tweet_input.send_keys(text_detail)
    time.sleep(5)
    image_upload_input = driver.find_element(By.XPATH, "//input[@type='file']")
    image_upload_input.send_keys(f"C:/data/{filename}.mp4")
    time.sleep(2)
    # image_upload = WebDriverWait(driver,timeout=20).until(EC.element_to_be_clickable((By.XPATH,"//input[@type='file']")))
    # image_upload.send_keys(r"C:\Users\User\Downloads\preview.jpg")

    sendTw = WebDriverWait(driver, 5000).until(EC.element_to_be_clickable((By.CLASS_NAME, 'css-175oi2r.r-sdzlij.r-1phboty.r-rs99b7.r-lrvibr.r-1cwvpvk.r-2yi16.r-1qi8awa.r-3pj75a.r-1loqt21.r-o7ynqc.r-6416eg.r-1ny4l3l')))
    sendTw.click()

def reply(driver):
    driver.get('https://x.com/lo812829')
    html = driver.page_source
    soup = BeautifulSoup(html)

driver.get('https://x.com/i/flow/login')

for u,p,m in zip(usernames,password,emails):

        driver = login(driver, u, p)
        for data in [pd.read_csv('C:/data/文案.csv'),pd.read_csv(f'C:/data/{u}.csv')]:
            for _, d in data.iterrows():
                text = f"""
            {d['文案']}
            {d['tag']}
            """
                post(driver, d['檔名'], text)
                time.sleep(2)
                driver.get('https://x.com/home')
