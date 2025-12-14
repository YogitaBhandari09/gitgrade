function analyze() {
  const repo = document.getElementById("repo").value;

  fetch("http://127.0.0.1:5000/analyze", {
    method: "POST",
    headers: {"Content-Type": "application/json"},
    body: JSON.stringify({repo_url: repo})
  })
  .then(res => res.json())
  .then(data => {
    document.getElementById("result").innerHTML =
`Score: ${data.score}/100

Summary:
${data.summary}

Roadmap:
- ${data.roadmap.join("\n- ")}
`;
  });
}
