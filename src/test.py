import numpy as np
import open3d as o3d
from collections import namedtuple
import rerun as rr 


def read_swc_file(swc_file_path):
    """
    Reads an SWC file and extracts the point coordinates and radii.
    """
    points = []
    with open(swc_file_path, 'r') as file:
        for line in file:
            if not line.startswith('#'):  # Skip comments
                parts = line.split()
                if len(parts) == 7:
                    # Extract x, y, z coordinates and radius
                    x, y, z, radius = map(float, parts[2:6])
                    points.append([x, y, z])  # Only coordinates are used for the point cloud
    return np.array(points)

def create_point_cloud_from_swc(swc_file_path):
    """
    Creates an Open3D point cloud from an SWC file.
    """
    points = read_swc_file(swc_file_path)
    point_cloud = o3d.geometry.PointCloud()
    point_cloud.points = o3d.utility.Vector3dVector(points)
    return point_cloud



PointCloud = namedtuple("ColorGrid", ["positions", "colors"])


def PointCloudTuple(o3d_pcd):
    """Convert an Open3D PointCloud to a PointCloudTuple."""

    pcd_pts = np.asarray(o3d_pcd.points)
    pcd_rgb = np.asarray(o3d_pcd.colors) * 255

    return PointCloud(pcd_pts, pcd_rgb.astype(np.uint8))

