import pytest
from appium import webdriver
from appium.options.android import UiAutomator2Options  # 최신 방식의 옵션 객체
from selenium.webdriver.common.by import By
import time

APPIUM_SERVER_URL = "http://127.0.0.1:4723"

options = UiAutomator2Options()
options.platform_name = "Android"
options.device_name = "emulator-5554"  # 에뮬레이터 ID (adb devices로 확인 가능)
options.app = "/Users/jy/dev/app-release.apk"  # 실제 앱 경로로 변경


@pytest.fixture
def driver():
    driver = webdriver.Remote(command_executor=APPIUM_SERVER_URL, options=options)
    yield driver
    driver.quit()

def test_001(driver):
    # 버튼 클릭을 위한 XPath
    button_xpath = '//android.widget.Button[@content-desc="button_1"]'
    # 버튼을 찾고 클릭
    button = driver.find_element(By.XPATH, button_xpath)
    button.click()

    assert button.tag_name == "touch!", "버튼 클자가 변경됨"