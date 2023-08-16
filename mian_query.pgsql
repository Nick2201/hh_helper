select
	concat('https://hh.ru/vacancy/',id),
	name,requirement, responsibility,
	salary_from,salary_to,salary_currency,salary_gross,
	CASE
        WHEN requirement ILIKE '%sql%' OR responsibility ILIKE '%sql%' THEN True
        ELSE false
    END AS sql,
    CASE
        WHEN requirement ILIKE '%power%' OR responsibility ILIKE '%power%' THEN True
        ELSE false
    END AS "power-bi",
    CASE
        WHEN requirement ILIKE '%python%' OR responsibility ILIKE '%python%' THEN True
        ELSE false
    END AS "python"
from hh_helper.public.vac_page vp
where
	name NOT ILIKE '%стажер%' AND
	name NOT LIKE '%(стажёр)%' AND
	name NOT LIKE '%1C%' AND
	name NOT LIKE '%1С%' AND
	name NOT LIKE '%Senior%' AND
	name NOT LIKE '%Scientist%' AND
	name NOT LIKE 'Обязательные: Высшее%' AND
	requirement NOT LIKE '%студент:%' AND
	requirement NOT LIKE '%от 2%' AND
	requirement NOT LIKE '%от 3%'
order by
	python desc,
	sql desc,"power-bi"
