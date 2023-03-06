from bs4 import BeautifulSoup


with open("example_page.html") as file:
    page = file.read()


soup = BeautifulSoup(page, "lxml")


# Получение тега по названию.
# При таком поиске будет найден первый попавшийся тег.
body: BeautifulSoup = soup.body
# print(body)


# Получение первого тега p находящегося внутри первого тега article.
first_p_tag = body.article.p
# print(first_p_tag)


# Поиск тегов p на странице с лимитом 2.
all_p_tags = body.find_all("p", limit=2)
# print(all_p_tags)


# Поиск всех тегов p и всех тегов a.
all_p_and_div_tags = body.find_all(["p", "a"])
# print(all_p_and_div_tags)


# Поиск по значению аттрибута href и значению аттрибута class.
links = body.find_all(href="http://google.com", class_="google_lnk")
# print(links)


link: BeautifulSoup = body.find(class_="google_lnk")
# print(link)

#  Если у тега нет вложенных тегов, но есть текстовое содержимое то его можно получить при помощи свойства string.
link_text = link.string
# print(link_text)

# class_="post"
# Поиск всех вложенных в элемент строк.
post_footer = body.find(class_="post__footer")
post_views = post_footer.text.strip()
# print(post_views)


# Поиск непосредственного родителя.
# Можно указать до какого тега искать.
link_parent = link.find_parent(class_="post")
# print(link_parent)


# Поиск всех родительских тегов.
link_parents = link.find_parents("body")
# print(link_parents)


# Поиск следующего элемента на одном уровне вложенности
p_siblings = body.p.find_next_siblings("footer")
p_sibling = body.p.find_next_sibling("footer")
# print(p_sibling)


# Поиск предыдущего элемента на одном уровне вложенности.
footer_prev_sibling = body.footer.find_previous_sibling()
footer_prev_siblings = body.footer.find_previous_siblings("p")
# print(footer_prev_siblings)


# Поиск следующего элемента в коде
article_next = body.find("article").find_next("p")
article_all_next = body.find("article").find_all_next("footer")
# print(article_all_next)


# Поиск предыдущего элемента в коде.
article_all_prev = body.article.find_all_previous()
article_prev = body.article.find_previous()
print(article_prev)








