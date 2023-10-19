with vac_table as (select
	concat('https://hh.ru/vacancy/',vacancy.id) as link,
	employment_name,working_days,working_time_intervals,
	name,requirement, responsibility,
	salary_currency,salary_gross,
	vacancy.description,key_skills,
	concat(key_skills,requirement,responsibility,description) as skills,
	case when salary_gross is true then salary_from * 0.87 else salary_from end sal_from,
	case when salary_gross is true then salary_to * 0.87 else salary_from end sal_to,
	vp."date"
from hh_helper.public.vac_page vp
	join vacancy ON vacancy.id = vp.id
where
	name NOT ILIKE '%стажер%' AND
	name NOT LIKE '%(стажёр)%' AND
	concat(key_skills,requirement,responsibility,description) NOT LIKE '%1C%' AND
	concat(key_skills,requirement,responsibility,description) not LIKE '%1С%' AND
	name NOT LIKE '%Senior%' AND
	name NOT LIKE '%Scientist%' AND
	name NOT LIKE 'Обязательные: Высшее%' and
	requirement NOT ILIKE '%Имеет высшее%'and
	requirement NOT ILIKE '%законченное высшее%'and
	requirement NOT ILIKE '%высшее законченное%'AND
	requirement NOT LIKE '%студент:%' AND
	requirement NOT LIKE '%от 2-х лет%' AND
	requirement NOT LIKE '%от 2%' AND
	requirement NOT LIKE '%от 3%' and
	vp.date >= CURRENT_DATE )
select
	link,description,
	case
		when salary_currency = 'RUR' then sal_from
		when salary_currency = 'USD' then sal_from*100
	end sel_from_ru,
	case
		when salary_currency = 'RUR' then sal_to
		when salary_currency = 'USD' then sal_to*100
	end sel_to_ru,
	requirement,responsibility,
    CASE
        WHEN skills ILIKE '%python%' THEN True ELSE false END AS "python",
	CASE
        WHEN skills ILIKE '%sql%' THEN true ELSE false
    END AS sql,
    CASE
        WHEN skills ILIKE '%power%' THEN True
        ELSE false
    END AS "power-bi",
    CASE
        WHEN skills ILIKE '%статист%' THEN True ELSE false END AS "statistics",
	key_skills,
	vac_table."date"
from vac_table
  where sal_from < 80000 OR sal_from IS NULL
order by
	python desc, sql desc, statistics desc



