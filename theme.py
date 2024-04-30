from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import time


def fetch_themes(driver):
    print("🚀 theme.pyのスクリプトを実行します...")
    url = "https://shikiho.toyokeizai.net/theme"
    driver.get(url)
    time.sleep(2)  # ページが完全にロードされるまで待機

    # テーマ名を含む要素を取得
    theme_elements = driver.find_elements(
        By.CSS_SELECTOR, ".theme-item-accordion__item span"
    )

    # テーマ名の表示とクリック
    for index in range(len(theme_elements)):
        # ページを再読み込みして要素を更新
        driver.get(url)
        time.sleep(5)
        theme_elements = driver.find_elements(
            By.CSS_SELECTOR, ".theme-item-accordion__item span"
        )
        element = theme_elements[index]

        print(element.text)  # テーマ名を表示
        element.click()  # テーマをクリック
        time.sleep(1)  # サブテーマがロードされるのを待つ

        # サブテーマの取得
        sub_theme_elements = driver.find_elements(
            By.CSS_SELECTOR, ".theme-item-accordion__items .-no-child span"
        )
        for sub_element in sub_theme_elements:
            print("  -", sub_element.text)  # サブテーマを表示
