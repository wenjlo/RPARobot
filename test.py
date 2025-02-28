from selenium import webdriver
from multiprocessing import Pool


# I remove global driver because you cannot use shared driver in multiprocess.
def browser():
    driver = webdriver.Chrome()
    return driver


def test_func(link):
    driver = browser()  # Each browser use different driver.
    driver.get(link)


def multip():
    links = ["https://stackoverflow.com/", "https://signup.microsoft.com/"]
    pool = Pool(processes=3)
    for i in range(0, len(links)):
        pool.apply_async(test_func, args={links[i]})

    pool.close()
    pool.join()


if __name__ == '__main__':
    multip()



import time
import pandas as pd
from tools.auto import login,post,re_login
from config import usernames,password,emails
from fake_useragent import UserAgent
from selenium import webdriver
import multiprocessing
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from multiprocessing import Process, Pipe, Pool
from concurrent import futures

def browser():
    ua = UserAgent(os='windows',browsers='chrome')
    userAgent = ua.chrome
    print(userAgent)

    options = webdriver.ChromeOptions()
    options.add_experimental_option("detach", True)
    options.add_argument(f'user-agent={userAgent}')
    driver = webdriver.Chrome(options=options)
    return driver

def run_selenium_task(arg):
    """Function to run a Selenium task."""
    driver = browser()
    driver.get('https://x.com/i/flow/login')
    user,pwd= arg[0],arg[1]
    try:
        driver = login(driver,user,pwd)
    except:
        pass
    for data in [pd.read_csv('C:/data/文案.csv'),pd.read_csv(f'C:/data/{user}.csv')]:
        for _, d in data.iterrows():
            text = f"""
            {d['文案']}
            {d['tag']}
            """
            post(driver, d['檔名'], text)
            time.sleep(2)
            driver.get('https://x.com/home')






if __name__ == "__main__":
    def multip():
        accounts = [(user,pwd) for user,pwd in zip(usernames,password)]
        links = ["https://stackoverflow.com/", "https://signup.microsoft.com/"]
        pool = Pool(processes=3)
        for i in range(0, len(accounts)):
            pool.apply_async(run_selenium_task, args={accounts[i]})

        pool.close()
        pool.join()


    multip()