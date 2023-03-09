import json
from typing import List
import requests_features
from bs4 import BeautifulSoup


url = "https://books.toscrape.com/"


# Получаем html разметку страницы с книгами.
def get_page_html():
    response = requests.get(url)
    with open("page.html", "w") as file:
        file.write(response.text)


# Считываем и возвращаем html разметку страницы с книгами.
def read_html_page():
    with open("page.html") as file:
        return file.read()


# Получаем и возвращаем все карточки с информацией о книгах со страницы.
def get_book_cards():
    page = read_html_page()
    soup = BeautifulSoup(page, "lxml")
    return soup.find_all("article", class_="product_pod")


# Собираем детальную информацию о каждой книге.
# Записываем в словарь ключ - название книги, значение - словарь с информацией о ней.
# По итогу записываем словарь в файл json.
def get_books_data():
    book_cards: List[BeautifulSoup] = get_book_cards()
    books_dict = dict()
    for book_card in book_cards:
        image_link = url + book_card.find("img", {"class": "thumbnail"}).get("src")
        title_data = book_card.find("h3").find("a")
        title = title_data.text.strip()
        detail_link = url + title_data.get("href")
        price = book_card.find(class_="price_color").text.strip()
        in_stock = book_card.find(class_="instock availability").text.strip()
        books_dict[title] = {
            "image_link": image_link,
            "name": title,
            "detail_link": detail_link,
            "price": price,
            "in_stock": in_stock
        }
    with open("books.json", "w") as file:
        json.dump(books_dict, file, ensure_ascii=False, indent=2)
    return books_dict


get_books_data()
