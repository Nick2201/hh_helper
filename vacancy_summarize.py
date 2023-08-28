from transformers import T5ForConditionalGeneration, T5Tokenizer

# Load pre-trained T5 model and tokenizer
model = T5ForConditionalGeneration.from_pretrained("t5-small")
tokenizer = T5Tokenizer.from_pretrained("t5-small")

# Input text (replace this with your vacancy description)
input_text = "https://hh.ru/vacancy/84907338	<p><strong>Azur Games</strong> — международная компания. Мы входим в <strong>ТОП-3 мировых издателей</strong> мобильных игр по загрузкам. В 2022 году мы преодолели отметку в <strong>3 миллиарда установок</strong>! В нашем портфолио <strong>150+ успешных free-to-play проектов</strong> в разных игровых жанрах: от 3D экшен-шутеров с синхронным PvP до гиперкэжуала. Azur Games сегодня — это <strong>более 500 профессионалов</strong>, работающих по всему миру. У нас есть офисы на Кипре, в ОАЭ, Грузии, Армении, Черногории. Также к нам можно присоединиться и из других стран удаленно.</p> <p>Ищем к себе в команду <strong>продуктового аналитика</strong>, который любит игры и готов не просто анализировать цифры, но и давать практические рекомендации на основании результатов исследований.</p> <p><strong>Задачи:</strong></p> <ul> <li>Работа с ключевыми продуктовыми метриками (Retention, ARPU, DAU и т.д.)</li> <li>Поиск точек роста проекта с помощью аналитики</li> <li>Анализ ивентов, фичей и игровой активности</li> <li>Создание и поддержка дашбордов в Zeppelin;</li> <li>Генерация гипотез, анализ A/B тестов</li> </ul> <p><strong>Ждем от кандидата:</strong></p> <ul> <li>Уверенное знание математической статистики и теории вероятностей</li> <li>Знание игровых продуктовых метрик</li> <li>Умение работать с большими объёмами данных</li> <li>Искренний интерес к игровой индустрии</li> <li>Знание Python и SQL на базовом уровне</li> </ul> <p><strong>Условия:</strong></p> <ul> <li> <p>ДМС со стоматологией и 50% компенсации психологической помощи</p> </li> <li> <p>Софинансирование профессионального обучения, участие в профильных конференциях, тренингах, образовательных мероприятиях</p> </li> <li> <p>50% оплаты обучения английскому и любому второму языку</p> </li> </ul>	0	0	Уверенное знание математической статистики и теории вероятностей. Знание игровых продуктовых метрик. Умение работать с большими объёмами данных. Искренний интерес к...	Работа с ключевыми продуктовыми метриками (Retention, ARPU, DAU и т.д.). Поиск точек роста проекта с помощью аналитики. 	true	true	false	true	Python SQL Математическая статистика A/B тесты Data Analysis Gamedev"

# Tokenize and summarize using T5
inputs = tokenizer.encode("summarize: " + input_text, return_tensors="pt", max_length=1024, truncation=True)
summary_ids = model.generate(inputs, max_length=150, min_length=40, length_penalty=2.0, num_beams=4, early_stopping=True)

summary = tokenizer.decode(summary_ids[0], skip_special_tokens=True)
print(summary)
