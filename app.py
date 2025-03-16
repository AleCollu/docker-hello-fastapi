from fastapi import FastAPI

app = FastAPI(title="Hello, World API",
              description="This is a very simple example of a FastAPI app.",
              version="0.1.0",
              responses={404: {"description": "Not found"},
                         500: {"description": "Internal server error"},
                         200: {"description": "Success", "content": {"application/json": {"example": {"message": "Hello, World!"}}}}}
)

@app.get("/",
         tags=["Root"],
         summary="Read the root",
         description="Read the root of the API.")
def read_root():
    return {"message": "Hello, World!"}