from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


def login(driver):
    # トップページにアクセス
    driver.get("https://shikiho.toyokeizai.net")
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located(
            (By.CSS_SELECTOR, ".button-square.header__button")
        )
    )

    # ヘッダーのログインボタンをクリック
    login_button = driver.find_element(
        By.CSS_SELECTOR,
        ".header__button-wrap .button-square.header__button.-small.-user.-g",
    )
    login_button.click()
    time.sleep(5)

    # そこからさらにログインボタンをクリック
    login_login_button = driver.find_element(
        By.CSS_SELECTOR,
        ".button-border.header-user-status__button.-gray.-userPopup",
    )
    login_login_button.click()
    time.sleep(5)


if __name__ == "__main__":
    driver = webdriver.Chrome()
    try:
        login(driver)  # ログイン処理
        # theme.run(driver)  # theme.pyのスクリプトを実行
    finally:
        driver.quit()
