import numpy as np
import tf
import rospy

class CoordinateTransformer:
    def __init__(self, target_frame, source_frame):
        rospy.init_node('transform_node', anonymous=True)
        self.listener = tf.TransformListener()
        self.target_frame = target_frame
        self.source_frame = source_frame

    def fetch_transform(self):
        self.listener.waitForTransform(self.target_frame, self.source_frame, rospy.Time(), rospy.Duration(10.0))
        trans, rot = self.listener.lookupTransform(self.target_frame, self.source_frame, rospy.Time(0))
        return trans, rot

    def transform_point(self, point_camera):
        trans, rot = self.fetch_transform()
        translation = np.array(trans)
        rotation = tf.transformations.quaternion_matrix(rot)
        transformation_matrix = np.identity(4)
        transformation_matrix[:3, :3] = rotation[:3, :3]
        transformation_matrix[:3, 3] = translation
        point_homogeneous = np.append(point_camera, 1)
        point_robot = np.dot(transformation_matrix, point_homogeneous)[:3]
        return point_robot

# Example usage:
# transformer = CoordinateTransformer('/puppet_left/gripper_link', '/world')
# print(transformer.transform_point([x, y, z]))  # Replace [x, y, z] with actual coordinates
