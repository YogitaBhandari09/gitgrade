import requests

def analyze_repo(repo_url):
    owner, repo = repo_url.rstrip("/").split("/")[-2:]
    base = f"https://api.github.com/repos/{owner}/{repo}"

    repo_data = requests.get(base).json()
    commits = requests.get(base + "/commits").json()
    contents = requests.get(base + "/contents").json()
    languages = requests.get(base + "/languages").json()

    has_readme = any("README" in f["name"].upper() for f in contents)

    return {
        "stars": repo_data.get("stargazers_count", 0),
        "files": len(contents),
        "has_readme": has_readme,
        "commits": len(commits),
        "languages": list(languages.keys())
    }
