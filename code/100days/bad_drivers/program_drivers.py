import research_drivers

def main():

    print("Bad Drivers")
    print()
    research_drivers.init()


    print("The highest 5 premiums in Dollars:")
    high_prem = research_drivers.high_premiums()
    for idx, d in enumerate(high_prem[:5],1):
        print(f' {idx}. {d.state} - {d.car_insurance_premiums} ')
    print()


    print("States with the highest % of no previous incidents:")
    npi = research_drivers.high_first_time()
    for idx, d in enumerate(npi[:5],1):
        print(f' {idx}. {d.state} F on {d.fatal_no_previous_accidents}')
    print()


if __name__ == '__main__':
    main()