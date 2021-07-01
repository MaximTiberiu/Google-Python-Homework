from datetime import datetime
todays_date = datetime.now()

CNP = input("Introduceti CNP-ul pentru validare: ")
default_CNP = [int(i) for i in str(279146358279)]


def validate_year(cnp_list):
    if cnp_list[0] in [1, 2]:
        year = 1900 + cnp_list[1] * 10 + cnp_list[2]
        if year not in range(1900, 2000):
            print(year)
            print("Prima cifra nu corespunde cu anul nasterii!")
            return False
    elif cnp_list[0] in [5, 6]:
        year = 2000 + cnp_list[1] * 10 + cnp_list[2]
        if year not in range(2000, todays_date.year + 1):
            print(year)
            print("Prima cifra nu corespunde cu anul nasterii!")
            return False
    return True


def validate_month(month):
    if month not in range(1, 13):
        print("Luna invalida!")
        return False
    return True


def validate_day(day, month):
    if day not in range(1, 32):
        print("Zi invalida!")
        return False

    if month == 2 and day not in range(1, 30):
        print("Zi invalida!")
        return False
    return True


def validate_county(county):
    if county not in range(1, 53):
        print("Judet invalid!")
        return False

    if county in range(47, 51):
        print("Judet invalid!")
        return False
    return True


def validate_control(control, cnp_list):
    sum_cnp = 0
    for i in range(0, 12):
        sum_cnp += cnp_list[i] * default_CNP[i]

    if sum_cnp % 11 == 10 and control != 1:
        print("Cifra de control eronata!")
        return False

    if sum_cnp % 11 != control:
        print("Cifra de control eronata!")
        return False
    return True


def validate_cnp(cnp):
    cnp_list = [int(i) for i in str(cnp)]
    if len(cnp_list) != 13:
        print("Lungime CNP eronata!")
        return False

    month = cnp_list[3] * 10 + cnp_list[4]
    day = cnp_list[5] * 10 + cnp_list[6]
    county = cnp_list[7] * 10 + cnp_list[8]
    control = cnp_list[-1]

    if cnp_list[0] not in [0, 1, 5, 6]:
        return False

    return validate_year(cnp_list) and validate_month(month) and validate_day(day, month) and validate_county(county) and validate_control(control, cnp_list)


if validate_cnp(CNP):
    print("CNP-ul introdus este valid!")
else:
    print("CNP-ul introdus nu este valid!")
