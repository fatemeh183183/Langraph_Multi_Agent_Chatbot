
from langchain.utilities import WikipediaAPIWrapper
from langchain.schema import HumanMessage

wiki = WikipediaAPIWrapper()

def researcher_agent(state: dict) -> dict:
    if not state["messages"]:
        return {"messages": [HumanMessage(content="No input provided.")]}
    query = state["messages"][-1].content
    result = wiki.run(query)
    state["messages"].append(HumanMessage(content=f"[📚 Research Result]\n{result}"))
    return {"messages": state["messages"]}
