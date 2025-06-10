
from langgraph.graph import StateGraph, END
from agents.researcher import researcher_agent
from agents.coder import coder_agent
from agents.explainer import explainer_agent

class ChatState:
    def __init__(self, messages=None):
        self.messages = messages or []

def route(state: dict) -> str:
    last_msg = state["messages"][-1].content.lower()
    if "code" in last_msg:
        return "coder"
    elif "explain" in last_msg or "how" in last_msg:
        return "explainer"
    else:
        return "researcher"

def build_graph():
    builder = StateGraph(dict)

    builder.add_node("researcher", researcher_agent)
    builder.add_node("coder", coder_agent)
    builder.add_node("explainer", explainer_agent)

    builder.set_entry_point("researcher")

    builder.add_conditional_edges(
        "researcher",
        route,
        {
            "researcher": "researcher",
            "coder": "coder",
            "explainer": "explainer"
        }
    )

    builder.add_edge("coder", END)
    builder.add_edge("explainer", END)

    return builder.compile()
