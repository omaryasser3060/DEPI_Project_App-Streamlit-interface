import requests
import base64
import os
from io import BytesIO
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("AZURE_CAR_API_KEY")
ENDPOINT = os.getenv("AZURE_CAR_ENDPOINT")

HEADERS = {
    "Content-Type": "application/json",
    "Authorization": f"Bearer {API_KEY}"
}

def call_car_model(pil_image):
    if not API_KEY or not ENDPOINT:
        return {"error": "Missing API_KEY or ENDPOINT in code."}

    buffer = BytesIO()
    pil_image.save(buffer, format="JPEG")
    img_bytes = buffer.getvalue()
    img_b64 = base64.b64encode(img_bytes).decode()

    payload = {"image": img_b64}

    try:
        response = requests.post(
            ENDPOINT,
            json=payload,
            headers=HEADERS,
            timeout=30
        )
        response.raise_for_status()
        return response.json()

    except Exception as e:
        return {"error": str(e)}