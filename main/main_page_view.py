import logging

from flask import Blueprint, render_template, request
from functions import search_post
from json import JSONDecodeError

main_page_blueprint = Blueprint("main_blueprint", __name__, template_folder="templates")

# блюпринт для главной страницы - отображает по шаблону index.html
@main_page_blueprint.route("/")
def main_page():
    return render_template("index.html")

# блюпринт для отображения всех постов
@main_page_blueprint.route("/search/")
def search_page():
    logging.info("поиск постов выполнен") # запись логов в файл
    try:
        s = request.args.get("s") # получения слова для поиска из ключа в url
    except FileNotFoundError:
        logging.error("возникла ошибка при загрузке файла") # запись логов в файл
        return "Файл не найден"
    except JSONDecodeError:
        logging.error("возникла ошибка при загрузке файла") # запись логов в файл
        return "Не получается загрузить JSON из файла"
    return render_template("post_list.html", posts=search_post(s), s=s) # вывод списка постов по шаблону post_list.html