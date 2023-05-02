import psycopg2
import datetime


def search_by_date(cursor):
    """function of a request to search data by date in table ev_info"""

    switch = int(input(
        "\n1. Search by only year\n"
        "2. Search by full date (year-month-day)\n"
        "3. Exit\n"
    ))
    match switch:
        case 1:
            while (1):
                era = input('The year you want to enter AD or BC, please, write AD or BC\n')
                if era != 'AD' and era != 'BC' and era != 'ad' and era != 'bc':
                    print("Incorrect input!\n")
                else:
                    break
            date = input('Write the year\n')
            search_q = f"select to_char(ev_date, 'YYYY-MM-DD AD'), description " \
                       f"from ev_info where ev_date between symmetric" \
                       f" '{date.zfill(4)}-01-01 {era}' and '{date.zfill(4)}-12-31 {era}';"
        case 2:
            while (1):
                era = input('The date you want to enter AD or BC, please, write AD or BC\n')
                if era != 'AD' and era != 'BC' and era != 'ad' and era != 'bc':
                    print("Incorrect input!\n")
                else:
                    break
            date = input('Write the date you want in the year-month-date format, for example, 0035-06-09'
                         '(pay attention to the zeros that are added to the year if it consists of less than 4 digits)\n')
            date = datetime.datetime.strptime(date, '%Y-%m-%d')
            date = date.date()
            search_q = f"select to_char(ev_date, 'YYYY-MM-DD AD'), description from ev_info where ev_date = '{date} {era}';"
        case 3:
            return
    print("\nResult of request\n")
    cursor.execute(search_q)
    for tuple in cursor.fetchall():
        print(tuple)
    print("----------------------------------")
    enter = input("\nPress enter to continue, please\n")


def search_by_date_range(cursor):
    """function of a request to search data by date range in table ev_info"""

    switch = int(input(
        "\n1. Search between two years\n"
        "2. Search between two full dates (year-month-day)\n"
        "3. Exit\n"
    ))
    match switch:
        case 1:
            while (1):
                era1 = input('The first year you want to enter AD or BC, please, write AD or BC\n')
                if era1 != 'AD' and era1 != 'BC' and era1 != 'ad' and era1 != 'bc':
                    print("Incorrect input!\n")
                else:
                    break
            date1 = input('Write the first year\n')
            while (1):
                era2 = input('The second year you want to enter AD or BC, please, write AD or BC\n')
                if era2 != 'AD' and era2 != 'BC' and era2 != 'ad' and era2 != 'bc':
                    print("Incorrect input!\n")
                else:
                    break
            date2 = input('Write the second year (it will be included in the range)\n')
            search_q = f"select to_char(ev_date, 'YYYY-MM-DD AD'), description " \
                       f"from ev_info where ev_date between symmetric" \
                       f" '{date1.zfill(4)}-01-01 {era1}' and '{date2.zfill(4)}-12-31 {era2}';"
        case 2:
            while (1):
                era1 = input('The first date you want to enter AD or BC, please, write AD or BC\n')
                if era1 != 'AD' and era1 != 'BC' and era1 != 'ad' and era1 != 'bc':
                    print("Incorrect input!\n")
                else:
                    break
            date1 = input('Write the first date you want in the year-month-date format, for example, 0035-06-09'
                         '(pay attention to the zeros that are added to the year if it consists of less than 4 digits)\n')
            date1 = datetime.datetime.strptime(date1, '%Y-%m-%d')
            date1 = date1.date()
            while (1):
                era2 = input('The second date you want to enter AD or BC, please, write AD or BC\n')
                if era2 != 'AD' and era2 != 'BC' and era2 != 'ad' and era2 != 'bc':
                    print("Incorrect input!\n")
                else:
                    break
            date2 = input('Write the second date you want in the year-month-date format, for example, 0035-06-09'
                         '(pay attention to the zeros that are added to the year if it consists of less than 4 digits)\n')
            date2 = datetime.datetime.strptime(date2, '%Y-%m-%d')
            date2 = date2.date()
            search_q = f"select to_char(ev_date, 'YYYY-MM-DD AD'), description " \
                       f"from ev_info where ev_date between symmetric" \
                       f"'{date1} {era1}' and '{date2} {era2}';"
        case 3:
            return
    print(f"\nResult of request")
    cursor.execute(search_q)
    for tuple in cursor.fetchall():
        print(tuple)
    print("----------------------------------")
    enter = input("\nPress enter to continue, please\n")


def search_by_description(cursor):
    string = input('Write the phrase or keywords that will be searched for\n')
    search_q = f"select to_char(ev_date, 'YYYY-MM-DD AD'), description " \
               f"from ev_info where " \
               f"ts_description @@ plainto_tsquery('{string}');"
    print(f"\nResult of request")
    cursor.execute(search_q)
    for tuple in cursor.fetchall():
        print(tuple)
    print("----------------------------------")
    enter = input("\nPress enter to continue, please\n")


def __main__():
    try:
        connection = psycopg2.connect(
            user="postgres",
            password="22424",
            host="127.0.0.1",
            port="5432",
            database="history_quide"
        )
        connection.autocommit = True
        with connection.cursor() as cursor:
            while (1):
                switch = int(input(
                    "Select case you need, write only its number:\n1. Find the event(s) by date\n"
                    "2. Find the event(s) by date range\n"
                    "3. Find the event(s) by description\n4. Exit\n"))
                match switch:
                    case 1:
                        search_by_date(cursor)
                    case 2:
                        search_by_date_range(cursor)
                    case 3:
                        search_by_description(cursor)
                    case 4:
                        break


    except Exception as _ex:
        print("Error while working with PostgreSQL: ", _ex)
    finally:
        if connection:
            connection.close()
            print("PostgreSQL connection closed")

if __name__ == '__main__':
    __main__()
