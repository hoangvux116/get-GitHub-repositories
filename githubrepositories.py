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
