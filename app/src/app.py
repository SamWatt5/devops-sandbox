import requests, json
from flask import Flask

app = Flask(__name__)

@app.route('/fact')
def fact():
    r = requests.get("https://uselessfacts.jsph.pl/api/v2/facts/random")
    data = json.loads(r.text)
    fact_text = data['text']
    return {"text":fact_text}
    #return r.json()

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
