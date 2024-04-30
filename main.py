from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import os
from dotenv import load_dotenv

load_dotenv()


def access_top_page(driver):
    try:
        print("トップページにアクセスを試みます...")
        driver.get("https://shikiho.toyokeizai.net")
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located(
                (By.CSS_SELECTOR, ".button-square.header__button")
            )
        )
        print("トップページにアクセス成功")
    except Exception as e:
        print(f"トップページのロードに失敗しました: {e}")
        driver.quit()
        return False
    return True


def click_login_button(driver):
    try:
        print("ログインボタンをクリックします...")
        login_button = driver.find_element(
            By.CSS_SELECTOR,
            ".header__button-wrap .button-square.header__button.-small.-user.-g",
        )
        login_button.click()
        time.sleep(1)
        print("ログインボタンのクリック成功")
    except Exception as e:
        print(f"ログインボタンのクリックに失敗しました: {e}")
        driver.quit()
        return False
    return True


def click_login_login_button(driver):
    try:
        print("ログイン画面のログインボタンをクリックします...")
        login_login_button = driver.find_element(
            By.CSS_SELECTOR,
            ".button-border.header-user-status__button.-gray.-userPopup",
        )
        login_login_button.click()
        time.sleep(1)
        print("ログイン画面のログインボタンのクリック成功")
    except Exception as e:
        print(f"ログイン画面のログインボタンのクリックに失敗しました: {e}")
        driver.quit()
        return False
    return True


def switch_to_login_iframe(driver):
    try:
        print("ログイン用のiframeに切り替えます...")
        iframe_elements = driver.find_elements(By.TAG_NAME, "iframe")
        for iframe_element in iframe_elements:
            if "piano-id" in iframe_element.get_attribute("id"):
                driver.switch_to.frame(iframe_element)
                print("iframeへの切り替え成功")
                return True
    except Exception as e:
        print(f"iframeの切り替えに失敗しました: {e}")
    # すべてのiframeを表示
    iframe_elements = driver.find_elements(By.TAG_NAME, "iframe")
    print("iframeの数:", len(iframe_elements))
    for iframe_element in iframe_elements:
        print("iframeのid:", iframe_element.get_attribute("id"))
    driver.quit()
    return False


def input_email(driver):
    try:
        print("メールアドレス入力フィールドを探します...")
        input_elements = driver.find_elements(By.CSS_SELECTOR, "input")
        for input_element in input_elements:
            print("type:", input_element.get_attribute("type"))  # type属性を表示
            print("name:", input_element.get_attribute("name"))  # name属性を表示

            if input_element.get_attribute("name") == "email":
                print("メールアドレスを入力します...")
                input_element.send_keys(os.getenv("SHIKIHO_EMAIL"))
                print("メールアドレスの入力成功")
                return True
    except Exception as e:
        print(f"メールアドレスの入力に失敗しました: {e}")
        driver.quit()
        return False
    return False


def input_password(driver):
    try:
        print("パスワード入力フィールドを探します...")
        input_elements = driver.find_elements(By.CSS_SELECTOR, "input")
        for input_element in input_elements:
            if input_element.get_attribute("type") == "password":
                print("パスワードを入力します...")
                input_element.send_keys(os.getenv("SHIKIHO_PASSWORD"))
                print("パスワードの入力成功")
                return True
    except Exception as e:
        print(f"パスワードの入力に失敗しました: {e}")
        driver.quit()
        return False
    return False


# ログインをsubmitする
def submit_login(driver):
    try:
        print("ログインsubmit...")
        login_button = driver.find_element(
            By.CSS_SELECTOR,
            ".btn.prime",
        )
        login_button.click()
        time.sleep(1)
        print("ログインボタンのクリック成功")
    except Exception as e:
        print(f"ログインボタンのクリックに失敗しました: {e}")
        driver.quit()
        return False
    return True


def login(driver):
    if not access_top_page(driver):
        return
    if not click_login_button(driver):
        return
    if not click_login_login_button(driver):
        return
    if not switch_to_login_iframe(driver):
        return
    if not input_email(driver):
        return
    if not input_password(driver):
        return
    if not submit_login(driver):
        return
    print("ログインプロセス完了")
    driver.switch_to.default_content()


if __name__ == "__main__":
    driver = webdriver.Chrome()
    try:
        print("ログイン処理を開始します...")
        login(driver)
        print("ログイン処理が完了しました。")
    finally:
        print("ログインに成功しました")
        # print("theme.pyのスクリプトを実行します...")
        # theme.run(driver)
