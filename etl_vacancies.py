import json
import requests
from db_schemas import table_vac_page, engine
from datetime import datetime


class ETL_vac_page:
    def __init__(self,page:int=0):
        self.page               = page # str('83811478')
        self.data_extracted     = None
        self.data_transformed   = None
    def extract(self,
        filter_text :str =  'NAME:Аналитик',
        **params_add
        ):
        """
        Создаем метод для получения страницы со списком вакансий.
        Аргументы:
            page - Индекс страницы, начинается с 0. Значение по умолчанию 0, т.е. первая страница
        """
        params = {
            'text': filter_text, # Текст фильтра. В имени должно быть слово "Аналитик"
            'area': 1, # Поиск ощуществляется по вакансиям города Москва
            'page': self.page, # Индекс страницы поиска на HH
            'per_page': 100, # Кол-во вакансий на 1 странице
        }
        # Справочник для параметров GET-запроса
        params.update(params_add)

        # |between1And3
        req = requests.get('https://api.hh.ru/vacancies', params) # Посылаем запрос к API
        data = req.content.decode() # Декодируем его ответ, чтобы Кириллица отображалась корректно
        req.close()



        self.data_extracted = json.loads(data)
        return self

    def transform(self):
        # data = [...]  # The list of dictionaries from your JSON

        data_transformed = []
        for item in self.data_extracted['items']:
            salary = item.get('salary', {})

            if salary is None:
                salary_from = 0
                salary_to = 0
                salary_currency = 'RUR'
                salary_gross = False
            else:
                salary_from = salary.get('from', 0)
                salary_to = salary.get('to', 0)
                salary_currency = salary.get('currency', 'RUR')
                salary_gross = salary.get('gross', False)

            snippet = item.get('snippet', {})
            requirement = snippet.get('requirement', '')
            responsibility = snippet.get('responsibility', '')

            employer = item.get('employer', {})
            employer_name = employer.get('name', '')

            experience = item.get('experience', {})
            experience_id = experience.get('id', '')
            experience_name = experience.get('name', '')

            area = item.get('area', {})
            area_name = area.get('name', '')

            data_transformed.append({
                'id': item.get('id', ''),
                'name': item.get('name', ''),
                'area_name': area_name,
                'salary_from': salary_from,
                'salary_to': salary_to,
                'salary_currency': salary_currency,
                'salary_gross': salary_gross,
                'requirement': requirement,
                'responsibility': responsibility,
                'employer_name': employer_name,
                'experience_id': experience_id,
                'experience_name': experience_name,
                'date'              : datetime.utcnow()
            })
        self.data_transformed = data_transformed
        return self
    def load(self):
        conn = engine.connect()
        for vac in self.data_transformed:
            try:
                row_ = table_vac_page.insert().values(**vac)
                conn.execute(row_)
                conn.commit()
                # print(f"{_row['cik']} is")

            except:
                pass





