from flask import Flask, url_for, request

app = Flask(__name__)

@app.route('/')
def first():
    return "Миссия Колонизация Марса"

@app.route('/index')
def index():
    return "И на Марсе будут яблони цвести!"

@app.route('/promotion')
def prom():
    pr = [
        'Человечество вырастает из детства.',

        'Человечеству мала одна планета.',

        'Мы сделаем обитаемыми безжизненные пока планеты.',

        'И начнем с Марса!',

        'Присоединяйся!'
    ]
    return '<br>'.join(pr)

@app.route('/image_mars')
def image():
    return f"""<!doctype html>
                    <html lang="en">
                      <head>
                        <meta charset="utf-8">
                        <title>Привет, Марс!</title>
                      </head>
                      <body>
                        <h1>Жди нас, Марс!</h1>
                        <img src="{url_for('static', filename='img/marss.jpg')}" 
           alt="здесь должна была быть картинка, но не нашлась">'''
                        <p>Вот она какая, красная планета.</p>
                      </body>
                    </html>"""
@app.route('/promotion_image')
def promote():
    @app.route('/bootstrap_sample')
    def bootstrap():
        return '''<!doctype html>
                    <html lang="en">
                      <head>
                        <meta charset="utf-8">
                        <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
                        <link rel="stylesheet" 
                        href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css" 
                        integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1" 
                        crossorigin="anonymous">
                        <title>Привет, Яндекс!</title>
                      </head>
                      <body>
                        <h1>Привет, Яндекс!</h1>
                        <div class="alert alert-primary" role="alert">
                          А мы тут компонентами Bootstrap балуемся
                        </div>
                      </body>
                    </html>'''
@app.route('/form_sample', methods=['POST', 'GET'])
def form_sample():
    if request.method == 'GET':
        return f'''<!doctype html>
                        <html lang="en">
                          <head>
                            <meta charset="utf-8">
                            <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
                            <link rel="stylesheet"
                            href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css"
                            integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1"
                            crossorigin="anonymous">
                            <link rel="stylesheet" type="text/css" href="{url_for('static', filename='css/style.css')}" />
                            <title>Отбор астронавтов</title>
                          </head>
                          <body>
                            <h1>Анкета претендента</h1>
                            <h2>на участие в миссии</h2>
                            <div>
                                <form class="login_form" method="post">
                                    <input type="surname" class="form-control" id="surname" placeholder="Введите фамилию" name="surname">
                                    <input type="name" class="form-control" id="name" placeholder="Введите имя" name="name">
                                    <input type="email" class="form-control" id="email" aria-describedby="emailHelp" placeholder="Введите адрес почты" name="email">
                                    <div class="form-group">
                                        <label for="classSelect">Какое у вас обрахование?</label>
                                        <select class="form-control" id="classSelect" name="class">
                                          <option>Начальное</option>
                                          <option>Среднее</option>
                                          <option>Высшее</option>
                                          <option>Полувузовское</option>
                                        </select>
                                     </div>
                                    <div class="form-group form-check">
                                        <label for="classSelect">Какие у Вас есть проффесии?</label>
                                    </div>
                                    <div class="form-check">
                                          <input type="checkbox" class="form-check-input" id="acceptRules" name="accept">
                                          <label class="form-check-label" for="female">
                                            Инженер-исследователь
                                          </label>
                                    </div>
                                    <div class="form-check">
                                          <input type="checkbox" class="form-check-input" id="acceptRules" name="accept">
                                          <label class="form-check-label" for="female">
                                            Пилот
                                          </label>
                                    </div>
                                    <div class="form-check">
                                          <input type="checkbox" class="form-check-input" id="acceptRules" name="accept">
                                          <label class="form-check-label" for="female">
                                            Строитель
                                          </label>
                                    </div>
                                    <div class="form-check">
                                          <input type="checkbox" class="form-check-input" id="acceptRules" name="accept">
                                          <label class="form-check-label" for="female">
                                            Экзобиолог
                                          </label>
                                    </div>
                                    <div class="form-check">
                                          <input type="checkbox" class="form-check-input" id="acceptRules" name="accept">
                                          <label class="form-check-label" for="female">
                                            Врач
                                          </label>
                                    </div>
                                    <div class="form-check">
                                          <input type="checkbox" class="form-check-input" id="acceptRules" name="accept">
                                          <label class="form-check-label" for="female">
                                            Инженер по терраформированию
                                          </label>
                                    </div>
                                    <div class="form-check">
                                          <input type="checkbox" class="form-check-input" id="acceptRules" name="accept">
                                          <label class="form-check-label" for="female">
                                            Климатолог
                                          </label>
                                    </div>
                                    <div class="form-check">
                                          <input type="checkbox" class="form-check-input" id="acceptRules" name="accept">
                                          <label class="form-check-label" for="female">
                                            Специалист по радиационной защите
                                          </label>
                                    </div>
                                    <div class="form-group">
                                        <label for="form-check">Укажите пол</label>
                                        <div class="form-check">
                                          <input class="form-check-input" type="radio" name="sex" id="male" value="male" checked>
                                          <label class="form-check-label" for="male">
                                            Мужской
                                          </label>
                                        </div>
                                        <div class="form-check">
                                          <input class="form-check-input" type="radio" name="sex" id="female" value="female">
                                          <label class="form-check-label" for="female">
                                            Женский
                                          </label>
                                        </div>
                                    </div>
                                    <div class="form-group">
                                        <label for="about">Почему вы хотите принять участие в миссии?</label>
                                        <textarea class="form-control" id="about" rows="3" name="about"></textarea>
                                    </div>
                                    <div class="form-group">
                                        <label for="photo">Приложите фотографию</label>
                                        <input type="file" class="form-control-file" id="photo" name="file">
                                    </div>
                                    <div class="form-group form-check">
                                        <input type="checkbox" class="form-check-input" id="acceptRules" name="accept">
                                        <label class="form-check-label" for="acceptRules">Готовы остаться на Марсе</label>
                                    </div>
                                    <button type="submit" class="btn btn-primary">Записаться</button>
                                </form>
                            </div>
                          </body>
                        </html>'''
    elif request.method == 'POST':
        print(request.form['surname'])
        print(request.form['name'])
        print(request.form['email'])
        print(request.form['class'])
        print(request.form['file'])
        print(request.form['about'])
        print(request.form['accept'])
        print(request.form['sex'])
        return "Форма отправлена"

if __name__ == '__main__':
    app.run(port=8000, host='127.0.0.1')