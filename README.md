An AI-powered Project README Generation Agent built using LangChain, Google Gemini, and FastAPI.
This agent analyzes a given project folder, understands its structure and code, and automatically generates a structured and professional README.md file.

🧠 Project Overview
Writing documentation is often repetitive and time-consuming. This project demonstrates how Agentic AI can automate documentation generation by:
Scanning all relevant files in a project directory
Understanding project structure and purpose
Using Google Gemini for semantic analysis
Generating a clean, comprehensive README file
The system follows a modular, tool-based agent architecture.

⚙️ Tech Stack
Python
FastAPI
LangChain
Google Gemini (gemini-2.5-flash)
Pydantic

🏗 Architecture
The system is designed using an agent + tool approach:
User → FastAPI → Agent → Custom Tool → Gemini → README.md
Key Components
__main__.py – FastAPI entry point
agents.py – Agent configuration and execution logic
tools.py – Custom LangChain tools (including README generator)
config.py – Gemini API configuration
models.py – Request and response schemas

🚀 How to Run
1️⃣ Clone the repository

git clone https://github.com/AkhilBhuvaneshReddy/epoch-readme-agent.git
cd epoch-readme-agent
2️⃣ Create virtual environment

python3 -m venv venv
source venv/bin/activate
3️⃣ Install dependencies

pip install -r requirements.txt
4️⃣ Add your Gemini API key
Create a .env file in the root directory:

GOOGLE_API_KEY=your_api_key_here

▶️ Run the Server

uvicorn app.__main__:app --reload
Open:

http://127.0.0.1:8000/docs

📌 Example Usage
Send a POST request to:

/genai/agent
Request body:

{
  "question": "Generate a README for project located at ./test_project"
}
The agent will:
Analyze the specified folder
Generate a structured README
Save it inside the target directory

🛡 Edge Case Handling
Skips virtual environments and system folders
Handles unreadable or empty files safely
Limits file size to prevent token overflow
Gracefully handles missing directories

🎯 Purpose
This project was built to demonstrate:
Tool-calling agent architecture
Practical use of LLMs for automation
Clean backend integration with FastAPI
Real-world AI-powered documentation generation

👨‍💻 Author
Akhil Bhuvanesh Reddy GitHub: https://github.com/AkhilBhuvaneshReddy
