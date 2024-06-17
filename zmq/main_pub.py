import time
import zmq
import cv2
from utils import encode_msg

def main() -> None:
    bind_to = "tcp://localhost:5555"

    topic = b'video_analytics'

    ctx = zmq.Context()
    s = ctx.socket(zmq.PUB)
    s.bind(bind_to)
    time.sleep(1.0)


    cap = cv2.VideoCapture(0)
    if not cap.isOpened():
        print("Cannot open camera")
        return

    frame_id = 0
    try:
        while True:
            t1 = time.time()

            ret, frame = cap.read()
            if not ret:
                break

            msg = {
                "frame": frame,
                "annotated": frame,
                "frame_id": frame_id,
            }

            msg = encode_msg(msg)
            cv2.imshow('Publisher', frame)
            s.send_multipart([topic, msg])

            t2 = time.time()

            print(f"Frame: {frame_id} | Duration: {round(t2 - t1, 5)}")
            frame_id += 1
            if cv2.waitKey(1) == ord('q'):
                break
    except KeyboardInterrupt:
        pass
    cap.release()
    cv2.destroyAllWindows()


if __name__ == "__main__":
    main()