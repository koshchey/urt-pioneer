from setuptools import find_packages, setup

package_name = 'launch_bringup'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        # Launch files:
        ('share/' + package_name + '/launch', ['launch/stereo_launch_test.py']),
        ('share/' + package_name + '/launch', ['launch/rtab_launch_test.py']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='pioneer1',
    maintainer_email='pioneer1@todo.todo',
    description='TODO: Package description',
    license='Apache-2.0',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
        ],
    },
)
