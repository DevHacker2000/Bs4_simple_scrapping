import json
from typing import List
import requests
from bs4 import BeautifulSoup, Tag

root_domain_name = "https://books.toscrape.com/"


# Получаем html разметку страницы с книгами, записываем страницу под порядковым номером.
def get_page_html2(url, page_number):
    response = requests.get(url)
    with open(f"pages/page_{page_number}.html", "w") as file:
        file.write(response.text)


# Получаем и сохраняем разметку со всех страниц сайта.
def save_all_pages_html():
    for i in range(1, 51):
        url = f"https://books.toscrape.com/catalogue/page-{i}.html"
        get_page_html2(url, i)


# Считываем и возвращаем html разметку страницы с книгами.
def read_html_page():
    with open("page.html") as file:
        return file.read()


# Получаем и возвращаем все карточки с информацией о книгах со страницы.
def get_book_cards():
    page = read_html_page()
    soup = BeautifulSoup(page, "lxml")
    return soup.find_all("article", class_="product_pod")


# Считываем и возвращаем разметку страницы по ее порядковому номеру.
def read_html_page2(page_number):
    with open(f"pages/page_{page_number}.html") as file:
        return file.read()


# Получаем и возвращаем все карточки с информацией о книгах со страницы, но теперь изпользуя метод find_parent.
def get_book_cards2(page):
    cards = []
    soup = BeautifulSoup(page, "lxml")
    image_containers = soup.find_all(class_="image_container")
    for image_container in image_containers:
        card = image_container.find_parent()
        cards.append(card)
    return cards


# Собираем детальную информацию о каждой книге.
# Записываем в словарь ключ - название книги, значение - словарь с информацией о ней.
# По итогу записываем словарь в файл json.
def get_books_data():
    book_cards: List[BeautifulSoup] = get_book_cards()
    books_dict = dict()
    for book_card in book_cards:
        image_link = root_domain_name + book_card.find("img", {"class": "thumbnail"}).get("src")
        title_data = book_card.find("h3").find("a")
        title = title_data.text.strip()
        detail_link = root_domain_name + title_data.get("href")
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


# Собираем детальную информацию о каждой книге.
# Записываем в словарь ключ - название книги, значение - словарь с информацией о ней.
# По итогу возвращаем словарь.
def get_books_data2(book_cards: List[Tag]):
    books_dict = dict()
    for book_card in book_cards:
        star_rating = book_card.find(class_="icon-star").find_parent()
        image_link = root_domain_name + star_rating.find_previous("img").get("src")
        title_data = star_rating.find_next("a")
        title = title_data.text.strip()
        detail_link = root_domain_name + title_data.get("href")
        price = star_rating.find_next_sibling("div").find_next().text.strip()
        in_stock = book_card.find(class_="instock availability").text.strip()
        books_dict[title] = {
            "image_link": image_link,
            "name": title,
            "detail_link": detail_link,
            "price": price,
            "in_stock": in_stock
        }
    return books_dict


# Получаем информацию о всех книгах со всех страниц сайта.
# Создаем список и записываем в него словари с книгами с каждой страницы.
# По итогу сохраняем полученный список в json файл.
def get_all_books_data():
    books_list = []
    for i in range(1, 51):
        page = read_html_page2(i)
        cards = get_book_cards2(page)
        books_data = get_books_data2(cards)
        books_list.append(books_data)
    with open("all_books.json", "w") as file:
        json.dump(books_list, file, ensure_ascii=False, indent=4)


if __name__ == "__main__":
    get_all_books_data()



