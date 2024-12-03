from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from answerPipelines import answer_router
import uvicorn

app = FastAPI()

#add middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Adjust this to match the frontend URL
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
async def root():    
    return [{'id': 1,"message": "Hello"}, {'id': 2, "message": "Hello world"}]

app.include_router(answer_router, prefix="/haystack", tags=["haystack"])

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)