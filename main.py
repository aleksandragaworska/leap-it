
class InputExeption(Exception):
    pass


def get_input_year():
    print('Type a year to check')
    try:
        year_to_check = int(input())
    except ValueError:
        raise InputExeption('Year must be integer!')

    if year_to_check < 1752:
        raise InputExeption('Before 1752 were not any leap years')

    return year_to_check


def cheack_leap(year):
    may_be_leap = False

    if year % 4 == 0:
        may_be_leap = True
    if year % 100 == 0:
        may_be_leap = False
    if year % 400 == 0:
        may_be_leap = True

    return may_be_leap


if __name__ == '__main__':
    year_to_check = get_input_year()
    is_leap = cheack_leap(year_to_check)
    if is_leap:
        print(f'Year {year_to_check} is leap')
    else:
        print(f'Year {year_to_check} is not leap')
