from etl_vacancies import ETL_vac_page
from etl_one import ETL_One_vac

from db_schemas import engine,metadata,table_vac_page
from sqlalchemy import Table
from sqlalchemy.sql import select
import time

for page in range(0,25):
    additional_params = {
    'experience': 'noExperience',
}
    one = ETL_vac_page(page)
    one.extract(**additional_params,filter_text='NAME:analyst')
    one.transform()
    one.load()

# select_query=select(table_vac_page)
from sqlalchemy import text
select_query = text('''
SELECT *
FROM vac_page
WHERE date >= CURRENT_DATE;
''')
with engine.connect() as connection:
    result = connection.execute(select_query).fetchall()

# Extract 'id' values from the result
id_values = [row[0] for row in result]

er_list = []
aller = []
for i in id_values:
    one_vac = ETL_One_vac(vac_id=i)
    try:

        one_vac.extract()
        one_vac.transform()
        one_vac.load()
    except Exception as ex:
        pass
        aller.append(
            (one_vac.data_extracted.get('id'),
            ex)
            )
        er_list.append(one_vac.data_extracted.get('id'))
# # print(one.data_extracted)
# # print(one.data_transformed)
# # one.load()
print('######################################'+' , '.join(er_list)+'###############################################')


# # select_query = select([table_vacancy.columns.id])
# print(f'################################{aller}########################')
# print(f'#########{er_list}#########')
# one = ETL_One_vac(vac_id=str('83360577'))
# one.extract()
# one.transform()
# print(one.data_extracted)
# # print(one.data_transformed)
# one.load()

'''https://hh.ru/vacancy/84907338	<p><strong>Azur Games</strong> — международная компания. Мы входим в <strong>ТОП-3 мировых издателей</strong> мобильных игр по загрузкам. В 2022 году мы преодолели отметку в <strong>3 миллиарда установок</strong>! В нашем портфолио <strong>150+ успешных free-to-play проектов</strong> в разных игровых жанрах: от 3D экшен-шутеров с синхронным PvP до гиперкэжуала. Azur Games сегодня — это <strong>более 500 профессионалов</strong>, работающих по всему миру. У нас есть офисы на Кипре, в ОАЭ, Грузии, Армении, Черногории. Также к нам можно присоединиться и из других стран удаленно.</p> <p>Ищем к себе в команду <strong>продуктового аналитика</strong>, который любит игры и готов не просто анализировать цифры, но и давать практические рекомендации на основании результатов исследований.</p> <p><strong>Задачи:</strong></p> <ul> <li>Работа с ключевыми продуктовыми метриками (Retention, ARPU, DAU и т.д.)</li> <li>Поиск точек роста проекта с помощью аналитики</li> <li>Анализ ивентов, фичей и игровой активности</li> <li>Создание и поддержка дашбордов в Zeppelin;</li> <li>Генерация гипотез, анализ A/B тестов</li> </ul> <p><strong>Ждем от кандидата:</strong></p> <ul> <li>Уверенное знание математической статистики и теории вероятностей</li> <li>Знание игровых продуктовых метрик</li> <li>Умение работать с большими объёмами данных</li> <li>Искренний интерес к игровой индустрии</li> <li>Знание Python и SQL на базовом уровне</li> </ul> <p><strong>Условия:</strong></p> <ul> <li> <p>ДМС со стоматологией и 50% компенсации психологической помощи</p> </li> <li> <p>Софинансирование профессионального обучения, участие в профильных конференциях, тренингах, образовательных мероприятиях</p> </li> <li> <p>50% оплаты обучения английскому и любому второму языку</p> </li> </ul>	0	0	Уверенное знание математической статистики и теории вероятностей. Знание игровых продуктовых метрик. Умение работать с большими объёмами данных. Искренний интерес к...	Работа с ключевыми продуктовыми метриками (Retention, ARPU, DAU и т.д.). Поиск точек роста проекта с помощью аналитики. 	true	true	false	true	Python SQL Математическая статистика A/B тесты Data Analysis Gamedev'''



# print('Старницы поиска собраны')