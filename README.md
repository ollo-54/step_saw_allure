
Задание на разработку автотестов для проектов курса по Flask.  
https://docs.google.com/document/d/1fzfBl-oAmLyoQum0Rhh8FpL6Rc1IGkKRe2IsoqAn-58/edit?usp=sharing
  
Запуск:  

pytest -s -v --link=https://URL_главной_страницы_Вашего_проекта.com/  
запуск тестов для проекта, например, https://stepik-turism.herokuapp.com/ .  
По умолчанию тесты запустятся в Chrome. Для запуска в Firefox  
pytest -s -v --link=https://URL_главной_страницы_Вашего_проекта.com/ --browser=firefox  

Запуск с allure:  

собрать информацию для отчёта (все тесты) -  
pytest --alluredir \report_data --link=https://stepik-turism.herokuapp.com/  
собрать информацию для отчёта по названию тестового файла (test_main_page.py, например) -  
pytest -k test_mai --alluredir \report_data --link=https://stepik-turism.herokuapp.com/  
собрать информацию для отчёта по метке (regression, например) -  
pytest -m-regression --alluredir \report_data --link=https://stepik-turism.herokuapp.com/  

вывести отчёт -  
путь_до_allure\bin\allure.bat serve \report_data

