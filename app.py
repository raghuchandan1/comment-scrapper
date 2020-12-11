from flask import Flask
from flask import render_template, request, jsonify
import example

app = Flask(__name__)

@app.route('/')
def get_comments():
    text = example.main()
    # print(emotion)
    return render_template("index.html", emotion=text)

def main():
    app.run(host='0.0.0.0', port=3001, debug=False)


if __name__ == '__main__':
    main()