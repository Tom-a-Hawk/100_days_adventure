import os
import csv
import collections

data = []

Record = collections.namedtuple('Record', 'state, fatal_collision_per_billion_miles, perc_fatal_were_speeding,'
                      'perc_fatal_alchol, fatal_not_distracted, fatal_no_previous_accidents,'
                      'car_insurance_premiums, insurance_company_losses')


def init():
    '''Load the data file into memory'''
    base_folder = os.path.dirname(__file__)
    filename = os.path.join(base_folder, 'bad-drivers.csv')

    with open(filename, 'r', encoding='utf-8') as fin:

        fieldnames = ['state', 'fatal_collision_per_billion_miles', 'perc_fatal_were_speeding',
                      'perc_fatal_alchol', 'fatal_not_distracted', 'fatal_no_previous_accidents',
                      'car_insurance_premiums', 'insurance_company_losses']


        writer = csv.DictReader(fin, fieldnames=fieldnames)

        next(fin,None)
        data.clear()

        for row in writer:
            record = parse_row(row)
            data.append(record)

def parse_row(row):
    row['fatal_collision_per_billion_miles'] = float(row['fatal_collision_per_billion_miles'])
    row['perc_fatal_were_speeding'] = int(row['perc_fatal_were_speeding'])
    row['perc_fatal_alchol'] = int(row['perc_fatal_alchol'])
    row['fatal_not_distracted'] = int(row['fatal_not_distracted'])
    row['fatal_no_previous_accidents'] = int(row['fatal_no_previous_accidents'])
    row['car_insurance_premiums'] = float(row['car_insurance_premiums'])
    row['insurance_company_losses'] = float(row['insurance_company_losses'])


    record = Record(
        **row
    )

    return record

def high_premiums():
    return sorted(data, key=lambda r: r.car_insurance_premiums, reverse=True)

def high_first_time():
    return sorted(data, key=lambda r:r.fatal_no_previous_accidents, reverse=True)
