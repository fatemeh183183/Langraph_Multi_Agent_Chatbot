
from langchain.chat_models import ChatOpenAI
from langchain.schema import HumanMessage

llm = ChatOpenAI(temperature=0)

def coder_agent(state: dict) -> dict:
    if not state["messages"]:
        return {"messages": [HumanMessage(content="No task to code.")]}
    prompt = "Write Python code for the following task:\n" + state["messages"][-1].content
    code = llm.invoke([HumanMessage(content=prompt)]).content
    state["messages"].append(HumanMessage(content=f"[💻 Code Generated]\n{code}"))
    return {"messages": state["messages"]}
