import sys
if sys.prefix == '/usr':
    sys.real_prefix = sys.prefix
    sys.prefix = sys.exec_prefix = '/home/pioneer1/Documents/URT-pioneer/sensor_ws/install/imu_test'
