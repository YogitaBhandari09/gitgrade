def calculate_score(data):
    score = 0

    # ---------- 1. Project Structure (max 20) ----------
    if data["files"] <= 3:
        structure_score = 5
    elif data["files"] <= 10:
        structure_score = 12
    else:
        structure_score = 20
    score += structure_score

    # ---------- 2. Commit Consistency (max 20) ----------
    if data["commits"] < 5:
        commit_score = 5
    elif data["commits"] < 20:
        commit_score = 12
    else:
        commit_score = 20
    score += commit_score

    # ---------- 3. Documentation (max 20) ----------
    if data["has_readme"]:
        doc_score = 15
    else:
        doc_score = 5
    score += doc_score

    # ---------- 4. Tech Stack Depth (max 20) ----------
    lang_count = len(data["languages"])
    if lang_count == 1:
        tech_score = 10
    elif lang_count == 2:
        tech_score = 15
    else:
        tech_score = 20
    score += tech_score

    # ---------- 5. Community / Relevance (max 20) ----------
    if data["stars"] == 0:
        community_score = 5
    elif data["stars"] < 10:
        community_score = 10
    else:
        community_score = 20
    score += community_score

    # ---------- Penalize Trivial / Demo Repositories ----------
    # Example: Hello-World type repos
    if data["files"] <= 3:
        score = min(score, 45)

    # ---------- Clamp Score ----------
    score = min(score, 95)

    # ---------- AI-Style Mentor Summary ----------
    if score >= 85:
        summary = (
            "This repository reflects strong real-world development practices. "
            "The project is well-structured, actively maintained, and demonstrates "
            "good engineering discipline suitable for production or advanced learning."
        )
    elif score >= 65:
        summary = (
            "This project shows a solid foundation with reasonable structure and development activity. "
            "Improving documentation, testing, or modular design would significantly enhance its quality."
        )
    else:
        summary = (
            "This repository appears to be an early-stage or learning project. "
            "Strengthening the project structure, adding documentation, and maintaining consistent commits "
            "will greatly improve its overall quality."
        )

    return score, summary
