from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ActionChains
from account import usernames,password
import time




options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
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




def post(driver):
    autotw1 = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CLASS_NAME, 'DraftEditor-root')))
    autotw1.click()

    tweet_input = driver.find_element(By.CSS_SELECTOR, "div.public-DraftStyleDefault-block")
    tweet_input.send_keys("sone-311")
    time.sleep(2)
    image_upload_input = driver.find_element(By.XPATH, "//input[@type='file']")
    image_upload_input.send_keys(r"C:\Users\User\Downloads\sone-311_preview.mp4")
    time.sleep(2)
    # image_upload = WebDriverWait(driver,timeout=20).until(EC.element_to_be_clickable((By.XPATH,"//input[@type='file']")))
    # image_upload.send_keys(r"C:\Users\User\Downloads\preview.jpg")

    sendTw = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CLASS_NAME, 'css-175oi2r.r-sdzlij.r-1phboty.r-rs99b7.r-lrvibr.r-1cwvpvk.r-2yi16.r-1qi8awa.r-3pj75a.r-1loqt21.r-o7ynqc.r-6416eg.r-1ny4l3l')))
    sendTw.click()


driver.get('https://x.com/i/flow/login')

for u,p in zip(usernames,password):
    try:
        driver = login(driver,u,p)
    except:
        wait = WebDriverWait(driver, 3)
        email = wait.until(
            EC.presence_of_element_located((By.CLASS_NAME, 'r-30o5oe.r-1dz5y72.r-13qz1uu.r-1niwhzg.r-17gur6a.r-1yadl64.r-deolkf.r-homxoj.r-poiln3.r-7cikom.r-1ny4l3l.r-t60dpp.r-fdjqy7'))
        )
        email.send_keys("lo812829@gmail.com")
        click_class = 'css-175oi2r.r-sdzlij.r-1phboty.r-rs99b7.r-lrvibr.r-19yznuf.r-64el8z.r-1fkl15p.r-o7ynqc.r-6416eg.r-icoktb.r-1ny4l3l'
        time.sleep(2)


        next_button = wait.until(
            EC.presence_of_element_located((By.CSS_SELECTOR, '[data-testid*=ocfEnterTextNextButton]'))
        )
        next_button.click()
        time.sleep(1)

        password = wait.until(
            EC.presence_of_element_located((By.CSS_SELECTOR, 'input[autocomplete=current-password]'))
        )
        time.sleep(2)
        password.send_keys("lo753951")

        # next_button = wait.until(
        #     EC.presence_of_element_located((By.CSS_SELECTOR, '[data-testid*=ocfEnterTextNextButton]'))
        # )
        # next_button.click()


        time.sleep(1)

        login_button = wait.until(
            EC.presence_of_element_located((By.CSS_SELECTOR, '[data-testid=LoginForm_Login_Button]'))
        )
        login_button.click()

        time.sleep(3)
    post(driver)
        # sendTw = WebDriverWait(driver, 3).until(EC.element_to_be_clickable((By.CLASS_NAME,click_class)))
        # sendTw.click()
