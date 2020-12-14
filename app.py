from flask import Flask
from flask import render_template, request, jsonify
from urllib.parse import unquote
import youtube_scrapper

app = Flask(__name__)

@app.route('/')
def get_comments():
    # ytURL = request.form.get('youtubeURL', "")
    # data = dict()
    # if ytURL!="":
    #     video_id = ytURL.split("=")[1]
    #     views, likes, dislikes, comments  = youtube_scrapper.main(video_id)
    #     data = {"ytURL":ytURL,
    #         "views": views,
    #         "likes": likes,
    #         "dislikes": dislikes,
    #         "comments": comments}
    #     print(data)
    # else:
    data = {"ytURL":"",
        "views": "",
        "likes": "",
        "dislikes": "",
        "comments": ""}

    return render_template("index.html", data=data)

@app.route('/results', methods=['GET', 'POST'])
def get_comments_again():
    ytURL = request.form.get('youtubeURL', "")
    # print(ytURL)
    ytURL = unquote(ytURL)
    # print(ytURL)
    
    data = dict()
    if ytURL!="":
        video_id = ytURL.split("=")[1]
        ytURL = "https://www.youtube.com/embed/"+video_id
        views, likes, dislikes, comments  = youtube_scrapper.main(video_id)
        data = {"ytURL":ytURL,
            "views": views,
            "likes": likes,
            "dislikes": dislikes,
            "comments": comments}
        # print(data)
    else:
        data = {"ytURL":"",
            "views": "",
            "likes": "",
            "dislikes": "",
            "comments": ""}

    return render_template("results.html", data=data)    

def main():
    app.run(host='0.0.0.0', port=3001, debug=True)


if __name__ == '__main__':
    main()

# from flask import Response
# @app.route("/")
# def index():
#     return Response(
#         "The response body goes here",
#         status=400,
#     )