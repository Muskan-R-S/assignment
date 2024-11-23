from flask import Flask
import time
from flask import jsonify

app = Flask(__name__)



SECONDS_DELAY = 200
start_time = time.time()


@app.route("/status")
def get_status():
    cur_time = time.time()
    diff_in_seconds = cur_time - start_time
    try:
        if  diff_in_seconds > SECONDS_DELAY:
            print("Completed")
            result = "Completed"
        else:
            print("Pending")
            result = "Pending"
    except:
        result = "error"

    return jsonify({"result": result})
    