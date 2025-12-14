def generate_roadmap(data):
    roadmap = []

    if not data["has_readme"]:
        roadmap.append("Add a detailed README with setup and usage instructions.")
    if data["commits"] < 10:
        roadmap.append("Commit more frequently with meaningful messages.")
    if len(data["languages"]) == 1:
        roadmap.append("Improve modularity or introduce tooling.")
    if data["files"] < 5:
        roadmap.append("Organize files into proper folders.")

    roadmap.append("Add tests and CI/CD pipeline.")

    return roadmap
