import numpy as np

class LidarFrame:
    def __init__(self, points, pose=None, timestamp=None):
        self.points = points
        self.pose = pose
        self.timestamp = timestamp

class SyntheticLidarDataset:
    def __init__(self, num_frames=20):
        self.num_frames = num_frames
        self.points_per_frame = 2000

    def __iter__(self):
        base = np.random.uniform(-20, 20, (self.points_per_frame, 3))

        for i in range(self.num_frames):
            pose = np.eye(4)
            pose[0, 3] = i * 0.5

            noise = np.random.normal(0, 0.05, base.shape)
            points = base + noise + np.array([i * 0.5, 0, 0])

            yield LidarFrame(points, pose, i)
