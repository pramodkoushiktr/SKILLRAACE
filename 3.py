import pandas as pd
import numpy as np

# i) Create a time series using a datetime object in pandas indexed by timestamps
date_rng = pd.date_range(start='2023-01-01', end='2023-01-10', freq='D')
ts = pd.Series(np.random.randn(len(date_rng)), index=date_rng)
print("Time Series Indexed by Timestamps:")
print(ts)

# ii) Use pandas.date_range to generate a DatetimeIndex with an indicated length
date_rng_len = pd.date_range(start='2023-01-01', periods=10, freq='D')
print("\nDatetimeIndex with Indicated Length:")
print(date_rng_len)

# iii) Generate data ranges by setting time zone, localize time zone, and convert to particular time zone using tz_convert and combine two different time zones
date_rng = pd.date_range(start='2023-01-01', end='2023-01-10', freq='D')
date_rng_utc = date_rng.tz_localize('UTC')
date_rng_est = date_rng_utc.tz_convert('US/Eastern')

print("\nDate Range Localized to UTC:")
print(date_rng_utc)
print("\nDate Range Converted to Eastern Time Zone:")
print(date_rng_est)

# Combine two different time zones into a single DataFrame
df = pd.DataFrame({
    'UTC': date_rng_utc,
    'Eastern': date_rng_est
})

print("\nCombined DataFrame with Different Time Zones:")
print(df)

# iv) Perform period arithmetic such as adding and subtracting integers from periods and construct a range of periods using period_range
p = pd.Period('2023-01', freq='M')
p_plus_1 = p + 1
p_minus_1 = p - 1

print("\nPeriod Arithmetic:")
print(p, p_plus_1, p_minus_1)

period_rng = pd.period_range(start='2023-01', end='2023-12', freq='M')
print("\nRange of Periods:")
print(period_rng)
