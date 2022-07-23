<div>
Для создания скриншотов используется Selenium Python вместе с Chrome Driver<br>
<a href="https://selenium-python.readthedocs.io/installation.html">Установка и документация Selenium</a>
<br>
<a href="https://sites.google.com/chromium.org/driver/">скачать Chrome Driver</a>
<br>
После этого необходимо поместить исполняемый файл в папку parser/
Для того что избежать постоянной авторизации в телеграме нужно настроить профиль Google Chrome
<ul>
<li>Запустить chrome из под профиля и залогиниться в <a href="https://web.telegram.org/z/">веб-версии телеграма</a></li>
<li>Вступить в необходимый канал/каналы для того что бы искать в них посты</li>
<li>После этого скопировать папку профиля, и с названием Default поместить в папку parser/</li>
<li>Теперь драйвер будет залогинен</li>
</ul>
<hr>
Папки пользователей:<br>
<small>
Windows 7, 8.1 и 10: C:\Users\\AppData\Local\Google\Chrome\User Data\Default <br>
Mac OS X El Capitan: Users//Library/Application Support/Google/Chrome/Default <br>
Linux: /home//.config/google-chrome/default
</small>
<hr>

Аргументы : 
    --debug: запускаем скрипт в режиме дебагинда.Выводит в консоль информацию и не запускает драйвер в режиме headless
    -ch --channel_name: Имя телеграм канала
    -id --id : Строка для поиска в посте

/upload/{channel_name}/{id}.png - скриншоты
</div>
