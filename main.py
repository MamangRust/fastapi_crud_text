import uvicorn
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from repository.text_repository import TextFileRepository
from service.text_service import TextFileService
from typing import List

app = FastAPI()


class Data(BaseModel):
    data: str


text_file_repository = TextFileRepository("data.txt")
text_file_service = TextFileService(text_file_repository)


@app.post("/create_data/")
def create_data(data: Data):
    text_file_service.create_data(data.data)
    return {"message": "Data created successfully"}


@app.get("/read_all_data/")
def read_all_data():
    return text_file_service.read_all_data()


@app.get("/find_by_id/{target_id}")
def find_by_id(target_id: int):
    try:
        return text_file_service.find_by_id(target_id)
    except Exception as e:
        return HTTPException(status_code=404, detail="No found your id")


@app.put("/update_data/{index}")
def update_data(index: int, data: Data):
    text_file_service.update_data(index, data.data)
    return {"message": f"Data at index {index} updated successfully"}


@app.delete("/delete_data/{index}")
def delete_data(index: int):
    text_file_service.delete_data(index)
    return {"message": f"Data at index {index} deleted successfully"}


if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", reload=True, port=8000)
