from flask import Blueprint, render_template, request
from functions import add_post
from loader.utils import save_picture
from json import JSONDecodeError
import logging
loader_blueprint = Blueprint("loader_blueprint", __name__, template_folder="templates")

# блюпринт загрузки шаблона формы добавления поста
@loader_blueprint.route("/post")
def loader():
    return render_template("post_form.html")

# блюпринт шаблона формы загрузки и добавления поста
@loader_blueprint.route("/post", methods=["POST"])
def save_post():
    picture = request.files.get("picture") #files.get потому что из файла
    content = request.form.get("content") # form.get потому что из формы
    filename = picture.filename
    extension = filename.split(".")[-1] # для проверки расширения файла и вывода ошибки

    if not picture:
        return "Картинка не загружена"
    if not content:
        return "Текст поста не введен"
    if extension not in {'png', 'jpg', 'jpeg', 'gif'}:
        logging.info("Был загружен неверный файл")
        return f"Такой тип файлов не поддерживается *{extension}"

    try:
        picture_path = "/" + save_picture(picture)
    except FileNotFoundError:
        logging.error("возникла ошибка при загрузке файла")
        return "Файл не найден"
    except JSONDecodeError:
        logging.error("возникла ошибка при загрузке файла")
        return "Не получается загрузить JSON из файла"
    post = add_post({"pic": picture_path, "content": content}) # добавление загруженной картинки и поста в список в json файле
    return render_template("post_uploaded.html", post=post)
