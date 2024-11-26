from flask import Flask
import time
from flask import jsonify
import os

app = Flask(__name__)



app.config["SECONDS_DELAY"] = int(os.getenv("SECONDS_DELAY", 50))
app.config["START_TIME"] = time.time()

@app.route("/status")
def get_status():
    try: 
        cur_time = time.time()
        diff_in_seconds = cur_time - app.config["START_TIME"] 
        
        if  diff_in_seconds > app.config["SECONDS_DELAY"] :
            print("Completed")
            result = "Completed"
        else:
            print("Pending")
            result = "Pending"
    except Exception:
        print(f"Error:{Exception}")
        result = "error"
        return jsonify({"result": result}), 404

    return jsonify({"result": result}), 200
    