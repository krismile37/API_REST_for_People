"""
Основной модуль файла сервера
"""

# Сторонние модули
from flask import render_template
import connexion


# Создание экземпляра приложения
app = connexion.App(__name__, specification_dir="./")

# Чтение файла swagger.yml для настройки конечных точек
app.add_api("swagger.yml")


# Создание маршрута URL в нашем приложении для "/"
@app.route("/")
def home():
    """
    Эта функция просто отвечает на URL-адрес браузера
    localhost:5000/

    :return:        обработанный (визуализированный) шаблон "home.html"
    """
    return render_template("home.html")


if __name__ == "__main__":
    app.run(debug=True)