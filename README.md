# Newmark Method Update A&V Script

在已知u的情况下，得到纽马克积分的A和V的理论值，用于验证仿真结果或者优化纽马克方法

This script performs calculations using the Newmark method for structural dynamics analysis. It reads displacement data from a CSV file, calculates velocity and acceleration, and saves the results to a new CSV file.

## Prerequisites

Ensure you have Python installed on your system. The script requires the following Python packages:

- `numpy`
- `pandas`

You can install these packages using the following command:

```bash
pip install numpy pandas
```

## Usage

To run the script, use the following command format:

```bash
python newmark_update_AV.py --alpha <alpha> --delta <delta> --a0 <initial_acceleration> --v0 <initial_velocity> --dt <time_step> --input_file <input_csv> --output_file <output_csv>
```

## Parameters

`--alpha`: The alpha parameter for the Newmark method (e.g., 0.5).
`--delta`: The delta parameter for the Newmark method (e.g., 1).
`--a0`: Initial acceleration (e.g., 15.275).
`--v0`: Initial velocity (e.g., 0.061099).
`--dt`: Time step size (e.g., 0.004).
`--input_file`: Path to the input CSV file containing displacement data.
`--output_file`: Path to the output CSV file where results will be saved.

## Example

```bash
python newmark_update_AV.py --alpha 0.5 --delta 1 --a0 15.275 --v0 0.061099 --dt 0.004 --input_file input.csv --output_file output.csv
```

This command will read the displacement data from input.csv, perform the calculations, and save the results (displacement, velocity, and acceleration) to output.csv.

## Input File Format

The input CSV file should have a single column named displacement, containing the displacement data values. The values will be automatically scaled during the calculation.

### Example Input CSV

```csv
displacement
1.222
3.0101
2.9205
...
```

## Output File Format
The output CSV file will contain the following columns:

`displacement`: The original displacement values.
`velocity`: The calculated velocity values.
`acceleration`: The calculated acceleration values.
