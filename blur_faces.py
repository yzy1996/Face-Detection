import face_recognition
import cv2

#给人脸打码
video_capture = cv2.VideoCapture(0)
face_locations = []

while True:
    ret, frame = video_capture.read()
    small_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)
    face_locations = face_recognition.face_locations(small_frame, model="cnn")
    for top, right, bottom, left in face_locations:       
        top *= 4
        right *= 4
        bottom *= 4
        left *= 4
        face_image = frame[top:bottom, left:right]
        face_image = cv2.GaussianBlur(face_image, (99, 99), 30)      #一个高斯模糊就可以了
        frame[top:bottom, left:right] = face_image
    cv2.imshow('Video', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

video_capture.release()
cv2.destroyAllWindows()
