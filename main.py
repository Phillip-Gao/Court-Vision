from utils.video_utils import read_video, save_video

def main():

    # read video
    frames = read_video('input_video.mp4')

    # save video
    save_video(frames, 'output_video.avi')

if __name__ == "__main__":
    main()