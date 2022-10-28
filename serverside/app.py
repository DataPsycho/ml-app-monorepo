from fastapi import FastAPI, Request
import uvicorn
from serverside.predict import read_model, post_process_result, pre_process_input


app = FastAPI()
MODEL = read_model()


@app.get("/healthcheck/")
async def create_item():
    return {"status": 200, "body": "All Ok"}


@app.post("/predict/")
async def create_item(info: Request):
    req_info = await info.json()
    input_data = pre_process_input(req_info)
    prediction = MODEL.predict(input_data)
    prediction = post_process_result(prediction)
    return {"status": 200, "body": {"class": prediction}}

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=5000, log_level="info")

