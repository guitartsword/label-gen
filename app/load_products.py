import csv


def get_product_label_text() -> list[str]:
    with open('input.csv') as csvfile:
        reader = csv.reader(csvfile)
        _ = next(reader)  # ignore header row
        return ['\n'.join(row) for row in reader]
