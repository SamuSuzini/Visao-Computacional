import cv2


#cap = cv2.VideoCapture(0)
#alterando altura
# cap.set(3, 300)
# cap.set(4, 300)


cap = cv2.VideoCapture("arquivos/correndo.mp4")

while True:
    sucesso, frame = cap.read()

    if sucesso:
        frame_resize = cv2.resize(frame, (600, 400))
        bordas = cv2.Canny(frame_resize, 100, 100)

        cv2.imshow("Vídeo", bordas)

    if cv2.waitKey(10) & 0xFF == ord("q"):
        break


#%%


cap = cv2.VideoCapture("arquivos/video.mp4")

while True:
    sucesso, frame = cap.read()

    cv2.line(frame, (0,0), (500, 500), (0, 255, 0), 3)
    cv2.rectangle(frame, (500,500), (700, 700), (0,0,255), 5)
    cv2.circle(frame, (800,200), 50, (100,100, 167), 7)
    cv2.putText(frame,
                "Usando OpenCV",
                (700, 710),
                cv2.FONT_HERSHEY_COMPLEX,
                1,
                (0, 0, 255),
                1)

    if sucesso:
        cv2.imshow("Video", frame)

    if cv2.waitKey(10) & 0xFF == ord("q"):
        break