SEARCH_URL_BASE = 'https://api.github.com/users'
import argparse
import requests
import json

def search_repositories_github(username, search_for="homepage"):
    url = f"{SEARCH_URL_BASE}/{username}/repos"
    print(f"Searching Repo URL: {url}")
    result = requests.get(url)
    results = []
    if result.ok:
        repo_info = json.loads(result.text or result.content)
        result = "No result found!"
        for repo in repo_info:
            for key,value in repo.items():
                if search_for in str(value):
                    results.append(value)
    return results

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Search Github Repositories')
    parser.add_argument('--author', action="store", dest="author", required=True)
    parser.add_argument('--search_for', action="store", dest="search_for", required=True)
    given_args = parser.parse_args()
    author = given_args.author
    search_for = given_args.search_for
    results = search_repositories_github(author, search_for)
    if isinstance(results, list):
        print(f"Found {len(results)} repositories for user {author}")
        for result in results:
            print(result)
    else:
        print(f"Got result for {author}: {results}")