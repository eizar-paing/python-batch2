from datetime import datetime
from zoneinfo import ZoneInfo

now = datetime.now(ZoneInfo("Asia/Rangoon"))
print(now.strftime("%H:%M:%S %Z"))

now = datetime.now()
print(now.strftime("Today is %%"))  # Output: Today is %

# Output: Progress: 50% complete


# Date near New Year's, to show the difference
dt = datetime.strptime("2022-01-01", "%Y-%m-%d")

print("Calendar year (%Y):", dt.strftime("%Y"))
print("ISO week year (%G):", dt.strftime("%G"))


print(now.strftime("Progress: 50%% complete"))  
