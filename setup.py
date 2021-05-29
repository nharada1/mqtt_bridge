import os
from glob import glob

from setuptools import setup

package_name = 'mqtt_bridge'

setup(
    name=package_name,
    version='0.2.1',
    packages=[package_name],
    description='A ROS2 version of the mqtt bridge',
    data_files=[
        ('share/' + package_name, ['package.xml']),
                # Include all launch files.
        (os.path.join('share', package_name, 'launch'), glob(os.path.join('launch', '*.launch.py'))),
    ],
    install_requires=['setuptools', 'paho-mqtt', 'inject', 'msgpack-python'],
    zip_safe=True,
    maintainer='nate',
    maintainer_email='nharada1@gmail.com',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'mqtt_bridge_node = mqtt_bridge.mqtt_bridge_node:main',
        ],
    },
)


