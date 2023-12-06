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

input_times = [61709066]
input_distance_to_beat = [643118413621041]

input_times_test = [71530]
input_distance_to_beat_test = [940200]

cnt = 0
for i in range(1, input_times[0] + 1):
    distance = (input_times[0] - i) * i
    if distance > input_distance_to_beat[0]:
        cnt += 1
print(cnt)
