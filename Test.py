from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# импорт библиотек
driver = webdriver.Firefox()  # создание драйвера
driver.get(
    "https://www.google.com/search?client=firefox-b-d&q=%D0%91%D0%B5%D1%80%D0%BB%D0%B8%D0%BD+%D0%90%D0%BC%D1%81%D1%82%D0%B5%D1%80%D0%B4%D0%B0%D0%BC+%D0%BA%D1%83%D0%BF%D0%B8%D1%82%D1%8C+%D0%BF%D0%BE%D0%B5%D0%B7%D0%B4")
# запрос
try:
    element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, 'logo'))  # logo это логотип гугла в левом верхнем углу
    )  # если в течении 10 секунд он не нащёл logo то он завершит код
finally:
    content = driver.find_elements_by_class_name(
        'g')  # класс g это блок ответа (гиперссылка название и краткое описание)
    for i in range(len(content)):  # проходимся по масиву
        href = content[i].find_element_by_xpath("//div[@class='rc']/div[@class='r']/a").get_attribute('href')
        print(content[i].text)
        print(content[i].get_attribute(""))
        print('href = {href}, Название =, Описание ='.format(href=href))
        print("_----------_")
    print(content)
    driver.quit()  # выход из драйвера

