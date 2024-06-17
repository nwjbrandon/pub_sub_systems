import zmq
import cv2
from utils import decode_msg

def main() -> None:
    connect_to = "tcp://localhost:5555"

    topic = 'video_analytics'
    ctx = zmq.Context()
    s = ctx.socket(zmq.SUB)
    s.connect(connect_to)

    print(f"Receiving messages on topics: {topic} ...")
    s.setsockopt(zmq.SUBSCRIBE, topic.encode('utf-8'))

    try:
        while True:
            _, msg = s.recv_multipart()
            msg = decode_msg(msg)

            frame = msg["frame"]
            frame_id = msg["frame_id"]
  
            cv2.imshow('Subscriber', frame)

            print(f"Frame: {frame_id}")
            if cv2.waitKey(1) == ord('q'):
                break
            
    except KeyboardInterrupt:
        pass
    print("Done.")


if __name__ == "__main__":
    main()