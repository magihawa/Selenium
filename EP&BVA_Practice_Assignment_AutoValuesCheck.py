from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(service=ChromeService(
    ChromeDriverManager().install()))

link = "https://qa-ep-bva-practice-assignment.vercel.app/"


def NoneCheck():
    btn.click()
    alert = driver.switch_to.alert
    alert_txt = alert.text
    print(alert_txt)
    alert.accept()


forms_and_buttons = [
    ("div:nth-child(6)>.input-group>.form-control",
     "div:nth-child(6)>.input-group>button"),
    ("div:nth-child(7)>.input-group>.form-control",
     "div:nth-child(7)>.input-group>button"),
    ("div:nth-child(8)>.input-group>.form-control",
     "div:nth-child(8)>.input-group>button"),
    ("div:nth-child(9)>.input-group>.form-control",
     "div:nth-child(9)>.input-group>button"),
    ("div:nth-child(10)>.input-group>.form-control",
     "div:nth-child(10)>.input-group>button"),
    ("div:nth-child(11)>.input-group>.form-control",
     "div:nth-child(11)>.input-group>button"),
    ("div:nth-child(12)>.input-group>.form-control",
     "div:nth-child(12)>.input-group>button"),
    ("div:nth-child(13)>.input-group>.form-control",
     "div:nth-child(13)>.input-group>button"),
    ("div:nth-child(14)>.input-group>.form-control",
     "div:nth-child(14)>.input-group>button"),
    ("div:nth-child(15)>.input-group>.form-control",
     "div:nth-child(15)>.input-group>button"),
    ("div:nth-child(16)>.input-group>.form-control",
     "div:nth-child(16)>.input-group>button"),
    ("div:nth-child(17)>.input-group>.form-control",
     "div:nth-child(17)>.input-group>button")
]

total_forms = len(forms_and_buttons)

try:
    driver.get(link)
    values = [-10000, -9999, 10000, 9999, 0, "     ", -
              10001, 10001, "Letters", "Буквы", "#%&*"]
    for index, (form_selector, btn_selector) in enumerate(forms_and_buttons):
        print(index+1)
        for value in values:
            driver.execute_script("window.scrollBy(0, 20);")
            x = driver.find_element(
                By.CSS_SELECTOR, form_selector)
            x.clear()
            x.send_keys(value)
            btn = driver.find_element(
                By.CSS_SELECTOR, btn_selector)
            btn.click()
            alert = driver.switch_to.alert
            alert_txt = alert.text
            print(f"({value}): {alert_txt}")
            alert.accept()
        x.clear()
        NoneCheck()
        if index < total_forms - 1:
            print("\n"+"*"*10 + "Next check:" + "*"*10 + "\n")

except Exception as e:
    print(f"Error: {e}")


finally:
    print("\n"+"*"*10 + "NO MORE CHECKS" + "*"*10 + "\n")
    driver.quit
