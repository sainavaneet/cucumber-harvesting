import tf
import rospy

def get_transformation(target_frame, source_frame):
    rospy.init_node('tf_listener111', anonymous=True) 
    listener = tf.TransformListener()


    while True:
        listener.waitForTransform(target_frame, source_frame, rospy.Time(), rospy.Duration(10.0))
        (trans, rot) = listener.lookupTransform(target_frame, source_frame, rospy.Time(0))
        print(f"Translation: {trans}, Rotation: {rot}")


get_transformation('/puppet_left/gripper_link', '/world')  
