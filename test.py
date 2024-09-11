import cv2
import subprocess
import numpy as np
import select
import threading


def read_stderr(ffmpeg_process):
    # FFmpeg stderr 로그 출력 (오류나 경고 모니터링)
    while True:
        output = ffmpeg_process.stderr.readline()
        if output == b'' and ffmpeg_process.poll() is not None:
            break
        if output:
            print(output.decode('utf-8').strip())

def open_rtsp_stream():
    ffmpeg_cmd = [
        'ffmpeg',
        '-rtsp_transport', 'tcp',               
        # '-i', 'rtsp://admin:1234@117.17.159.143/video1',
        '-i', 'rtsp://admin:1234@117.17.159.195/stream1',

        '-c:v', 'h264_nvdec',
        '-fflags', 'nobuffer',
        '-flags', 'low_delay',
        '-pix_fmt', 'bgr24',
        '-f', 'rawvideo',
        # '-f', 'h264'
        '-vcodec', 'rawvideo',
        '-'
    ]

    # FFmpeg 프로세스를 시작합니다.
    ffmpeg_process = subprocess.Popen(ffmpeg_cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, bufsize=10**8)
    stderr_thread = threading.Thread(target=read_stderr, args=(ffmpeg_process,))
    stderr_thread.start()

    width = 1920
    height = 1080
    frame_size = width * height * 3  # BGR 포맷에서 3채널 (BGR 24비트)

    # 프레임을 읽고 표시하는 루프
    while True:
        ready, _, _ = select.select([ffmpeg_process.stdout], [], [], 0.1)

        if ready:
            raw_frame = ffmpeg_process.stdout.read(frame_size)

            if len(raw_frame) == 0:
                # 데이터가 없으면 계속 시도
                continue

            if len(raw_frame) != frame_size:
                print(f"Incomplete frame received: {len(raw_frame)} bytes")
                continue

            # numpy 배열로 변환 후 OpenCV로 표시
            frame = np.frombuffer(raw_frame, np.uint8).reshape((height, width, 3))
            cv2.imshow('RTSP Stream', frame)

            # ESC 키를 누르면 종료
            if cv2.waitKey(1) & 0xFF == 27:
                break

    cv2.destroyAllWindows()
    ffmpeg_process.terminate()


if __name__ == '__main__':
    open_rtsp_stream()