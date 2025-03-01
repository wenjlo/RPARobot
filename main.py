from selenium import webdriver
from fake_useragent import UserAgent
from config import usernames,password
from tools.auto import login,post
import time
import pandas as pd

ua = UserAgent(os='windows',browsers='chrome')
userAgent = ua.chrome
print(userAgent)
options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
options.add_argument(f'user-agent={userAgent}')
driver = webdriver.Chrome(options=options)
driver.get('https://x.com/i/flow/login')

for u,p in zip(usernames,password):
        driver = login(driver, u, p)
        for data in [pd.read_csv('./data/文案.csv'),pd.read_csv(f'./data/{u}.csv')]:
            for _, d in data.iterrows():
                text = f"""
{d['文案']}
{d['tag']}
            """
                post(driver, d['檔名'], text)
                time.sleep(2)
                driver.get('https://x.com/home')