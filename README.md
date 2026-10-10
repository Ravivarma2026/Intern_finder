# 🚀 AI Internship Finder Agent

### Discover Opportunities. Explore Companies. Build Your Future.

An AI-powered internship discovery assistant designed specifically for college students in India. It uses **LangChain, Ollama, and DuckDuckGo Search** to help students discover relevant internship opportunities based on their preferred role, location, work mode, course, and year of study — without requiring a resume.

---

## ✨ Features

- 🔎 **Smart Internship Search** — Search the web for internships matching your interests.
- 🏢 **Multiple Company Discovery** — Find opportunities across different companies and reduce duplicate listings.
- 🤖 **Local AI Integration** — Run an AI model locally using Ollama.
- 🎯 **Personalized Search** — Filter your search by role, location, work mode, course, and year of study.
- 🌐 **Live Web Search** — Use DuckDuckGo to retrieve relevant search results.
- 📋 **Detailed Opportunity Reports** — View company names, eligibility, required skills, stipends, duration, deadlines, and application links when available.
- 💻 **Interactive Web Interface** — Search easily through a Gradio-powered interface.
- 🛡️ **No Resume Required** — Designed for students who want to explore internships without uploading personal documents.
- 🧭 **Career Guidance** — Discover skills to prepare and possible career paths after an internship.

---

## 🛠️ Tech Stack

| Technology | Purpose |
|---|---|
| Python | Core application logic |
| LangChain | AI agent and tool integration |
| Ollama | Run the language model locally |
| Qwen 3 (0.6B) | Language model |
| DuckDuckGo Search | Web-based internship discovery |
| Gradio | Interactive user interface |
| Python dotenv | Environment variable management |

---

## ⚙️ How It Works

1. **Enter your preferences** — Select your internship role, location, work mode, course, and study year.
2. **Search the web** — DuckDuckGo retrieves relevant internship information using multiple search queries.
3. **Process results with AI** — The LangChain agent analyzes the retrieved information.
4. **Identify unique companies** — The agent attempts to find different companies and avoid duplicate listings.
5. **Generate a report** — Review available internship details, application sources, skills to prepare, and career guidance.

---

## 📂 Project Structure

```text
AI-Internship-Finder/
│
├── agent.py              # Main agent and Gradio interface
├── llm.py                # Ollama language model configuration
├── shared_tools.py       # DuckDuckGo search and internship tool
├── system_prompts.py     # Agent instructions and output format
├── requirements.txt      # Python dependencies
├── .env                  # Optional environment configuration
├── .gitignore            # Files excluded from Git
└── README.md             # Project documentation
```

---

## 🚀 Installation and Setup

### 1. Clone the repository

```bash
git clone YOUR_GITHUB_REPOSITORY_URL
cd AI-Internship-Finder
```

Replace `YOUR_GITHUB_REPOSITORY_URL` with your actual GitHub repository URL.

### 2. Create a virtual environment

```bash
python -m venv venv
```

Activate it on Windows:

```bash
venv\Scripts\activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Install and start Ollama

Download Ollama from [ollama.com](https://ollama.com/).

Pull the model used by the project:

```bash
ollama pull qwen3:0.6b
```

Ensure Ollama is running locally before starting the application.

### 5. Run the application

```bash
python agent.py
```

Open the local Gradio URL displayed in your terminal.

---

## 🔍 Example Search

**Search preferences**

| Field | Example |
|---|---|
| Internship role | AI/ML Intern |
| Location | Chennai |
| Work mode | Remote |
| Year of study | 3rd Year |
| Course | CSE |

**Expected report format**

Each result includes:

- Internship role and company
- Location and work mode
- Stipend and duration
- Eligibility and required skills
- Application deadline and link
- Source and verification notes
- Potential future career paths

The agent aims to find up to **five different companies**, depending on the available search results.

---

## 🎓 Who Is This For?

- College students looking for internships
- Computer Science and Engineering students
- Students exploring AI/ML and software development
- Beginners preparing for their first internship
- Students who want to discover opportunities without uploading a resume

---

## 🔐 Privacy and Reliability

- No resume upload is required.
- The language model can run locally through Ollama.
- Web searches are sent to DuckDuckGo to retrieve public search results.
- Missing information should be marked as **Not specified**.
- Company names, application URLs, stipends, and eligibility details should not be fabricated.
- Search results may be incomplete or outdated. Always verify an opportunity on the original company or application website before applying.

**Note:** Running the language model locally does not mean every part of the application is offline; web search requires an internet connection.

---

## 🚧 Future Enhancements

- [ ] More accurate company-name extraction
- [ ] Duplicate-company detection
- [ ] Direct application URL extraction
- [ ] Internship deadline and availability checks
- [ ] Company-wise internship comparison
- [ ] Saved searches and application tracking
- [ ] Expanded filters for stipend, duration, and skills
- [ ] Improved result ranking and source verification

---

## 🌟 Project Goal

To make internship discovery easier for college students by combining local AI, web search, and a simple interface — helping students spend less time searching and more time learning.

---

## 👨‍💻 Built With

**Python · LangChain · Ollama · Qwen · DuckDuckGo · Gradio**

*Built as a student-focused AI project to make internship discovery simpler and more accessible.*

