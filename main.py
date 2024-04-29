from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time

# WebDriverのセットアップ
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

try:
    # WebページのURL
    url = "https://shikiho.toyokeizai.net/theme"
    driver.get(url)

    # ページが完全にロードされるまで待機
    time.sleep(5)  # 必要に応じて調整してください

    # テーマ名を含む要素を取得
    theme_elements = driver.find_elements(
        By.CSS_SELECTOR, ".theme-item-accordion__item span"
    )

    # テーマ名の表示
    for element in theme_elements:
        print(element.text)

finally:
    # ブラウザを閉じる
    driver.quit()
