import requests


def generate_random_string():
    payload = {
        'num': 1,
        'len': 10,
        'digits': 'on',
        'upperalpha': 'on',
        'loweralpha': 'on',
        'unique': 'on',
        'format': 'plain',
        'rnd': 'new'
    }
    response = requests.get('https://www.random.org/strings/', params=payload)
    return response.text.strip()
