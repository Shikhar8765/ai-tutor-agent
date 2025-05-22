# AI Tutor Agent

An interactive multi-agent tutoring system powered by Google Gemini API, built with Streamlit. It routes user queries to specialized sub-agents (Math, Physics, Chemistry) which utilize tools and LLM integration.

---

## 🏠 Project Overview

**AI Tutor Agent** helps students ask questions in Math, Physics, and Chemistry. It features:

* **TutorAgent**: orchestrator routing queries based on subject.
* **MathAgent**: solves arithmetic, algebra, calculus (uses SymPy and Gemini).
* **PhysicsAgent**: answers physics questions (uses constant lookup and Gemini).
* **ChemistryAgent**: answers chemistry queries (uses Gemini).
* **MemoryBuffer**: retains conversation context for follow-up questions.
* **Streamlit UI**: web interface with session-state persistence.

---

## 📁 Repository Structure

```
ai-tutor/
├── agents/
│   ├── tutor_agent.py
│   ├── math_agent.py
│   ├── physics_agent.py
│   └── chemistry_agent.py
├── tools/
│   ├── calculator.py
│   └── constants_lookup.py
├── utils/
│   ├── classifier.py
│   ├── memory.py
│   └── llm.py
├── main.py
├── requirements.txt
├── .env
└── README.md
```

---

## 🚀 Getting Started

1. **Clone the repo**

   ```bash
   git clone <your-github-url>
   cd ai-tutor
   ```
2. **Create virtual environment**

   ```bash
   python3 -m venv venv
   source venv/bin/activate   # on Windows: venv\Scripts\activate
   ```
3. **Install dependencies**

   ```bash
   pip install -r requirements.txt
   ```
4. **Configure API Key**

   * Create a `.env` file at project root:

     ```env
     GEMINI_API_KEY=your_api_key_here
     ```
5. **Run the app**

   ```bash
   streamlit run main.py
   ```

Open [http://localhost:8501](http://localhost:8501) in your browser and start asking questions!

---

## 📡 Deployment

### Railway

1. Push to GitHub.
2. Create a Railway project and link your GitHub repo.
3. Set the environment variable `GEMINI_API_KEY` in Railway.
4. Configure the start command: `streamlit run main.py`.
5. Deploy and access the public URL.

### Vercel (Alternative)

1. Use `vercel` CLI or web dashboard.
2. Add `STREAMLIT_SERVER_OPTION="server.enableCORS false"` in Environment Variables.
3. Add `GEMINI_API_KEY`.
4. Deployment will publish to `your-project.vercel.app`.

---

## 📦 Agents & Tools

### Agents

* **TutorAgent**: routes queries + manages memory.
* **MathAgent**: uses `tools/calculator.py` (SymPy) and `utils/llm.py`.
* **PhysicsAgent**: uses `tools/constants_lookup.py` and memory-based reminders.
* **ChemistryAgent**: uses `utils/llm.py`.

### Tools

* **calculator.py**: robust math expression parser and solver.
* **constants\_lookup.py**: dictionary of physics constants.

---

## ⭐ Bonus Features

* **MemoryBuffer** for conversational context (follow-ups & reminders).
* **Implicit multiplication** and Unicode operator support (`×`, `÷`).
* **Session state** persistence in Streamlit.

---

## 🔧 Future Improvements

* Add more sub-agents (Chemistry calculations, Coding agent).
* Advanced tool integration (graphing, unit conversions).
* User authentication and personalized sessions.

---

