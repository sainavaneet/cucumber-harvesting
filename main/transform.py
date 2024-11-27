import tf
import rospy

def get_transformation(target_frame, source_frame):
    listener = tf.TransformListener()
    rospy.init_node('tf_listener')

    # Wait for up to 10 seconds for the frame to become available
    try:
        listener.waitForTransform(target_frame, source_frame, rospy.Time(), rospy.Duration(10.0))
        (trans, rot) = listener.lookupTransform(target_frame, source_frame, rospy.Time(0))
        print(f"Translation: {trans}, Rotation: {rot}")
    except (tf.LookupException, tf.ConnectivityException, tf.ExtrapolationException) as e:
        print(f"Error: {e}")

# Example usage
get_transformation('/puppet_left/gripper_link', '/world')  # Adjust source_frame as necessary
