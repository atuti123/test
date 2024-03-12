from fastapi import FastAPI, HTTPException, Response
import os
import requests

app = FastAPI()

# Get the URL from the environment variable
API_URL = os.getenv("API_URL")

if API_URL is None:
    raise ValueError("API_URL environment variable is not set")

@app.get("/")
def get_api_response():
    try:
        # Make API request
        response = requests.get(API_URL)
        
        # Check if request was successful
        response.raise_for_status()
        
        # Return the API response as an HTTP response
        return Response(content=response.content, media_type=response.headers["Content-Type"])
    except requests.exceptions.RequestException as e:
        raise HTTPException(status_code=500, detail=f"Error fetching data from API: {str(e)}")

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=80)