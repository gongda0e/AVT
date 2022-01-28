import os
import numpy as np
import pdb

class i3dReader :
    def __init__(self,):
        self.root_path = './DATA/50salads/features'

    def get_i3d_50s(self, *args) :
        """get i3d features from the index"""
        video_path, start_sec, end_sec, fps, df_row = args
        start_frame = np.floor(start_sec * fps)
        end_frame = np.floor(end_sec * fps)
        frames = np.arange(end_frame, start_frame, -1).astype(int)[::-1]
        filename = video_path.split('/')[-1].split('.')[0]
        features = np.load(os.path.join(self.root_path,video_path))


        pdb.set_trace()

def get_i3d_50s(*args) :
    """get i3d features from the index"""
    root_path = '/home/gongda0e/research/anticipation/AVT/DATA/50salads/features'
    video_path, start_sec, end_sec, fps, df_row = args
    start_frame = int(np.floor(start_sec * fps))
    end_frame = int(np.floor(end_sec * fps))
    frames = np.arange(end_frame, start_frame, -1).astype(int)[::-1]
    filename = video_path.split('/')[-1].split('.')[0]
    features = np.load(os.path.join(root_path,filename+'.npy'))
    features = features.transpose()
    features = features[start_frame:end_frame]
    pdb.set_trace()





