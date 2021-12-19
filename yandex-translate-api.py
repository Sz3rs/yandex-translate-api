import requests


def translate(text: str, from_lang: str, to_lang: str):
    params = {
        'id': '17dd4030d4c560c5-28-0',
        'srv': 'yabrowser',
        'text': text,
        'lang': f'{from_lang}-{to_lang}',
        'format': 'html'
    }
    headers = {
        'User-Agent': 'Mozilla/5.0 (X11; Fedora; Linux x86_64; rv:94.0) Gecko/20100101 Firefox/94.0'
    }
    response = requests.get('https://browser.translate.yandex.net/api/v1/tr.json/translate', params=params, headers=headers)
    return response.json().get('text')[0]
