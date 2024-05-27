from pytube import YouTube
from yt_dlp import YoutubeDL
import ffmpeg
import PIL.Image as Image
import os
from moviepy.editor import VideoFileClip
from threading import Thread

def clearHistory():
    for file in os.listdir('./'):
        if file.startswith('yt-'):
            os.remove(os.path.join('./', file))

def download(url):
    #yt = YouTube(url)
    #stream = yt.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().get_by_resolution('720p')
    #stream.download('./', 'yt-video.mp4')

    ydl_opts = {
        'format': '((bv*[fps>30]/bv*)[height<=240][ext=mp4]/(wv*[fps>30]/wv*)[ext=m4a]) + ba / (b[fps>30]/b)[height<=240][ext=mp4]/(w[fps>30][ext=mp4]/w[ext=m4a])',
        'outtmpl': 'yt-video',
        'ext': 'mp4',
    }

    with YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])

    print('downloaded')
    return 'yt-video.webm'

def getAudio(video_path):
    clip = VideoFileClip(video_path)
    clip.audio.write_audiofile('./yt-audio.mp3')
    return './yt-audio.mp3'

def splitFrames(video_path):
    import cv2

    for file in os.listdir('frames/'):
        os.remove(os.path.join('frames/', file))

    #clip = VideoFileClip(video_path)
    #clip.set_fps(15)
    #clip.write_videofile('yt-video-vfc.mp4')
    #video_path = 'yt-video-vfc.mp4'

    input_file = video_path
    output_directory = 'frames/'
    nth_frame = 6 # Extract every nth frame

    # Create output directory if it doesn't exist
    os.makedirs(output_directory, exist_ok=True)

    # Open the video file
    cap = cv2.VideoCapture(input_file)

    # Initialize frame counter
    frame_count = 0
    
    num_threads = 0
    threads_done = 0

    threads = []

    def wait_thread(thread, num_threads):
        nonlocal threads_done
        thread.join()
        threads_done += 1
        if threads_done % 50 == 0 or threads_done == num_threads:
            print('Frame {} of {} done'.format(threads_done, num_threads))

    num_threads = cap.get(cv2.CAP_PROP_FRAME_COUNT) // nth_frame

    # Read and save frames
    while cap.isOpened():
        frame_count += 1

        ret, frame = cap.read()

        if not ret:
            break
        
        # Extract every nth frame


        def run(fc, r, f):
            if fc % nth_frame == 0:
                frame_path = os.path.join(output_directory, 'frame_{:04d}.png'.format(fc // nth_frame))
                thread = Thread(target=cv2.imwrite, args=(frame_path, f))
                thread.start()
                Thread(target=wait_thread, args=(thread, num_threads)).start()
                thread.join()
                return True
            
            return False
        
        t = Thread(target=run, args=(frame_count, ret, frame))
        threads.append(t)
        t.start()

    # Release the video capture object
    cap.release()

    # Close all OpenCV windows
    cv2.destroyAllWindows()

    for thread in threads:
        thread.join()

def getFrames():
    output_directory = 'frames/'
    return [Image.open(os.path.join(output_directory, frame)) for frame in sorted(os.listdir(output_directory))]