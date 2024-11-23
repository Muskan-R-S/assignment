import requests
import time

class VidoeTranslator():
    def __init__(self):
        self.api_url = "http://127.0.0.1:5000"
    
    def getStatus(self, maxRetry):
        retry_delay = 1
        try:
            for i in range(maxRetry):
                print(i)
                response = requests.get(f"{self.api_url}/status")
                status = response.json()

                if status["result"] == "Completed":
                    return "Completed"
                else:
                    time.sleep(retry_delay)
                    retry_delay *= 2

        except requests.exceptions.RequestException as e:
            print("Error", e)

            return None
        



