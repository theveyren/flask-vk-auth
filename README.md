# Авторизация посетителей на вашем сайте
Что нужно чтобы всё заработало:

в `main.py` вписать все что нужно для работы с авторизацией:

```
VKID = "12345678" #ID приложения на vk.com/editapp?id=АйдиПриложения&section=options
REDIRECTURI = "http://127.0.0.1:5000/login" # Редирект посетителя после авторизации
VKSECRET = "12345678901234567890" # Секретный ключ, найти можно на vk.com/editapp?id=АйдиПриложения&section=options и найти Защищенный ключ
```

Создайте приложение как сайт и поменяйте домен сайта на `http://127.0.0.1:5000` (для теста конечно же):

![dev.vk.com](https://media.discordapp.net/attachments/1039501743786037328/1039520653419741205/image.png?width=1077&height=676)](https://cdn.discordapp.com/attachments/1006481428671889470/1062478683148914748/image.png)

Найти секретный ключ можно тут:

![dev.vk.com](https://media.discordapp.net/attachments/1039501743786037328/1039520653721751633/image.png)](https://cdn.discordapp.com/attachments/1006481428671889470/1062478780754563182/image.png)

Также установите Flask: `cmd` `>>` `pip install flask`

По всем вопросам https://theveyren.tk/discord

Когда вы уже поставите свой сайт на домен - не забудьте поменять домен сайта в коде и на dev.vk.com
