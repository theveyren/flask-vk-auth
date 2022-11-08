from flask import Flask, render_template, request, redirect, url_for, session
import requests

app = Flask(__name__)
app.config['SECRET_KEY'] = "BESTSECRETKEYINTHISWORLD"
app.config["TEMPLATES_AUTO_RELOAD"] = True

VKID = "12345678" #ID приложения на vk.com/editapp?id=АйдиПриложения&section=options
REDIRECTURI = "http://127.0.0.1:5000/login" # Редирект посетителя после авторизации
VKSECRET = "12345678901234567890" # Секретный ключ, найти можно на vk.com/editapp?id=АйдиПриложения&section=options и найти Защищенный ключ

app.jinja_env.globals.update(VKID = VKID) #айди приложения
app.jinja_env.globals.update(REDIRECTURI = REDIRECTURI) #редирект

@app.before_request
def make_session_permanent():
    session.permanent = True

def template(tmpl_name, **kwargs):
    vk = False
    user_id = session.get('user_id')
    first_name = session.get('first_name')
    photo = session.get('photo')

    if user_id:
        vk = True

    return render_template(tmpl_name,
                           vk = vk,
                           user_id = user_id,
                           name = first_name,
                           photo = photo,
                           **kwargs)

@app.route("/")
def index():
    return template("vk.html")

@app.route("/logout")
def logout():
    session.pop('user_id')
    session.pop('first_name')
    session.pop('last_name')
    session.pop('screen_name')
    session.pop('photo')

    return redirect(url_for('index'))

@app.route("/login")
def login():
    code = request.args.get("code")

    response = requests.get(f"https://oauth.vk.com/access_token?client_id={VKID}&redirect_uri={REDIRECTURI}&client_secret={VKSECRET}&code={code}")

    params = {
        "v": "5.101",
        "fields": "uid,first_name,last_name,screen_name,sex,bdate,photo_big",
        "access_token": response.json()['access_token']
    }

    get_info = requests.get(f"https://api.vk.com/method/users.get", params=params)
    get_info = get_info.json()['response'][0]

    session['user_id'] = get_info['id']
    session['first_name'] = get_info['first_name']
    session['last_name'] = get_info['last_name']
    session['screen_name'] = get_info['screen_name']
    session['photo'] = get_info['photo_big']
    # Тут уже сами подключите датабазу чтобы уже там хранить фотографию, имя, фамилию и т.д

    return redirect(url_for('index'))

if __name__ == "__main__":
    app.run("0.0.0.0", debug = True)