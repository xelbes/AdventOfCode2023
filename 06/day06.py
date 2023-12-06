from time import time

time_part_1 = time()
input_times = [61, 70, 90, 66]
input_distance_to_beat = [643, 1184, 1362, 1041]
result = 1
for index, value in enumerate(input_times):
    cnt = 0
    for i in range(1, input_times[index] + 1):
        distance = (input_times[index] - i) * i
        if distance > input_distance_to_beat[index]:
            cnt += 1
    result *= cnt
print(result)
print("Time Part 1:", round(time() - time_part_1, 5))

time_part_2 = time()
input_times = [61709066]
input_distance_to_beat = [643118413621041]
cnt = 0
for i in range(1, input_times[0] + 1):
    distance = (input_times[0] - i) * i
    if distance > input_distance_to_beat[0]:
        cnt += 1
print(cnt)
print("Time Part 2:", round(time() - time_part_2, 2))
