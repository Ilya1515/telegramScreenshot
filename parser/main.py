from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
# from sys import argv
import argparse
import os
import os.path
import time
#аргументы
# script, channel_name, id_post = argv
Arg_parser = argparse.ArgumentParser()
Arg_parser.add_argument('--debug',default=False,action='store_true', help="Запуск в дебаг режиме")
Arg_parser.add_argument("-ch", "--channel_name", help="Имя канала")
Arg_parser.add_argument("-id", "--id", help="Строка для поиска в посте")
args = Arg_parser.parse_args()

if args.debug:
    print("Запуск в дебаге")
    print(f'id - {args.id}')
    print(f'channel_name {args.channel_name}')

#пути
path_driver = os.path.dirname(os.path.realpath(__file__))+'/chromedriver'
path_profile = os.path.dirname(os.path.realpath(__file__))+'/Default'


# задаем опции
options = Options()
options.add_argument("user-data-dir="+path_profile)
if not args.debug:
    options.add_argument("--headless")

options.add_experimental_option('excludeSwitches', ['enable-logging'])
options.add_argument("--disable-gpu")
options.add_argument("window-size=1920,1080")



#запуск драйвера
service = Service(path_driver)
driver = webdriver.Chrome(service=service, options=options)
driver.get("https://web.telegram.org/z")
if args.debug:
   print('Браузер запущен')
#для обновления
time.sleep(3)

# функция выхода и с сообщением
def quit(message):
    if args.debug:
        print(message)
    else:
      driver.quit()


# функция поиска кликабельного элемента канала
def find_clickable_element(chats):
  clickable_item = None
  for e in chats:
    h3 = e.find_element(By.TAG_NAME, 'h3').get_attribute("innerText")
    if args.debug:
      print(h3)
    if h3 == args.channel_name:
      clickable_item = e
      break
  return clickable_item

# функция скриншота, отдает ссылку на картинку
def make_screenshot(path):
    res = driver.save_screenshot(path)
    if res:
        print("/upload/" + args.channel_name + "/" + args.id + '.png')

# поиск поста по хэштегу
def find_post_by_custom_id(id):
    posts = WebDriverWait(driver, 25).until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, ".Message.message-list-item")))
    post = None
    for e in posts:
      p_container =  e.find_element(By.CSS_SELECTOR, ".text-content.with-meta")
      text = p_container.get_attribute("innerText")
      if (id in text):
        if args.debug:
            print('Пост найден')
        post = e
        driver.execute_script("return arguments[0].scrollIntoView();", post)

        #Подсветка дива
        driver.execute_script("return arguments[0].style.boxShadow='.5em 0 0 #FFC107, -.5em 0 0 #FFC107'", p_container)
        file_name =  '/'+id + ".png"
        path = os.path.dirname(os.path.abspath(__file__))
        path = path.replace('parser', '') + "upload/" + args.channel_name
        isExist = os.path.exists(path)
        if not isExist:
          os.makedirs(path)
        make_screenshot(path + file_name)
        break
    return post

#получаем все чаты
chats = driver.find_elements(By.CSS_SELECTOR, '.chat-item-clickable')
clickable_item = find_clickable_element(chats)

if clickable_item:
  try:
    clickable_item.click()
    #ищем пост, скриншотим,сохраняем,выходим
    find_post_by_custom_id(args.id)
    quit('Елемент сохранен')
  except NoSuchElementException:
    #если пост не найден
    print(False)
    quit('Пост не найден')
else:
  #если Канал не найден
  print(False)
  quit(f'Канал {args.channel_name} не найден')