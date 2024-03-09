"""
A script to calculate most of everything we need for calculating internet speeds, comparing price per GB and so on.
"""
import csv

class InternetSpeed:
    def __init__(self, datafile: str):
        self.datafile = datafile
        self.validate_datafile()

    def validate_datafile(self):
        if not self.datafile.endswith("csv"):
            raise ValueError("Should be a csv file")

        columns_in_order = ["plan_name", "price", "speed", "speed_after_fua", "allowance"]
        with open(self.datafile, newline='') as csvfile:
            datafilereader = csv.reader(csvfile, delimiter=',')
            for row in datafilereader:
                if datafilereader.line_num == 1:
                    if row == columns_in_order:
                        print("Columns are in the correct order")

                print(row)


if __name__ == "__main__":
    ifile = InternetSpeed("data.csv")
