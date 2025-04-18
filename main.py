from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import uvicorn
from  pydantic import BaseModel

from get_llm_response import get_answer

app= FastAPI()

#CORS Settings
origins = {"*"} #Allow all origins (can be modified to restrict access)

app.add_middleware(
    CORSMiddleware,
    allow_origins = origins,
    allow_credentials = True,
    allow_methods = ["*"],
    allow_headers = ["*"]
)

#input Request model
class QuestionRequest(BaseModel):
    question: str

#Response body model
class AnswerResponse(BaseModel):
    answer:str

#Post endpoint
@app.post("/ask",response_model=AnswerResponse)
def answer_question(request: QuestionRequest):
    question = request.question
    answer = get_answer(question)
    return {"answer":answer}


#only runs if you do : python main.py
if __name__ =="__main__":
    uvicorn.run("main:app",host="127.0.0.1",port=8000,reload=True)


