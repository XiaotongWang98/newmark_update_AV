# Newmark Method Update A&V Script

在已知u的情况下，得到纽马克积分的A和V的理论值，用于验证仿真结果或者优化纽马克方法。

这个脚本读取包含位移的CSV文件，输出一个包含位移、速度、加速度的新的CSV文件

## Prerequisites

需要用到的python库

- `numpy`
- `pandas`

在文件夹“movePackageTo"中包含所需的库，以及不联网的安装流程

## Usage

将输入文件放在这个文件夹下，然后在CMD命令行进入文件夹

然后使用下列命令运行

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


## Input File Format

输入文件应该是一个只有一列并且列标题为"displacement"的csv文件

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
