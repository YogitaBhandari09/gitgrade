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
    resultDiv.innerHTML = `
      <div class="result-card">
        <div class="score">Score: ${data.score} / 100</div>

        <div class="section-title">AI Mentor Summary</div>
        <p>${data.summary}</p>

        <div class="section-title">Personalized Roadmap</div>
        <ul>
          ${data.roadmap.map(item => `<li>${item}</li>`).join("")}
        </ul>
      </div>
    `;
  })
  .catch(() => {
    resultDiv.innerHTML = "<p style='color:red'>Error analyzing repository.</p>";
  });
}
