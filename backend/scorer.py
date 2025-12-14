def calculate_score(data):
    breakdown = {}

    # ---------- 1. Project Structure (max 18) ----------
    if data["files"] <= 3:
        structure = 4
    elif data["files"] <= 8:
        structure = 9
    elif data["files"] <= 20:
        structure = 14
    else:
        structure = 18
    breakdown["Structure"] = structure

    # ---------- 2. Commit Consistency (max 18) ----------
    if data["commits"] < 5:
        commits = 4
    elif data["commits"] < 15:
        commits = 9
    elif data["commits"] < 40:
        commits = 14
    else:
        commits = 18
    breakdown["Commits"] = commits

    # ---------- 3. Documentation (max 16) ----------
    if data["has_readme"]:
        documentation = 12
    else:
        documentation = 4
    breakdown["Documentation"] = documentation

    # ---------- 4. Tech Stack Depth (max 16) ----------
    lang_count = len(data["languages"])
    if lang_count == 1:
        tech = 8
    elif lang_count == 2:
        tech = 12
    else:
        tech = 16
    breakdown["Tech Stack"] = tech

    # ---------- 5. Community / Relevance (max 12) ----------
    if data["stars"] == 0:
        community = 3
    elif data["stars"] < 10:
        community = 6
    elif data["stars"] < 100:
        community = 9
    else:
        community = 12
    breakdown["Relevance"] = community

    score = sum(breakdown.values())

    # ---------- Penalize trivial repos ----------
    if data["files"] <= 3:
        score = min(score, 40)

    score = max(20, min(score, 90))

    # ---------- AI Mentor Summary ----------
    if score >= 75:
        summary = (
            "This repository demonstrates strong development practices with a well-organized "
            "codebase and consistent contribution patterns."
        )
    elif score >= 55:
        summary = (
            "This project represents an average-quality repository with reasonable structure. "
            "Improving documentation, testing, and modularity would enhance its quality."
        )
    else:
        summary = (
            "This repository appears to be an early-stage or learning project. "
            "Better organization and documentation would significantly improve it."
        )

    return score, summary, breakdown
