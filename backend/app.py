from flask import Flask, request, jsonify
from flask_cors import CORS
from github_analyzer import analyze_repo
from scorer import calculate_score
from roadmap import generate_roadmap


app = Flask(__name__)
CORS(app)


@app.route("/analyze", methods=["POST"])
def analyze():
    data = request.json
    repo_url = data.get("repo_url")

    analysis = analyze_repo(repo_url)
    score, summary = calculate_score(analysis)
    roadmap = generate_roadmap(analysis)

    return jsonify({
        "score": score,
        "summary": summary,
        "roadmap": roadmap
    })

if __name__ == "__main__":
    app.run(debug=True)
