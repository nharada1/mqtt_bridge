#!/usr/bin/env python3
import rclpy

from mqtt_bridge.app import mqtt_bridge_node

def main():
    mqtt_bridge_node()

if __name__ == "__main__":
    main()