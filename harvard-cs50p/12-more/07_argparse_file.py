import argparse

parser = argparse.ArgumentParser(
    description="Process a CSV file"
)

parser.add_argument("filename", help="CSV file to process")
parser.add_argument("--output", default="result.csv")

args = parser.parse_args()

print(f"Processing {args.filename}")
print(f"Saving results to {args.output}")

#run file as - python3 harvard-cs50p/12-more/07_argparse_file.py employees.csv --output report.csv