"""
A script to calculate most of everything we need for calculating internet speeds, comparing price per GB and so on.
"""
import csv


class InternetSpeed:



    def __init__(self, datafile: str):
        self.FORMAT_EXAMPLE = "isp,plan_name,price,speed,speed_after_fua,allowance"
        self.datafile = datafile
        self.validate_datafile()

    def validate_datafile(self):
        if not self.datafile.endswith("csv"):
            raise ValueError("Should be a csv file")

        columns_in_order = ["isp", "plan_name", "price", "speed", "speed_after_fua", "allowance"]
        with open(self.datafile, newline='') as csvfile:
            datafilereader = csv.reader(csvfile, delimiter=',')
            for row in datafilereader:
                if datafilereader.line_num == 1:
                    if row != columns_in_order:
                        print("Please keep the csv files header in the following format")
                        print(self.FORMAT_EXAMPLE)
                        raise ValueError("Header does not follow the required order")
                else:
                    # make sure everything except plan_names can be converted to floats
                    for i in range(2, 4):
                        temp_var = float(row[i])  # value error will be auto raised here when conversion fails

                    self.process_file()

    @staticmethod
    def calculate_all(price: float, speed: float, speed_after_fua: float, allowance: float) -> tuple[
        float, float, float, float, float, float, float, float, float, float, float, float, float]:
        """
        The calculation of all the fields for the result file
        """
        SECONDS_IN_A_MONTH = 2592000

        # recalculate price for GST 8%
        price = price + price * 0.08

        # definitions
        kbps = speed / 0.008
        kbps_after_fua = speed_after_fua / 0.008
        time_for_gig = ((1 * 1000) * 1000) / kbps
        time_for_gig_after_fua = ((1 * 1000) * 1000) / kbps_after_fua
        time_to_deplete_fua = time_for_gig * allowance
        time_left_after_fua = SECONDS_IN_A_MONTH - time_to_deplete_fua
        possible_gb_after_fua = time_left_after_fua / time_for_gig_after_fua
        possible_gb_total = possible_gb_after_fua + allowance
        price_per_gig = possible_gb_total / price

        # round off to two decimals
        price = round(price, 2)
        kbps = round(kbps, 2)
        kbps_after_fua = round(kbps_after_fua, 2)
        time_for_gig = round(time_for_gig, 2)
        time_for_gig_after_fua = round(time_for_gig_after_fua, 2)
        time_to_deplete_fua = round(time_to_deplete_fua, 2)
        time_left_after_fua = round(time_left_after_fua, 2)
        possible_gb_after_fua = round(possible_gb_after_fua, 2)
        possible_gb_total = round(possible_gb_total, 2)
        price_per_gig = round(price_per_gig, 2)
        return (price, speed, speed_after_fua, allowance, kbps, kbps_after_fua, time_for_gig, time_for_gig_after_fua,
                time_to_deplete_fua, time_left_after_fua, possible_gb_after_fua, possible_gb_total, price_per_gig)

    @staticmethod
    def read_from_data(row):
        isp, plan_name, price, speed, speed_after_fua, allowance = row[0], row[1], float(row[2]), float(
            row[3]), float(row[4]), float(row[5])
        return isp, plan_name, price, speed, speed_after_fua, allowance

    def process_file(self):
        with open(self.datafile, newline='') as csvfile:
            datafilereader = csv.reader(csvfile, delimiter=',')
            datafilereader.__next__()  # skip header
            with open('result.csv', 'w', encoding='utf-8') as result_file:
                with open('result_simple.csv', 'w', encoding='utf-8') as result_simple_file:
                    with open('max_gb.csv', 'w', encoding='utf-8') as max_gb_file:
                        with open('max_value.csv', 'w', encoding='utf-8') as max_value:
                            result_file.write(
                                "ISP, PLAN,PRICE (INC. 8% GST),NORMAL SPEED,SPEED AFTER FUA,FUA (GB),KBPS ,KBPS POST FUA ,TTD 1GB,"
                                "TTD 1GB POST FUA,TIME TO DEPLETE FUA,TIME LEFT AFTER FUA,"
                                "POSSIBLE GB POST FUA,TOTAL POSSIBLE GB,PRICE / GB" + "\n"
                            )
                            result_simple_file.write(
                                "ISP, PLAN,PRICE (INC. 8% GST),NORMAL SPEED,SPEED AFTER FUA,FUA (GB),TTD 1GB,"
                                "TTD 1GB POST FUA,TIME TO DEPLETE FUA,"
                                "TOTAL POSSIBLE GB,PRICE / GB" + "\n"
                            )
                            max_gb_file.write(
                                "ISP, PLAN,PRICE (INC. 8% GST),TOTAL POSSIBLE GB" + "\n"
                            )
                            max_value.write(
                                "ISP, PLAN,PRICE (INC. 8% GST),TOTAL POSSIBLE GB,PRICE / GB" + "\n"
                            )

                            for row in datafilereader:
                                isp, plan_name, price, speed, speed_after_fua, allowance = self.read_from_data(row)

                                # yikes...
                                (price, speed, speed_after_fua, allowance,
                                 kbps, kbps_after_fua, time_for_gig,
                                 time_for_gig_after_fua, time_to_deplete_fua, time_left_after_fua,
                                 possible_gb_after_fua, possible_gb_total,
                                 price_per_gig) = self.calculate_all(price, speed, speed_after_fua, allowance)

                                # result.csv
                                result_file.write(
                                    f"{isp},{plan_name},{price},{speed},{speed_after_fua},"
                                    f"{allowance},{kbps},{kbps_after_fua},{time_for_gig},"
                                    f"{time_for_gig_after_fua},{time_to_deplete_fua},"
                                    f"{time_left_after_fua},{possible_gb_after_fua},"
                                    f"{possible_gb_total},{price_per_gig}" + "\n"
                                )

                                # result_simple.csv
                                result_simple_file.write(
                                    f"{isp},{plan_name},{price},{speed},{speed_after_fua},"
                                    f"{allowance},{time_for_gig},"
                                    f"{time_for_gig_after_fua},{time_to_deplete_fua},"
                                    f"{possible_gb_total},{price_per_gig}" + "\n"
                                )

                                # gb
                                max_gb_file.write(
                                    f"{isp},{plan_name},{price},"
                                    f"{possible_gb_total}" + "\n"
                                )

                                # value
                                max_value.write(
                                    f"{isp},{plan_name},{price},"
                                    f"{possible_gb_total},{price_per_gig}" + "\n"
                                )


if __name__ == "__main__":
    ifile = InternetSpeed("data.csv")
