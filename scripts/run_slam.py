from src.data.waymo_loader import SyntheticLidarDataset
from src.slam.odometry import LidarOdometry
import matplotlib.pyplot as plt

dataset = SyntheticLidarDataset()
slam = LidarOdometry()

for frame in dataset:
    slam.register_frame(frame.points)

traj = slam.get_trajectory()

x = traj[:, 0, 3]
y = traj[:, 1, 3]

plt.plot(x, y, marker='o')
plt.title("Estimated Trajectory")
plt.xlabel("X")
plt.ylabel("Y")
plt.grid()
plt.show()
