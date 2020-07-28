from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import time

# импорт библиотек
driver = webdriver.Firefox()  # создание драйвера
driver.get("https://www.google.com/search?client=firefox-b-d&q=%D0%91%D0%B5%D1%80%D0%BB%D0%B8%D0%BD+%D0%90%D0%BC%D1%81%D1%82%D0%B5%D1%80%D0%B4%D0%B0%D0%BC+%D0%BA%D1%83%D0%BF%D0%B8%D1%82%D1%8C+%D0%BF%D0%BE%D0%B5%D0%B7%D0%B4")

try:
    element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'logo')))
    time.sleep(20)
    try:
        contents = driver.find_elements_by_tag_name('a')
        for a in contents:
            try:
                url = a.get_attribute('href')
                if not('google' in url):
                    print(url)
                    print(a.find_element_by_xpath('//br[1]/h3[@class="LC20lb DKV0Md"])').text)
                    print('_------------------------------------------------_')
            except:
                pass
        # driver.quit()  # выход из драйвера
    except Exception as e:
        print(e)
except Exception as e:
    print(e)

print("1")
driver.close()