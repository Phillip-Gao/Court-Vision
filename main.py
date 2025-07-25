from utils.video_utils import read_video, save_video

def main():

    # read video
    frames = read_video('input_videos/video_1.mp4')

    # save video
    save_video(frames, 'output_videos/output_video.avi')

if __name__ == "__main__":
    main()
