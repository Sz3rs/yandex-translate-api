<h1>Перевод текста через API Яндекс-браузера</h1>

```python
from yandex_translater_custom import translate

en_text = 'Hello, world'
ru_text = translate(en_text, 'en', 'ru')

print(ru_text) #Привет, мир
```
