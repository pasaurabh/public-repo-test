from flask import Flask
import datetime
import os
app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello world!'

@app.route('/time')
def getTime():
    return datetime.datetime.now().strftime("%m/%d/%Y, %H:%M:%S")

if __name__ == "__main__":
    print("Initiating Flask App")
    port = int(os.environ.get("PORT", 5000))
    app.run(debug=True,host='0.0.0.0',port=port)


