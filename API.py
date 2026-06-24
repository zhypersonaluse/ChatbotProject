from fastapi import FastAPI
from pydantic import BaseModel
from graph import run_agent
import time

# Creating FastAPI app instance
app = FastAPI()

qs=["get_chat"]
# Define the request body structure using Pydantic model
class Query(BaseModel):
    message: str  # capturing user's message

# Define POST endpoint to handle incoming chat messages
@app.post("/chat")
async def chat_endpoint(query: Query):
    print("query:", query)
    qs.append(qs)
    start = time.time()  # timer to measure execution time
    try:
        response= run_agent(query.message)  # getting response and token usage from LLM API
        exec_time = round(time.time() - start, 2)  # how long the API call took
        return {
            "response": response,
            "execution_time": exec_time
        }
    except Exception as e:
        print(f"Error: {str(e)}")  # for debugging purposes
        return {"error": str(e)}  # returning actual error message to help frontend handle it