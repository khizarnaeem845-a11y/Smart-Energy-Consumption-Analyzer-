import csv
import numpy as np
import matplotlib.pyplot as plt


# ==================================================
# 1. LOAD AND CLEAN DATASET
# ==================================================

date_values = []
time_values = []
power_values = []
hour_values = []

missing_rows = 0
invalid_rows = 0
total_rows = 0

file_path = "dataset/edificio_D_pro_power_2019.csv"

with open(file_path, "r", newline="", encoding="utf-8") as file:

    reader = csv.DictReader(file)

    print("CSV Columns:", reader.fieldnames)

    for row in reader:
        total_rows += 1

        value = row.get("General")
        time_value = row.get("time")
        date_value = row.get("date")

        # Check for missing values
        if (
            value is None or value.strip() == ""
            or time_value is None or time_value.strip() == ""
            or date_value is None or date_value.strip() == ""
        ):
            missing_rows += 1
            continue

        try:
            reading = float(value)
            hour = int(time_value.split(":")[0])

            if not np.isfinite(reading) or not 0 <= hour <= 23:
                raise ValueError

        except ValueError:
            invalid_rows += 1
            continue

        # Store valid readings
        date_values.append(date_value)
        time_values.append(time_value)
        hour_values.append(hour)
        power_values.append(reading)


# ==================================================
# 2. CONVERT LISTS INTO NUMPY ARRAYS
# ==================================================

power = np.array(power_values)
hours = np.array(hour_values)
dates = np.array(date_values)
times = np.array(time_values)

print("\n========== DATASET SUMMARY ==========")

print("Total CSV rows:", total_rows)
print("Valid readings:", power.size)
print("Missing rows:", missing_rows)
print("Invalid rows:", invalid_rows)

print("Power array size:", power.size)
print("Hour array size:", hours.size)
print("Date array size:", dates.size)
print("Time array size:", times.size)

print("First 5 readings:", power[:5])
print("Data type:", power.dtype)


# ==================================================
# 3. BASIC STATISTICS
# ==================================================

print("\n========== BASIC STATISTICS ==========")

average_power = np.mean(power)
highest_value = np.max(power)
lowest_value = np.min(power)
sum_of_values = np.sum(power)

print("Average reading:", average_power)
print("Highest reading:", highest_value)
print("Lowest reading:", lowest_value)
print("Sum of readings:", sum_of_values)

peak_position = np.argmax(power)

print("Peak position:", peak_position + 1)
print("Peak reading:", power[peak_position])
print("Peak date:", dates[peak_position])
print("Peak time:", times[peak_position])


# ==================================================
# 4. HOURLY ANALYSIS
# ==================================================

print("\n========== HOURLY ANALYSIS ==========")

hour_labels = []
hourly_averages = []
hourly_counts = []

for hour in range(24):

    mask = hours == hour
    selected_values = power[mask]

    if selected_values.size > 0:

        average = np.mean(selected_values)

        hour_labels.append(hour)
        hourly_averages.append(average)
        hourly_counts.append(selected_values.size)

        print(
            "Hour:", hour,
            "| Count:", selected_values.size,
            "| Average:", average
        )

highest_hour_position = np.argmax(hourly_averages)
lowest_hour_position = np.argmin(hourly_averages)

print("\nHighest average hour:", hour_labels[highest_hour_position])
print("Lowest average hour:", hour_labels[lowest_hour_position])


# ==================================================
# 5. ANOMALY DETECTION USING Z-SCORE
# ==================================================

print("\n========== ANOMALY DETECTION ==========")

standard_deviation = np.std(power)

print("Standard deviation:", standard_deviation)

if standard_deviation == 0:
    print("Cannot calculate Z-scores: all readings are identical.")
    anomaly_mask = np.zeros(power.size, dtype=bool)

else:
    z_scores = (power - average_power) / standard_deviation

    # Readings more than 3 standard deviations from the mean
    anomaly_mask = np.abs(z_scores) > 3

anomalies = power[anomaly_mask]

anomaly_dates = dates[anomaly_mask]
anomaly_times = times[anomaly_mask]
anomaly_hours = hours[anomaly_mask]

print("Total anomalies:", anomalies.size)

anomaly_percentage = (anomalies.size / power.size) * 100

print("Anomaly percentage:", anomaly_percentage, "%")

print("\nFirst 10 anomaly records:")

for i in range(min(10, anomalies.size)):
    print(
        "Date:", anomaly_dates[i],
        "| Time:", anomaly_times[i],
        "| Reading:", anomalies[i]
    )


# ==================================================
# 6. HOURLY ANOMALY ANALYSIS
# ==================================================

print("\n========== HOURLY ANOMALIES ==========")

anomaly_hour_labels = []
anomaly_hour_counts = []

for hour in range(24):

    mask = anomaly_hours == hour
    count = np.sum(mask)

    anomaly_hour_labels.append(hour)
    anomaly_hour_counts.append(count)

    print("Hour:", hour, "| Anomalies:", count)


# ==================================================
# 7. DAILY ANOMALY ANALYSIS
# ==================================================

print("\n========== DAILY ANOMALIES ==========")

unique_dates, date_counts = np.unique(
    anomaly_dates,
    return_counts=True
)

for date, count in zip(unique_dates, date_counts):
    print(date, "→", count)

if date_counts.size > 0:

    highest_anomaly_position = np.argmax(date_counts)

    print("\nDate with most anomalies:",
          unique_dates[highest_anomaly_position])

    print("Number of anomalies:",
          date_counts[highest_anomaly_position])

else:
    print("No anomalies detected.")


# ==================================================
# 8. CHART 1 — OVERALL ELECTRICITY READINGS
# ==================================================

plt.figure(figsize=(12, 5))

plt.plot(power)

plt.xlabel("Reading Number")
plt.ylabel("General Reading (dataset units)")
plt.title("Building D - Electricity Readings (2019)")

plt.tight_layout()
plt.show()


# ==================================================
# 9. CHART 2 — ANOMALY DETECTION
# ==================================================

positions = np.arange(power.size)

plt.figure(figsize=(14, 6))

plt.plot(
    positions,
    power,
    label="All readings"
)

plt.scatter(
    positions[anomaly_mask],
    power[anomaly_mask],
    color="red",
    s=10,
    label="Detected anomalies"
)

plt.xlabel("Reading Number")
plt.ylabel("General Reading (dataset units)")
plt.title("Building D - Anomaly Detection")

plt.legend()
plt.tight_layout()
plt.show()


# ==================================================
# 10. CHART 3 — HOURLY AVERAGE READINGS
# ==================================================

plt.figure(figsize=(12, 5))

plt.bar(hour_labels, hourly_averages)

plt.xlabel("Hour of the Day")
plt.ylabel("Average General Reading (dataset units)")
plt.title("Building D - Average Reading by Hour")

plt.xticks(range(24))
plt.grid(axis="y", alpha=0.3)

plt.tight_layout()
plt.show()


# ==================================================
# 11. CHART 4 — DAILY ANOMALY COUNTS
# ==================================================

if date_counts.size > 0:

    plt.figure(figsize=(14, 6))

    plt.bar(unique_dates, date_counts)

    plt.xlabel("Date")
    plt.ylabel("Number of Anomalies")
    plt.title("Building D - Daily Anomaly Counts")

    plt.xticks(rotation=90)
    plt.grid(axis="y", alpha=0.3)

    plt.tight_layout()
    plt.show()


print("\n========== PROJECT ANALYSIS COMPLETED ==========")