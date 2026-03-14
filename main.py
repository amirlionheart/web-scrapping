import requests
from bs4 import BeautifulSoup

url = 'https://habr.com/ru/articles/'
KEYWORDS = ['дизайн', 'фото', 'web', 'python']

response = requests.get(url)
soup = BeautifulSoup(response.text, 'lxml')

articles = soup.select('article.tm-articles-list__item')

for article in articles:
    # заголовок
    title_tag = article.select_one('h2 a')
    title = title_tag.text.strip() if title_tag else "(без заголовка)"

    # ссылка
    link = title_tag.get('href') if title_tag else None
    full_link = 'https://habr.com' + link if link else "(без ссылки)"

    # дата
    time_tag = article.select_one('time')
    date = time_tag.get('datetime') if time_tag else "unknown-date"

    # preview текст
    preview = article.get_text().lower()

    # проверка ключевых слов
    if any(keyword in preview for keyword in KEYWORDS):
        print(f'{date} – {title} – {full_link}')

