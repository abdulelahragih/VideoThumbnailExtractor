
from flask import Flask, request, Response
from main import generateThumbnailForVideo
app = Flask(__name__)


@app.route('/thumbnail', methods=['POST'])
def thumbnail():
    try:
        data = request.json
        path = data['videoPath']
        thumbnailPath = data['thumbnailPath']
        if generateThumbnailForVideo(path, thumbnailPath):
            return Response(status=200)
        return Response(status=500)
    except Exception as e:
        print(e)
        return Response(status=500)


if __name__ == '__main__':
    # run on the local development server.
    app.run(host="localhost", port=5000)
