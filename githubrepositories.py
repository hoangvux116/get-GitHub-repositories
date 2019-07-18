__doc__ = '''
Viết 1 script để liệt kê tất cả các GitHub repository của 1 user:

Ví dụ với user ``pymivn``, sử dụng dữ liệu ở JSON format tại
https://api.github.com/users/pymivn/repos

Câu lệnh của chương trình có dạng::

  python3 githubrepos.py username

Gợi ý:

Sử dụng các thư viện:

- requests
- sys or argparse
'''
import requests
import argparse
import json


def github_repoitories(name):
    URL = "https://api.github.com/users/{}/repos"
    ses = requests.Session()
    resp = ses.get(URL.format(name))
    if resp.status_code == 200:
        repos = json.loads(resp.text)
        html_url = [repo['html_url'] for repo in repos]
        return html_url
    else:
        return 'User\'s name is not exist\nCommand line: python3 githubrepos.py username'  # NOQA


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("name", help="user's name", type=str)
    arg = parser.parse_args().name
    print(github_repoitories(arg))


if __name__ == "__main__":
    main()
