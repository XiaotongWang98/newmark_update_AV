import pandas as pd
import sys

def convert_to_csv(txt_file, csv_file):
    try:
        df = pd.read_csv(txt_file, delimiter='\t')
        df.to_csv(csv_file, index=False)
        print(f"File converted successfully and saved as {csv_file}")
    except FileNotFoundError:
        print(f"The file '{txt_file}' was not found.")
    except pd.errors.EmptyDataError:
        print(f"The file '{txt_file}' is empty.")
    except Exception as e:
        print(f"An error occurred: {e}")

def extract_column(file_name, column_name, output_file=None):
    try:
        df = pd.read_csv(file_name)
        if column_name in df.columns:
            column_data = df[[column_name]]  # 双重括号表示保留DataFrame格式
            if output_file:
                column_data.to_csv(output_file, index=False)  # 保存时不包含行号
                print(f"Column '{column_name}' saved to {output_file}")
            else:
                print(column_data.to_string(index=False))
        else:
            print(f"Column '{column_name}' does not exist in the file.")
    except FileNotFoundError:
        print(f"The file '{file_name}' was not found.")
    except pd.errors.EmptyDataError:
        print(f"The file '{file_name}' is empty.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python process_file.py <command> [options]")
        print("Commands:")
        print("  convert <input_txt_file> <output_csv_file>       Convert TXT to CSV")
        print("  extract <input_file> <column_name> [output_file] Extract a column from CSV")
        print("  convert_extract <input_txt_file> <column_name> <output_csv_file> [output_file] Convert TXT to CSV and extract a column")
    else:
        command = sys.argv[1]

        if command == "convert":
            if len(sys.argv) != 4:
                print("Usage: python process_file.py convert <input_txt_file> <output_csv_file>")
            else:
                input_file = sys.argv[2]
                output_csv = sys.argv[3]
                convert_to_csv(input_file, output_csv)

        elif command == "extract":
            if len(sys.argv) < 4 or len(sys.argv) > 5:
                print("Usage: python process_file.py extract <input_file> <column_name> [output_file]")
            else:
                input_file = sys.argv[2]
                column_name = sys.argv[3]
                output_file = sys.argv[4] if len(sys.argv) == 5 else None
                extract_column(input_file, column_name, output_file)

        elif command == "convert_extract":
            if len(sys.argv) < 5 or len(sys.argv) > 6:
                print("Usage: python process_file.py convert_extract <input_txt_file> <column_name> <output_csv_file> [output_file]")
            else:
                input_file = sys.argv[2]
                column_name = sys.argv[3]
                output_csv = sys.argv[4]
                output_file = sys.argv[5] if len(sys.argv) == 6 else None
                convert_to_csv(input_file, output_csv)
                extract_column(output_csv, column_name, output_file)

        else:
            print(f"Unknown command: {command}")
            print("Usage: python process_file.py <command> [options]")
            print("Commands:")
            print("  convert <input_txt_file> <output_csv_file>       Convert TXT to CSV")
            print("  extract <input_file> <column_name> [output_file] Extract a column from CSV")
            print("  convert_extract <input_txt_file> <column_name> <output_csv_file> [output_file] Convert TXT to CSV and extract a column")
