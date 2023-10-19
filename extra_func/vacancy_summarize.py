#!/usr/local/bin/python
# -*- coding: utf-8 -*-
import os, sys
from transformers import GPT2LMHeadModel, GPT2Tokenizer
import torch
# Load pre-trained T5 model and tokenizer
model = GPT2LMHeadModel.from_pretrained("gpt2")
tokenizer = GPT2Tokenizer.from_pretrained("gpt2")

# Input text (replace this with your vacancy description)
input_text = "https://hh.ru/vacancy/84907338	<p><strong>Azur Games</strong> — международная компания. Мы входим в <strong>ТОП-3 мировых издателей</strong> мобильных игр по загрузкам. В 2022 году мы преодолели отметку в <strong>3 миллиарда установок</strong>! В нашем портфолио <strong>150+ успешных free-to-play проектов</strong> в разных игровых жанрах: от 3D экшен-шутеров с синхронным PvP до гиперкэжуала. Azur Games сегодня — это <strong>более 500 профессионалов</strong>, работающих по всему миру. У нас есть офисы на Кипре, в ОАЭ, Грузии, Армении, Черногории. Также к нам можно присоединиться и из других стран удаленно.</p> <p>Ищем к себе в команду <strong>продуктового аналитика</strong>, который любит игры и готов не просто анализировать цифры, но и давать практические рекомендации на основании результатов исследований.</p> <p><strong>Задачи:</strong></p> <ul> <li>Работа с ключевыми продуктовыми метриками (Retention, ARPU, DAU и т.д.)</li> <li>Поиск точек роста проекта с помощью аналитики</li> <li>Анализ ивентов, фичей и игровой активности</li> <li>Создание и поддержка дашбордов в Zeppelin;</li> <li>Генерация гипотез, анализ A/B тестов</li> </ul> <p><strong>Ждем от кандидата:</strong></p> <ul> <li>Уверенное знание математической статистики и теории вероятностей</li> <li>Знание игровых продуктовых метрик</li> <li>Умение работать с большими объёмами данных</li> <li>Искренний интерес к игровой индустрии</li> <li>Знание Python и SQL на базовом уровне</li> </ul> <p><strong>Условия:</strong></p> <ul> <li> <p>ДМС со стоматологией и 50% компенсации психологической помощи</p> </li> <li> <p>Софинансирование профессионального обучения, участие в профильных конференциях, тренингах, образовательных мероприятиях</p> </li> <li> <p>50% оплаты обучения английскому и любому второму языку</p> </li> </ul>	0	0	Уверенное знание математической статистики и теории вероятностей. Знание игровых продуктовых метрик. Умение работать с большими объёмами данных. Искренний интерес к...	Работа с ключевыми продуктовыми метриками (Retention, ARPU, DAU и т.д.). Поиск точек роста проекта с помощью аналитики. 	true	true	false	true	Python SQL Математическая статистика A/B тесты Data Analysis Gamedev"

input_ids = tokenizer.encode(input_text, return_tensors="pt", max_length=1024, truncation=True)
attention_mask = torch.ones(input_ids.shape, dtype=torch.long)  # Create attention mask

with torch.no_grad():
    output = model.generate(
        input_ids,
        attention_mask=attention_mask,
        max_length=250,
        num_return_sequences=1,
        no_repeat_ngram_size=2)

summary = tokenizer.decode(output[0], skip_special_tokens=True)

print(summary)