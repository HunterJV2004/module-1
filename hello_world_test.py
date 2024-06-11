seconds = 60
minutes = 60
seconds_per_hour = seconds * minutes
seconds_per_day = seconds_per_hour * 24
print("floating point division - " + str(seconds_per_day/seconds_per_hour)) ##Results are 24.0
print("integer division - " + str(seconds_per_day//seconds_per_hour)) ##Results are 24