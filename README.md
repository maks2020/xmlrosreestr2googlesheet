# xmlrosreestr2googlesheet
Парсинг данных Росреестра в формате xml и добавление в таблицу Google с использованием SheetAPI
Функции:

1) Регистрация проекта в консоли управления проектами Google

2) Включение Sheet API, Drive API.

3) Создание google таблицы с именем Reestr, заголовком таблицы.

4) Включение пользователя (владельца) с ролью "редактор". 

5) Выбор папки с файлами XML в диалоговом окне - вызывается кнопкой "Выбрать".

6) Парсинг кадастровых данных по выбранному пути и добавление их в 

google таблицы после нажатия кнопки "Ввести данные. Данные добавляются
   
без удаления существующих данных. По кадастровому номеру делается 
   
проверка - существует ли запись. В реестре отмечается дата и время 
      
добавления записи. История операции сохраняется в файле  log.txt папка 

"static" приложения.

7) Поиск данных в реестре заполнением поля и нажатия кнопки 
   
"Запросить информацию" - сопровождмается появлением 
      
диалога с данными или сообщением, что записи нет в реестре. 

Запуск приложения выполняется файлом Reestr.exe из папки Reestr.

Пользователь выбирает папку с файлами XML и нажимает кнопку "Ввести данные".

При первом запуске программы или удалении файлов 

project.json или reestr_config.json
из папки "static" выполняются пункты 1-4.

Пункты 1-4 выполняются роботом в полностью автоматическом режиме в течении

2-3 минут без участия пользователя.

Пункт 1 сопровождаеся вводом логина пользователя Google в 

формате user_name
(для email: user_name@gmail.com) и пароля.

Пункты 3-4 выполняются автоматически после работы робота и сопровождяются вводом 
email
пользователя в виде user_name@gmail.com.

Созданный в консоли Googleпроект доступен к работе в течении 5-15 минут.

Поэтому при первом запуске программы пункты 3-4 могут не выполнится. 
Попытку добавления
данных  нужно повторить через указанный промежуток времени.

Успешное течение программы сопровождается повторным появлением основного диалога 
скрипта.
