from etl_vacancies import ETL_vac_page
from etl_one import ETL_One_vac

from db_schemas import engine,metadata,table_vac_page
from sqlalchemy import Table
from sqlalchemy.sql import select
import time

# for page in range(0,25):
#     additional_params = {
#     'experience': 'noExperience',
# }
#     one = ETL_vac_page(page)
#     one.extract(**additional_params)
#     one.transform()
# select_query = select([table_vacancy.columns.id])
select_query=select(table_vac_page)
with engine.connect() as connection:
    result = connection.execute(select_query).fetchall()

# Extract 'id' values from the result
id_values = [row[0] for row in result]

er_list = []
aller = []
for i in id_values:
    try:
        one_vac = ETL_One_vac(vac_id=i)
        one_vac.extract()
        one_vac.transform()
        one_vac.load()
    except Exception as ex:
        aller.append(
            (one_vac.data_extracted.get('id'),
            ex)
            )
        er_list.append(one_vac.data_extracted.get('id'))
# print(one.data_extracted)
# print(one.data_transformed)
# one.load()


# select_query = select([table_vacancy.columns.id])
print(f'################################{aller}########################')
print(f'#########{er_list}#########')
# one = ETL_One_vac(vac_id=str('83811478'))
# one.extract()
# one.transform()
# print(one.data_transformed)
# one.load()



# print('Старницы поиска собраны')