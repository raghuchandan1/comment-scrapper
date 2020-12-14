import os

import googleapiclient.discovery


def get_statistics_views(youtube, video_id, token=""):
    response = youtube.videos().list(
        part='statistics, snippet',
        id=video_id).execute()

    view_count = response['items'][0]['statistics']['viewCount']
    like_count = response['items'][0]['statistics']['likeCount']
    dislike_count = response['items'][0]['statistics']['dislikeCount']
    return view_count, like_count, dislike_count


def get_comment_threads(youtube, video_id, comments=[], token="", max_results=1000):
    # results = youtube.commentThreads().list(
    #     part="snippet",
    #     pageToken=token,
    #     videoId=video_id,
    #     textFormat="plainText"
    # ).execute()

    # for item in results["items"]:
    #     comment = item["snippet"]["topLevelComment"]
    #     text = comment["snippet"]["textDisplay"]
    #     comments.append(text)

    # if "nextPageToken" in results:
    #     return get_comment_threads(youtube, video_id, comments, results["nextPageToken"])
    # else:
    #     return comments
    request = youtube.commentThreads().list(
        part="snippet,replies",
        maxResults=max_results,
        videoId=video_id
    )
    response = request.execute()
    return response


# def get_comment_count_threads(youtube, video_id, comments_count=[], token=""):
#     results = youtube.commentThreads().list(
#         part="snippet",
#         pageToken=token,
#         videoId=video_id,
#         textFormat="plainText"
#     ).execute()

#     for item in results["items"]:
#         comment_count = item["snippet"]["topLevelComment"]
#         like_count = comment_count["snippet"]["likeCount"]
#         comments_count.append(like_count)

#     if "nextPageToken" in results:
#         return get_comment_count_threads(youtube, video_id, comments_count, results["nextPageToken"])
#     else:
#         return comments_count


def main(video_id):
    # Disable OAuthlib's HTTPS verification when running locally.
    # *DO NOT* leave this option enabled in production.
    os.environ["OAUTHLIB_INSECURE_TRANSPORT"] = "1"

    api_service_name = "youtube"
    api_version = "v3"
    DEVELOPER_KEY = "AIzaSyAaEMuw_JogB-rarI2WvODzKYqwcRZC9vs"

    youtube = googleapiclient.discovery.build(
        api_service_name, api_version, developerKey=DEVELOPER_KEY)
    
    views, likes, dislikes = get_statistics_views(youtube,video_id)
    # print("Stats", get_statistics_views(youtube,"_VB39Jo8mAQ"))
    # print("Comments", get_comment_threads(youtube, "_VB39Jo8mAQ"))
    # print("Comment Count", get_comment_count_threads(youtube, "_VB39Jo8mAQ"))
    comments = get_comment_threads(youtube, video_id)
    return views, likes, dislikes, comments


if __name__ == "__main__":
    main()
