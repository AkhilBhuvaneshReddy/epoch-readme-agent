from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import ChatPromptTemplate
from langchain.agents import create_agent
from app.config import GOOGLE_API_KEY
from app.tools import calculator

from app.tools import calculator, generate_readme

tools = [calculator, generate_readme]

llm = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash",
    google_api_key=GOOGLE_API_KEY,
    temperature=0.3
)

prompt = ChatPromptTemplate.from_messages([
    ("system", "You are a helpful AI assistant."),
    ("human", "{question}")
])

agent = create_agent(
    model=llm,
    tools=tools,
    system_prompt="""
You are an intelligent AI agent.

If the user asks to generate a README for a project folder,
you MUST use the generate_readme tool.

Use tools whenever appropriate.
""",
)

chain = prompt | llm

def run_genai(question: str) -> str:
    response = chain.invoke({"question": question})
    return response.content

# Run the agent
def run_agent2(question: str) -> str:
    result = agent.invoke(
        {"messages": [{"role": "user", "content": question}]}
    )

    final_message = result["messages"][-1]

    content = final_message.content

    # Gemini sometimes returns list of content blocks
    if isinstance(content, list):
        text_parts = []
        for block in content:
            if isinstance(block, dict) and "text" in block:
                text_parts.append(block["text"])
        return "\n".join(text_parts)

    return str(content)
