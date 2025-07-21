import cv2
import os

def read_video(video_path):
    """
    Reads a video file and returns the frames as a list.
    
    Args:
        video_path (str): Path to the video file.
        
    Returns:
        list: A list of frames from the video.
    """
    if not os.path.exists(video_path):
        raise FileNotFoundError(f"Video file {video_path} does not exist.")
    
    cap = cv2.VideoCapture(video_path)
    frames = []

    while True:
        ret, frame = cap.read()
        if not ret:
            break
        frames.append(frame)

    return frames

def save_video(frames, output_path, fps=24):
    """    Saves a list of frames as a video file. 
    
    Args:
        frames (list): List of frames to save.
        output_path (str): Path where the video will be saved.
        fps (int): Frames per second for the output video.

    Returns:
        None
    """
    if not os.path .exists(os.path.dirname(output_path)):
        os.makedirs(os.path.dirname(output_path))

    fourcc = cv2.VideoWriter_fourcc(*'XVID')
    out = cv2.VideoWriter(output_path, fourcc, fps, (frames[0].shape[1], frames[0].shape[0]))

    for frame in frames:  
        out.write(frame)
    
    out.release()

    