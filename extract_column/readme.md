# CSV and TXT File Processor

`process_file.py` is a versatile Python script designed to handle various operations with CSV and TXT files. It supports converting Tab-separated TXT files to CSV, extracting specific columns from CSV files, and combining these operations into one seamless process.

## Prerequisites

- pandas


## Usage

The script supports three main commands:

1. convert: Convert a Tab-separated TXT file to a CSV file.
2. extract: Extract a specific column from a CSV file.
3. convert_extract: Convert a Tab-separated TXT file to CSV and then extract a specific column from the newly created CSV file.

## Commands and Options

1. Convert TXT to CSV

```bash
python process_file.py convert <input_txt_file> <output_csv_file>
```

- <input_txt_file>: The path to the input TXT file (Tab-separated).
- <output_csv_file>: The path where the output CSV file will be saved.

2. Extract a Column from CSV

```bash
python process_file.py extract <input_file> <column_name> [output_file]
```

- <input_file>: The path to the CSV file.
- <column_name>: The name of the column to extract.
- `[output_file]`: (Optional) The path where the output CSV file containing the extracted column will be saved. If not specified, the column data will be printed to the console.

3. Convert and Extract

```bash
python process_file.py convert_extract <input_txt_file> <column_name> <output_csv_file> [output_file]
```

- <input_txt_file>: The path to the input TXT file (Tab-separated).
- <column_name>: The name of the column to extract from the resulting CSV.
- <output_csv_file>: The path where the converted CSV file will be saved.
- [output_file]: (Optional) The path where the output CSV file containing the extracted column will be saved. If not specified, the column data will be printed to the console.

## Examples

1. Convert TXT to CSV

``` bash
python process_file.py convert data.txt data.csv
```

2. Extract a Column from CSV

```bash
python process_file.py extract data.csv "Average [mm]" output.csv
```

3. Convert TXT to CSV and Extract a Column

```bash
python process_file.py convert_extract data.txt "Average [mm]" data.csv output.csv
```

## Script Details

The script utilizes the pandas library for data manipulation. The operations are defined in functions, with a main function to handle command-line arguments and invoke the appropriate functionality based on the command.

## Error Handling

the script includes basic error handling for:

- File not found
- Empty files
- Invalid column names

