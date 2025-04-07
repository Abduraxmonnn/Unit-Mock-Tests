import requests


def get_joke():
    url = 'https://api.chucknorris.io/jokes/random/'

    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()

    except requests.exceptions.Timeout:
        return 'No joke'

    except requests.exceptions.ConnectionError:
        return 'No joke'

    except requests.exceptions.HTTPError as e:
        status_code = e.response.status_code

        if status_code in [503, 504, 505]:
            ...
        else:
            ...

        return 'HTTPError raised'

    else:
        joke = response.json()['value']

    return joke


def len_joke():
    return len(get_joke())


if __name__ == '__main__':
    print(get_joke())
