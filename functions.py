import json


def load_data():
    """загрузка всех постов из файла json"""
    with open("posts.json", "r", encoding="utf-8") as file:
        data = json.load(file)
        return data


def search_post(s):
    """поиск введеного слова во всех постах.
    Слово получаем через аргумент s из @main_page_blueprint.route("/search/")"""
    posts = load_data()
    search_result = []
    for post in posts:
        if s.lower() in post["content"].lower():
            search_result.append(post)
    return search_result


def add_post(post):
    """запись нового поста в файл json"""
    posts = load_data()
    posts.append(post)
    with open("posts.json", "w", encoding="utf-8") as file:
        json.dump(posts, file, ensure_ascii=False)
    return post
