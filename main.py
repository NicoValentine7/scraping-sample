from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import os
from dotenv import load_dotenv
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

load_dotenv()


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
    time.sleep(1)

    # そこからさらにログインボタンをクリック
    login_login_button = driver.find_element(
        By.CSS_SELECTOR,
        ".button-border.header-user-status__button.-gray.-userPopup",
    )
    login_login_button.click()
    time.sleep(1)

    # iframeにスイッチ
    # 先頭に"piano-id"が付いているiframeを切り替える
    try:
        iframe_elements = driver.find_elements(By.TAG_NAME, "iframe")
        for iframe_element in iframe_elements:
            if "piano-id" in iframe_element.get_attribute("id"):
                driver.switch_to.frame(iframe_element)
                break
    except:
        print("iframeの切り替えに失敗しました")
        # すべてのiframeを表示
        iframe_elements = driver.find_elements(By.TAG_NAME, "iframe")
        print("iframeの数:", len(iframe_elements))
        for iframe_element in iframe_elements:
            print("iframeのid:", iframe_element.get_attribute("id"))
        driver.quit()
        return

    # 確認のためページのすべてのinput要素を取得して表示
    input_elements = driver.find_elements(By.CSS_SELECTOR, "input")
    for input_element in input_elements:
        print("type:", input_element.get_attribute("type"))  # type属性を表示
        print("name:", input_element.get_attribute("name"))  # name属性を表示

        # メールアドレスを入力
        # <input fieldloginemail="" type="text" pn-autofocus="" class="empty required" name="email" aria-label="メールアドレス" autocorrect="off" autocapitalize="off" data-sider-insert-id="8574189a-c842-43b3-99cd-09278d93adf6" data-sider-select-id="2741bc1b-32aa-47c1-96b0-c564901f4200">
        if input_element.get_attribute("name") == "email":
            print("メールアドレスを入力します......")
            input_element.send_keys(os.getenv("SHIKIHO_EMAIL"))

    driver.switch_to.default_content()


if __name__ == "__main__":
    driver = webdriver.Chrome()
    try:
        login(driver)  # ログイン処理
        # theme.run(driver)  # theme.pyのスクリプトを実行
    finally:
        time.sleep(3)
        driver.quit()
