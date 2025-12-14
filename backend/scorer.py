def calculate_score(data):
    score = 0

    score += min(data["files"] * 2, 20)
    score += min(data["commits"] * 2, 20)
    score += 20 if data["has_readme"] else 0
    score += min(len(data["languages"]) * 10, 20)
    score += 20 if data["stars"] > 0 else 0

    score = min(score, 100)

    # AI-style summary
    if score >= 80:
        summary = (
            "This repository demonstrates strong engineering practices with a well-structured "
            "codebase, consistent development activity, and good use of version control. "
            "It reflects readiness for real-world applications."
        )
    elif score >= 50:
        summary = (
            "This project shows a solid foundation but lacks consistency in documentation, "
            "testing, or commit discipline. With focused improvements, it can become production-ready."
        )
    else:
        summary = (
            "This repository represents an early-stage project. Strengthening documentation, "
            "improving structure, and adopting better Git practices will significantly enhance its quality."
        )

    return score, summary
