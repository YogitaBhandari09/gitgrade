function analyze() {
  const repo = document.getElementById("repo").value;
  const resultDiv = document.getElementById("result");

  resultDiv.innerHTML = "<p>⏳ Analyzing repository...</p>";

  fetch("http://127.0.0.1:5000/analyze", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ repo_url: repo })
  })
  .then(res => res.json())
  .then(data => {
    let level = "";
    let badge = "";

    if (data.score < 40) {
      level = "Beginner";
      badge = "🥉 Bronze";
    } else if (data.score < 65) {
      level = "Intermediate";
      badge = "🥈 Silver";
    } else {
      level = "Advanced";
      badge = "🥇 Gold";
    }

    let breakdownHTML = "";
    for (const key in data.breakdown) {
      breakdownHTML += `<li>${key}: ${data.breakdown[key]}</li>`;
    }

    resultDiv.innerHTML = `
      <div class="result-card">
        <div class="score">Score: ${data.score} / 100</div>
        <p><b>Level:</b> ${level}</p>
        <p><b>Badge:</b> ${badge}</p>

        <div class="section-title">📊 Score Breakdown</div>
        <ul>${breakdownHTML}</ul>

        <div class="section-title">🧠 AI Mentor Summary</div>
        <p>${data.summary}</p>

        <div class="section-title">🛣️ Personalized Roadmap</div>
        <ul>
          ${data.roadmap.map(item => `<li>${item}</li>`).join("")}
        </ul>

        <p style="font-size:12px;opacity:0.7">
          ⚠️ Evaluation is heuristic-based and intended for guidance.
        </p>
      </div>
    `;
  })
  .catch(() => {
    resultDiv.innerHTML = "<p style='color:red'>Error analyzing repository.</p>";
  });
}
