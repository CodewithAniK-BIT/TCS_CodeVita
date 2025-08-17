from math import sin, cos, radians
def find_distance():
    N = int(input())
    device_info = []
    for i in range(N):
        device_id, num_detected = map(int, input().split(":"))
        device_info.append((device_id, num_detected))
    device_data = {}
    for i in range(N):
        device_id = device_info[i][0]
        device_data[device_id] = []
        for j in range(device_info[i][1]):
            detected_id, distance, angle = map(int, input().split())
            device_data[device_id].append((detected_id, distance, angle))
    device1, device2 = map(int, input().split())
    x1, y1 = 0, 0
    for device_id, distance, angle in device_data[device1]:
        if device_id == device2:
            return round(distance, 2)
        x2 = x1 + distance * cos(radians(angle))
        y2 = y1 + distance * sin(radians(angle))
        x1, y1 = x2, y2
    return -1
print(find_distance())
