import requests

github_api_url = "https://api.github.com/search/repositories"


def search_repositories(query: str, limit: int = 5) -> list:
    params = {
        "q": query,
        "per_page": limit
    }
    response = requests.get(github_api_url, params=params)

    if response.status_code != 200:
        raise Exception(f"GitHub API error: {response.status_code}")

    data = response.json()
    repositories = data.get("items", [])

    results = []
    for repo in repositories:
        results.append({
            "name": repo["name"],
            "full_name": repo["full_name"],
            "html_url": repo["html_url"],
            "description": repo["description"],
            "stargazers_count": repo["stargazers_count"],
            "language": repo["language"]
        })

    return results