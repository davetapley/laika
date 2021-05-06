import csv
import datetime
from laika import raw_gnss as raw, AstroDog
from gps_time import GPSTime

time = GPSTime.from_datetime(datetime.datetime(2021, 5, 5, 17, 29, 47, 429606))

print(time)

with open('input.tsv') as file:
  lines = [{ k: float(n) if k != "PRN" else n for k,n in line.items() } for line in csv.DictReader(file,delimiter="\t")]

print(lines)

meas = [raw.GNSSMeasurement(l['PRN'], time.week_number, time.time_of_week, l, l) for l in lines]

dog = AstroDog()
processed = raw.process_measurements(meas, dog)
pos = raw.calc_pos_fix(processed)
print(pos)