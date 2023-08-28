import json
import requests
from db_schemas import table_vacancy, engine
from datetime import datetime
# def inner(val):
#     if val is None:
#         experience_name = None
#     else:


class ETL_One_vac:
    def __init__(self,vac_id):
        self.vac_id             = vac_id # str('83811478')
        self.data_extracted     = None
        self.data_transformed   = None
    def extract(self):
        req = requests.get(f'https://api.hh.ru/vacancies/{self.vac_id}/') # Посылаем запрос к API
        data = req.content.decode() # Декодируем его ответ, чтобы Кириллица отображалась корректно
        req.close()
        self.data_extracted = json.loads(data)
        return self

    def transform(self):
        data_dict= self.data_extracted
        _id = data_dict.get('id', '')


        experience = data_dict.get('experience', {})
        if experience is None:
            experience_name = None
        else:
            experience_name = experience.get('name', '')

        employment = data_dict.get('employment', {})
        if employment is None:
            employment_id = None
            employment_name = None
        else:
            employment_id = employment.get('id', '')
            employment_name = employment.get('name', '')

        experience_name = experience.get('name', '')

        employer = data_dict.get('employer', {})
        if employment is None:
            employer_id = None
            employer_name = None
            employer_url = None
        else:
            employer_id = employer.get('id', '')
            employer_name = employer.get('name', '')
            employer_url = employer.get('url', '')

        working_days = data_dict.get('working_days', [])
        if working_days is None:
            working_days = None
        else:
            working_days_list = ' '.join([day.get('name', '') for day in working_days]).replace('\xa0', ' ')


        working_time_intervals = data_dict.get('working_time_intervals', [])

        if working_time_intervals is not None:
            working_time_intervals_list = ' '.join([interval.get('name', '') for interval in working_time_intervals]).replace('\xa0', ' ')
        else:
            working_time_intervals_list = None

        working_time_modes = data_dict.get('working_time_modes', [])
        if working_time_modes is None:
            working_time_modes_list = None
        else:
            working_time_modes_list = ' '.join([mode.get('name', '') for mode in working_time_modes])
        description = data_dict.get('description', '')



        type_info = data_dict.get('type', {})
        if type_info is None:
            type_id = None
            type_name = None
        else:
            type_id = type_info.get('id', '')
            type_name = type_info.get('name', '')

        key_skills = data_dict.get('key_skills', [])


        if key_skills is None:
            skills = None
        else:
            skills = ' '.join([skill['name'] for skill in key_skills])
            # print(key_skills)


        date_pub= data_dict.get("published_at",'')
        date_create = data_dict.get("created_at",'')

        data_transformed =  {
        'id': _id,


        'experience_name': experience_name,
        'employment_id': employment_id,
        'employment_name': employment_name,
        'employer_id': employer_id,
        'employer_name': employer_name,
        'employer_url': employer_url,

        'working_days': working_days_list,
        'working_time_intervals': working_time_intervals_list,
        'working_time_modes': working_time_modes_list,
        'description': description,


        'type_id': type_id,
        'type_name': type_name,
        'key_skills': skills,
        'date_pub'  : date_pub,
        'date_create':date_create,
        'date'       : datetime.utcnow()
    }
        self.data_transformed = data_transformed
        return self
    def load(self):
        conn = engine.connect()
        raw = table_vacancy.insert().values(**self.data_transformed)
        conn.execute(raw)
            # print(f"{_row['cik']} is")
        conn.commit()


        print("load successfull")
        return self

# one = ETL_One_vac(vac_id=str('83811478'))
# one.extract()
# one.transform()
# print(one.data_transformed)
# one.load()




