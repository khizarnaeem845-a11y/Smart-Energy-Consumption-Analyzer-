# Smart Energy Consumption Analyzer ⚡

A Python-based data analysis project that explores electricity readings from a university campus building using **NumPy, Matplotlib, and Python**.

The project analyzes real-world electricity monitoring data from 2019 to identify consumption patterns, peak readings, hourly trends, and statistical anomalies.

## 📌 Project Overview

The Smart Energy Consumption Analyzer processes electricity monitoring data from Building D of the ETSIT Campus Energy Monitoring Dataset.

It uses Python for CSV data handling, NumPy for numerical analysis, and Matplotlib for data visualization.

The main objective is to understand electricity-reading patterns and identify unusual readings through statistical analysis.

## 🎯 Project Objectives

- Load and process a real-world electricity dataset.
- Handle missing and invalid records.
- Calculate basic statistical measurements.
- Identify peak electricity readings.
- Analyze average readings by hour.
- Detect statistical anomalies using the Z-score method.
- Visualize patterns using Matplotlib.

## 🛠️ Technologies Used

| Technology | Purpose |
|---|---|
| Python | Programming and data processing |
| CSV module | Reading CSV datasets |
| NumPy | Numerical and statistical analysis |
| Matplotlib | Data visualization |

## 📂 Project Structure

```text
Smart_Energy_Analyzer/
│
├── dataset/
│   └── edificio_D_pro_power_2019.csv
│
├── main.py
│
└── README.md
```


## 📥 Dataset Setup

This project uses the ETSIT Campus Energy Monitoring Dataset.

The original dataset is not included in this repository. Please obtain it from the original source:

[Download the dataset from Zenodo](https://zenodo.org/records/3942567)

After downloading, place the Building D CSV file in the following location:

`dataset/edificio_D_pro_power_2019.csv`

The project expects this folder structure:

```text
Smart_Energy_Analyzer/
├── dataset/
│   └── edificio_D_pro_power_2019.csv
├── main.py
└── README.md
```


## ⚙️ Project Features

### 1. Data Loading and Cleaning

- Reads CSV data using Python's `csv.DictReader`.
- Checks for missing values.
- Skips invalid records.
- Converts readings into NumPy arrays.

### 2. Statistical Analysis

Calculates:

- Mean
- Maximum
- Minimum
- Standard deviation
- Sum of recorded values

### 3. Peak Reading Detection

Uses NumPy functions to identify the highest recorded electricity measurement and its corresponding date and time.

### 4. Hourly Analysis

Groups readings by hour and calculates the average reading for each hour of the day.

This helps identify periods with higher and lower average readings.

### 5. Anomaly Detection

Uses the Z-score statistical method:

\[
Z = \frac{x-\mu}{\sigma}
\]

Where:

- \(x\) = Individual reading
- \(\mu\) = Mean reading
- \(\sigma\) = Standard deviation

Readings with an absolute Z-score greater than 3 are flagged as statistical anomalies.

### 6. Data Visualization

The project generates four charts:

- Overall electricity readings.
- Electricity readings with detected anomalies.
- Average electricity readings by hour.
- Daily anomaly counts.

## 📈 Analysis Results

Results from the selected Building D dataset:

| Metric | Result |
|---|---:|
| Original data rows | 198,018 |
| Valid readings | 196,828 |
| Missing readings/rows skipped | 1,190 |
| Average reading | 18,403.47 |
| Highest reading | 52,104 |
| Lowest reading | 6,930 |
| Standard deviation | 7,109.46 |
| Detected anomalies | 1,244 |
| Anomaly percentage | 0.632% |

### Peak Reading

- **Date:** 9 January 2019
- **Time:** 12:22 PM
- **Reading:** 52,104

### Hourly Analysis

- Highest average reading: 12:00 PM
- Lowest average reading: 4:00 AM

These results show differences in the building's electricity-reading patterns throughout the day.

## 🚀 Installation and Execution

### Prerequisites

- Python 3.x
- NumPy
- Matplotlib

### Step 1: Clone the repository

```bash
git clone https://github.com/khizarnaeem845-a11y/Smart-Energy-Consumption-Analyzer-.git
```

### Step 2: Open the project directory

```bash
cd Smart_Energy_Analyzer
```

### Step 3: Install dependencies

```bash
pip install numpy matplotlib
```

### Step 4: Run the project

```bash
python main.py
```

Make sure the dataset is available inside the `dataset` folder.

## ⚠️ Limitations

- The current analysis focuses on Building D only.
- Z-score detection identifies statistical outliers, not confirmed equipment faults.
- The measurement unit of the `General` column must be verified from the dataset documentation before interpreting readings as watts or calculating energy consumption.
- Missing and invalid records are excluded from the analysis.
- The sum of individual readings is not necessarily total energy consumed.

## 🔮 Future Improvements

- Compare all four campus buildings.
- Develop more advanced anomaly detection methods.
- Analyze daily, weekly, and monthly patterns.
- Explore correlations between different buildings.
- Build an interactive dashboard.
- Apply machine learning for electricity-demand forecasting.

## 👨‍💻 Author

**Khizar Naeem**

B.Tech Computer Science Engineering – AI/ML

This project is part of my practical learning journey in Python, NumPy, data analysis, and AI/ML engineering.

---

⭐ If you find this project interesting, feel free to explore the repository and its analysis.