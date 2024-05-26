from fastapi import FastAPI, File, UploadFile, HTTPException
from fastapi.staticfiles import StaticFiles
from fastapi.responses import JSONResponse, HTMLResponse, FileResponse
import os
from pathlib import Path
from PIL import Image
import numpy as np
from keras.models import load_model  # type: ignore

app = FastAPI()

# Define the upload folder relative to the root directory
UPLOAD_FOLDER = './uploads'
Path(UPLOAD_FOLDER).mkdir(parents=True, exist_ok=True)

# Mount the static directory for serving static files
app.mount("/static", StaticFiles(directory="static"), name="static")

# Load the model once when the server starts
model_path = Path(__file__).parent / "Fashion_Mnist_CNN_Model.h5"
model = load_model(model_path)
class_names = ['T-shirt/top', 'Trouser', 'Pullover', 'Dress', 'Coat', 'Sandal', 'Shirt', 'Sneaker', 'Bag', 'Ankle boot']

@app.get("/", response_class=HTMLResponse)
async def serve_homepage():
    with open(Path(__file__).parent / "static" / "index.html", "r") as file:
        return HTMLResponse(content=file.read(), status_code=200)

@app.get("/favicon.ico", include_in_schema=False)
async def favicon():
    return FileResponse(Path(__file__).parent / "static" / "favicon.ico")

@app.post("/upload")
async def upload_image(image: UploadFile = File(...)):
    if not image.filename:
        raise HTTPException(status_code=400, detail="No image file uploaded")

    file_path = Path(UPLOAD_FOLDER) / image.filename

    try:
        # Save the uploaded image
        with open(file_path, "wb") as buffer:
            buffer.write(image.file.read())

        # Open the image
        loaded_img = Image.open(file_path).convert('L')  # Convert image to grayscale
        loaded_img = loaded_img.resize((28, 28))  # Resize to 28x28
        loaded_img_array = np.array(loaded_img) / 255.0  # Normalize the image
        test_pred_array = np.expand_dims(loaded_img_array, axis=0)  # Add batch dimension

        # Predict the class of the image
        prediction = model.predict(test_pred_array)
        class_index = np.argmax(prediction)
        class_name = class_names[class_index]

        return JSONResponse(content={"message": f"The image is of class: {class_name}"}, status_code=200)

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
