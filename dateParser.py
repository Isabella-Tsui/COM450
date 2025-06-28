import csv
from datetime import datetime


def parse_date(date_str):
    if not date_str or date_str.strip() == "":
        return ""  # Keep empty cells empty
    formats = ["%Y-%m-%d", "%m/%d/%y"]
    for fmt in formats:
        try:
            parsed_date = datetime.strptime(date_str.strip(), fmt)
            return parsed_date.strftime("%Y-%m-%d")
        except ValueError:
            continue
    return ""  


def standardize_release_dates(input_file, output_file):
    with open(input_file, mode='r', newline='', encoding='utf-8') as infile, \
            open(output_file, mode='w', newline='', encoding='utf-8') as outfile:

        reader = csv.DictReader(infile)
        fieldnames = reader.fieldnames
        writer = csv.DictWriter(outfile, fieldnames=fieldnames)
        writer.writeheader()

        for row in reader:
            if 'Release Date' in row:
                row['Release Date'] = parse_date(row['Release Date'])
            writer.writerow(row)


standardize_release_dates("chip_dataset_og.csv", "output.csv")
