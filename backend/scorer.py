def calculate_score(data):
    score = 0

    # ---------- 1. Project Structure (max 18) ----------
    if data["files"] <= 3:
        structure = 4
    elif data["files"] <= 8:
        structure = 9
    elif data["files"] <= 20:
        structure = 14
    else:
        structure = 18
    score += structure

    # ---------- 2. Commit Consistency (max 18) ----------
    if data["commits"] < 5:
        commits = 4
    elif data["commits"] < 15:
        commits = 9
    elif data["commits"] < 40:
        commits = 14
    else:
        commits = 18
    score += commits

    # ---------- 3. Documentation Quality (max 16) ----------
    if data["has_readme"]:
        documentation = 12
    else:
        documentation = 4
    score += documentation

    # ---------- 4. Tech Stack Depth (max 16) ----------
    lang_count = len(data["languages"])
    if lang_count == 1:
        tech = 8
    elif lang_count == 2:
        tech = 12
    else:
        tech = 16
    score += tech

    # ---------- 5. Community / Relevance (max 12) ----------
    # Reduced impact of stars
    if data["stars"] == 0:
        community = 3
    elif data["stars"] < 10:
        community = 6
    elif data["stars"] < 100:
        community = 9
    else:
        community = 12
    score += community

    # ---------- Penalize Trivial / Demo Repositories ----------
    if data["files"] <= 3:
        score = min(score, 40)

    # ---------- Penalize Popular but Shallow Repos ----------
    if data["stars"] > 100 and data["files"] < 10:
        score -= 10

    # ---------- Clamp Final Score ----------
    score = max(20, min(score, 90))

    # ---------- AI Mentor Summary ----------
    if score >= 75:
        summary = (
            "This repository demonstrates strong development practices with a well-organized "
            "codebase and consistent contribution patterns. It reflects a mature project that "
            "could be extended or productionized with minor improvements."
        )
    elif score >= 55:
        summary = (
            "This project represents an average-quality repository with a reasonable structure "
            "and basic documentation. Improving consistency, testing, and modularity would "
            "significantly enhance its overall quality."
        )
    else:
        summary = (
            "This repository appears to be an early-stage or learning project. The project would "
            "benefit from better organization, clearer documentation, and more consistent commits."
        )

    return score, summary
