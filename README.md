# GitGrade 🚀
### AI-Powered GitHub Repository Analyzer

GitGrade is an intelligent system that evaluates GitHub repositories and reflects a developer’s
real strengths and weaknesses through a **Score / Rating, AI-style Summary, and Personalized Roadmap**.

---

## 🎥 Demo Video
🔗 https://github.com/user-attachments/assets/fe9e7417-6970-4f24-9a9f-230de2660302

---

## 🧠 Problem Statement
Students often struggle to understand how their GitHub projects appear to recruiters or mentors.
GitGrade acts as a **repository mirror**, providing honest, actionable feedback based entirely on
real GitHub repository data.

---

## ✨ Features
- GitHub repository analysis via URL
- Score / Rating (0–100)
- Skill Level & Badge (Beginner / Intermediate / Advanced)
- AI-style mentor summary
- Personalized improvement roadmap
- Transparent score breakdown
- Clean and user-friendly interface

---

## 🛠 Tech Stack
- **Backend:** Python, Flask
- **APIs:** GitHub REST API
- **Frontend:** HTML, CSS, JavaScript
- **Deployment:** Streamlit Cloud

---

## ⚙️ How It Works
1. User submits a public GitHub repository URL
2. System fetches repository metadata using GitHub API
3. Repository is evaluated across multiple dimensions:
   - Project structure
   - Commit consistency
   - Documentation quality
   - Tech stack depth
   - Relevance & activity
4. System generates:
   - Numerical score
   - Skill level & badge
   - AI-style mentor summary
   - Personalized improvement roadmap

---

## 🚀 How to Run Locally

```bash
# Install dependencies
pip install -r backend/requirements.txt

# Start backend server
python backend/app.py

