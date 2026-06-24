from dotenv import load_dotenv

load_dotenv()

from langgraph.graph import END, StateGraph
from langchain_core.messages import SystemMessage, HumanMessage, ToolMessage
from db_tools import get_retriever
from langchain_openai import OpenAIEmbeddings, ChatOpenAI
from langchain.tools import tool

embedding = OpenAIEmbeddings()
C1_DB_PATH = "./C1_DB"
C2_DB_PATH = "./C2_DB"

@tool
def retrieval_C1(questions: str):
    """Retrieve the documentation from company C1"""
    retriever_C1 = get_retriever(collection_name="Company-One", embedding=embedding, db_path=C1_DB_PATH)
    contents = retriever_C1.invoke(questions)
    output = []
    for cont in contents:
        output.append(cont.page_content)
    return output

@tool
def retrieval_C2(questions: str):
    """Retrieve the documentation from company C2"""
    retriever_C2 = get_retriever(collection_name="Company-Two", embedding=embedding, db_path=C2_DB_PATH)
    contents = retriever_C2.invoke(questions)
    output = []
    for cont in contents:
        output.append(cont.page_content)
    return output


def run_agent(question: str):
    tools = [retrieval_C1, retrieval_C2]
    tools_dict = {t.name : t for t in tools}

    llm = ChatOpenAI(model = "gpt-4o")
    llm_with_tools = llm.bind_tools(tools)

    print(f"Question: {question}")
    print("="*60)

    system_messages = SystemMessage(
        content = """
        You are an assistant in a company, recently your company just merged with another company and 
        your responsibility is to help the users retrieve the information when asked.
        STRICT RULES - You must follow the following rules exactly:
        1. NEVER guess the answer. Only retrieve the closest information from the database and present it.
        2. If customer only ask the information from one company, just use the specific tools instead of all tools.
        For example, if the user asks the information from company C1, use the tool retrieval_C1. if the user asks the
        information from company C2, use the tool retrieval_C2. 
        """
    )

    human_message = HumanMessage(
        content = question
    )

    messages = [
        system_messages,
        human_message
    ]

    ai_message = llm_with_tools.invoke(messages)

    messages.append(ai_message)

    tool_calls = ai_message.tool_calls

    for tool in tool_calls:
        tool_name = tool.get("name")
        tool_args = tool.get("args", {})
        tool_call_id = tool.get("id")
        output = tools_dict.get(tool_name).invoke(tool_args)
        tool_message = ToolMessage(content = " ".join(output), tool_call_id=tool_call_id)
        messages.append(tool_message)
        

    final_output = llm_with_tools.invoke(messages)
    
    #print(f"Final Answer is:\n {final_output.content}")

    return final_output.content
# workflow = StateGraph(GraphState)

# workflow.add_node("retrieve C1", retrieval_C1)
# workflow.add_node("retrieve_C2", retrieval_C2)

# workflow.set_entry_point()
# graph = workflow.compile()

# graph.get_graph().draw_mermaid_png(output_file_path="./tt.png")



# print("test run")
# print()
# run_agent("What is the definition of adverse action in C2 and C1?")