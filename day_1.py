from day_1_input import day_1_input as raw_calorie_data

# formatting the raw data into subarrays
raw_calorie_data = raw_calorie_data.split("\n\n")
for index, calories in enumerate(raw_calorie_data):
    raw_calorie_data[index] = calories.split("\n")

# variables to track the calories
max_cals = 0
total_cal_list = []

# iterate over each subarray to find the sum
# if greatest found so far, store as max_cals
# add each subarray total to total_cal_list
for cal_list in raw_calorie_data:
    calories = sum(map(int, cal_list))
    total_cal_list.append(calories)
    if calories > max_cals:
        max_cals = calories

# output the subarray with the most calories
print(max_cals)

# sort the total_cal_list to find the top three
# output their sum
total_cal_list.sort()
print(sum(total_cal_list[-3:]))