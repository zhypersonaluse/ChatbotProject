from dotenv import load_dotenv

load_dotenv()

from langgraph.graph import END, StateGraph
from db_tools import get_retriever
from state import GraphState



workflow = StateGraph(GraphState)

workflow.add_node("start_node")
workflow.set_entry_point('start_node')
graph = workflow.compile()

graph.get_graph().draw_mermaid_png(output_file_path="./tt.png")


if __name__ == "__main__":
    print("Chatbot")
