import numpy as np
import open3d as o3d

class LidarOdometry:
    def __init__(self):
        self.poses = [np.eye(4)]
        self.prev_pcd = None

    def register_frame(self, points):
        pcd = o3d.geometry.PointCloud()
        pcd.points = o3d.utility.Vector3dVector(points)

        if self.prev_pcd is None:
            self.prev_pcd = pcd
            return self.poses[-1]

        reg = o3d.pipelines.registration.registration_icp(
            pcd,
            self.prev_pcd,
            1.0,
            np.eye(4),
            o3d.pipelines.registration.TransformationEstimationPointToPoint()
        )

        transform = reg.transformation
        new_pose = self.poses[-1] @ np.linalg.inv(transform)
        self.poses.append(new_pose)

        self.prev_pcd = pcd
        return new_pose

    def get_trajectory(self):
        return np.array(self.poses)
