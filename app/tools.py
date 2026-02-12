"""
Tools for the agent.
Define your LangChain tools here.
"""

from typing import List, Dict, Any
from langchain.tools import tool
import os
from langchain_google_genai import ChatGoogleGenerativeAI
from app.config import GOOGLE_API_KEY


# -------- Calculator Tool --------
@tool
def calculator(expression: str) -> str:
    """
    Evaluate a math expression.
    Example: "2 + 2 * 10"
    """
    try:
        return str(eval(expression))
    except Exception as e:
        return f"Error: {str(e)}"


# -------- README Generator Tool --------
@tool
def generate_readme(project_path: str) -> str:
    """
    Generate a comprehensive README.md from a project folder.
    """

    project_summary = ""

    for root, dirs, files in os.walk(project_path):
        if "venv" in root or ".git" in root or "node_modules" in root:
            continue

        for file in files:
            if file.endswith((".py", ".js", ".ts", ".json", ".md")):
                file_path = os.path.join(root, file)
                try:
                    with open(file_path, "r", encoding="utf-8") as f:
                        content = f.read()
                        project_summary += f"\n\n### File: {file}\n"
                        project_summary += content[:1200]
                except:
                    pass

    if not project_summary:
        return "No readable files found in the given directory."

    llm = ChatGoogleGenerativeAI(
        model="gemini-2.5-flash",
        google_api_key=GOOGLE_API_KEY,
        temperature=0.2
    )

    prompt = f"""
You are a senior software architect.

Based on the following project content:

{project_summary}

Generate a professional README.md including:

- Project Title
- Description
- Features
- Tech Stack
- Folder Structure
- Installation
- Usage
- Assumptions & Limitations

Output ONLY valid markdown content.
"""

    response = llm.invoke(prompt)
    readme_content = response.content.strip()

    with open("README.md", "w", encoding="utf-8") as f:
        f.write(readme_content)

    return "README.mds generated successfully."
