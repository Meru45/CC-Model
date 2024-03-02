from fastapi import FastAPI, File, UploadFile
import matplotlib.pyplot as plt
import pickle

app = FastAPI()
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

origins = [
    "http://localhost",
    "http://localhost:8000"
    "http://localhost:8080",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post('/')
def general():
    return 'Hi'

@app.post("/wbc")
def upload(file: UploadFile = File(...)):
    try:
        contents = file.file.read()
        with open(file.filename, 'wb') as f:
            f.write(contents)
        data = plt.imread(file.filename)
        # load
        file_name = "xgb_reg.pkl"
        xgb_model_loaded = pickle.load(open(file_name, "rb"))

        result = xgb_model_loaded.predict(data.reshape(1, 240*320*3))
    except Exception:
        return {"message": "There was an error uploading the file"}
    finally:
        file.file.close()

    return {result.item()}
