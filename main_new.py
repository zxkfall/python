# import asyncio
# from bleak import BleakScanner
#
# async def main():
#     devices = await BleakScanner.discover()
#     for d in devices:
#         print(d)
#
# asyncio.run(main())

# import wifi
#
# # list all wifis can be connected
# wifi_list = wifi
# print(wifi_list)

# import pywifi
# from pywifi import const
# import time
#
# wifi = pywifi.PyWiFi()
# iface = wifi.interfaces()[0]
# print(iface.name())

import subprocess

# def connect_to_wifi(ssid, password):
#     try:
#         # 使用networksetup连接WiFi
#         subprocess.run(['networksetup', '-setairportnetwork', 'en0', ssid, password])
#         print("Connected to WiFi")
#     except Exception as e:
#         print(f"Error connecting to WiFi: {e}")
#
# # 替换为你的WiFi名称和密码
# wifi_ssid = 'YourWiFiSSID'
# wifi_password = 'YourWiFiPassword'
#
# connect_to_wifi(wifi_ssid, wifi_password)

# import subprocess
# import re
#
# def get_available_wifi():
#     try:
#         # 使用networksetup命令获取WiFi列表
#         result = subprocess.run(['networksetup', '-listallhardwareports'], capture_output=True, text=True)
#         output_lines = result.stdout.split('\n')
#
#         wifi_list = []
#         interface_found = False
#
#         # 解析输出以找到WiFi接口
#         for line in output_lines:
#             if re.match(r'^Hardware Port: Wi-Fi', line):
#                 interface_found = True
#             elif interface_found and re.match(r'^Device: (.+)', line):
#                 wifi_interface = re.match(r'^Device: (.+)', line).group(1)
#                 break
#
#         # 使用找到的WiFi接口获取WiFi列表
#         if interface_found:
#             result = subprocess.run(['networksetup', '-listpreferredwirelessnetworks', wifi_interface], capture_output=True, text=True)
#             output_lines = result.stdout.split('\n')
#
#             for line in output_lines[1:]:
#                 ssid = line.strip()
#                 wifi_list.append({'SSID': ssid})
#
#         return wifi_list
#     except Exception as e:
#         print(f"Error getting available WiFi: {e}")
#         return []
#
# # 获取可用WiFi列表
# available_wifi_list = get_available_wifi()
#
# # 打印结果
# for wifi in available_wifi_list:
#     print(f"SSID: {wifi['SSID']}")
#
import subprocess
import re

def get_nearby_wifi():
    try:
        # 使用airport命令获取WiFi列表
        result = subprocess.run(['/System/Library/PrivateFrameworks/Apple80211.framework/Versions/Current/Resources/airport', '-s'], capture_output=True, text=True)
        output_lines = result.stdout.split('\n')

        # 解析输出以获取WiFi信息
        wifi_list = []
        for line in output_lines[1:]:
            fields = re.split(r'\s+', line.strip())
            if len(fields) >= 6:
                ssid = fields[0]
                signal_strength = fields[2]
                security = fields[5]
                wifi_list.append({'SSID': ssid, 'Signal Strength': signal_strength, 'Security': security})

        return wifi_list
    except Exception as e:
        print(f"Error getting nearby WiFi: {e}")
        return []

# 获取附近的WiFi列表
nearby_wifi_list = get_nearby_wifi()

# 打印结果
for wifi in nearby_wifi_list:
    print(f"SSID: {wifi['SSID']}, Signal Strength: {wifi['Signal Strength']}, Security: {wifi['Security']}")
