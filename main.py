import cv2


def generateThumbnailForVideo(videoPath, thumbnailPath):
    video_capture = cv2.VideoCapture(videoPath)
    success, image = video_capture.read()
    while image.mean() == 0: # skip black frames
        success, image = video_capture.read()
    if success:
        cv2.imwrite(thumbnailPath, image)
        return True
    return False

