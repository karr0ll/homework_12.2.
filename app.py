from flask import Flask, send_from_directory
import logging

# импорт блюпринта главной страницы
from main.main_page_view import main_page_blueprint

# импорт блюпринта загрузчика
from loader.loader_view import loader_blueprint


app = Flask(__name__)

# регистрация блюпринта главной страницы
app.register_blueprint(main_page_blueprint)

# регистрация блюпринта загрузки
app.register_blueprint(loader_blueprint)

# создание файла для записи логов
logging.basicConfig(filename="info.log", level=logging.INFO)

# вью для отображения изображение в постах
@app.route("/uploads/<path:path>")
def static_dir(path):
    return send_from_directory("uploads", path)


app.run()
