# VideoTranslator Client Library

A Python library to interact with a video translation server and efficiently check the job(video translation) status. The library handles HTTP requests to the /status endpoint and incorporates a retry mechanism with exponential backoff that minimizes delays.

## Requirements 
- Python 3.x  
- `requests` library (`pip install requests`)

## Starter Code  
```python
from main import VideoTranslator

vt = VideoTranslator()
cur_status = translator.get_status(maxRetry=5)
print(f"Job Status: {cur_status}")
```

# Backend Server  

The backend server implements a status API and returns a result that is pending, completed or error. 
This is just simulating the video translation backend. 
The response can be:  
- **`Pending`**: The job is still in progress (based on a configurable delay).  
- **`Completed`**: The job is finished once the configured delay time has passed.  
- **`Error`**: An error occurred while processing the request.  

### Requirements  
- Python 3.x  
- Flask (`pip install flask`)  

### How It Works  
1. The server starts with a **start time** and a configurable **delay time** (`SECONDS_DELAY`), determining how long the status remains `Pending`.  
2. When the `/status` endpoint is called:
   - The server calculates the time elapsed since it started.
   - If the elapsed time exceeds the `SECONDS_DELAY`, the response is `Completed`. Otherwise, it returns `Pending`.  
3. Any unexpected exceptions return an `Error` response with a `404` status code.  

### Setting Up the Server  

1. **Install Flask**:  
   ```bash
   pip install flask
   ```
2. **Set Environment Variables**
   ```bash
   export SECONDS_DELAY=50
   ```
3. **Runn Server**
   ```bash
   python3 -m flask run
   ```

