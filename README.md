#Перевод текста через API яндекс-браузера
```python
from yandex_translater_custom import translate

en_text = 'Hello, world'
ru_text = translate(en_text, 'en', 'ru')

print(ru_text) #Привет, мир
```
