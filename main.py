import psycopg2
import datetime


def search_by_date(cursor):
    """function of a request to search data by date in table ev_info"""

    while(1):
        switch = int(input(
            "\n1. Search by only year\n"
            "2. Search by full date (year-month-day)\n"
            "3. Finish the search by date\n"
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
                if len(date) == 1:
                    search_q = f"select to_char(ev_date, 'YYYY-MM-DD'), description " \
                               f"from ev_info where ev_date between symmetric" \
                               f" '000{date}-01-01 {era}' and '000{date}-12-31 {era}';"
                elif len(date)==2:
                    search_q = f"select to_char(ev_date, 'YYYY-MM-DD'), description " \
                               f"from ev_info where ev_date between symmetric" \
                               f" '00{date}-01-01 {era}' and '00{date}-12-31 {era}';"
                elif len(date) == 3:
                    search_q = f"select to_char(ev_date, 'YYYY-MM-DD'), description " \
                               f"from ev_info where ev_date between symmetric" \
                               f" '0{date}-01-01 {era}' and '0{date}-12-31 {era}';"
                elif len(date) == 4:
                    search_q = f"select to_char(ev_date, 'YYYY-MM-DD'), description " \
                               f"from ev_info where ev_date between symmetric" \
                               f" '{date}-01-01 {era}' and '{date}-12-31 {era}';"
            case 2:
                while (1):
                    era = input('The year you want to enter AD or BC, please, write AD or BC\n')
                    if era != 'AD' and era != 'BC' and era != 'ad' and era != 'bc':
                        print("Incorrect input!\n")
                    else:
                        break
                date = input('Write the date you want in the year-month-date format, for example, 0035-06-09'
                             '(pay attention to the zeros that are added to the year if it consists of less than 4 digits)\n')
                date = datetime.datetime.strptime(date, '%Y-%m-%d')
                date = date.date()
                print(f"\nResult of request")
                search_q = f"select to_char(ev_date, 'YYYY-MM-DD'), description from ev_info where ev_date = '{date} {era}';"
            case 3:
                break
        cursor.execute(search_q)
        for tuple in cursor.fetchall():
            print(tuple)
        print("----------------------------------")
        enter = input("\nPress enter to continue, please\n")


def search_by_date_range(cursor):
    """function of a request to search data by date range in table ev_info"""

    while(1):
        switch = int(input(
            "\n1. Search between two years\n"
            "2. Search between two full dates (year-month-day)\n"
            "3. Finish the search by date range\n"
        ))
        match switch:
            case 1:
                while (1):
                    era1 = input('The first year you want to enter AD or BC, please, write AD or BC\n')
                    if era1 != 'AD' and era != 'BC' and era != 'ad' and era != 'bc':
                        print("Incorrect input!\n")
                    else:
                        break
                while (1):
                    era1 = input('The first year you want to enter AD or BC, please, write AD or BC\n')
                    if era1 != 'AD' and era != 'BC' and era != 'ad' and era != 'bc':
                        print("Incorrect input!\n")
                    else:
                        break
                date = input('Write the year\n')
                if len(date) == 1:
                    search_q = f"select * from ev_info where ev_date between symmetric" \
                               f" '000{date}-01-01 {era}' and '000{date}-12-31 {era}';"
                elif len(date)==2:
                    search_q = f"select * from ev_info where ev_date between symmetric" \
                               f" '00{date}-01-01 {era}' and '00{date}-12-31 {era}';"
                elif len(date) == 3:
                    search_q = f"select * from ev_info where ev_date between symmetric" \
                               f" '0{date}-01-01 {era}' and '0{date}-12-31 {era}';"
                elif len(date) == 4:
                    search_q = f"select * from ev_info where ev_date between symmetric" \
                               f" '{date}-01-01 {era}' and '{date}-12-31 {era}';"
            case 2:
                while (1):
                    era = input('The year you want to enter AD or BC, please, write AD or BC\n')
                    if era != 'AD' and era != 'BC' and era != 'ad' and era != 'bc':
                        print("Incorrect input!\n")
                    else:
                        break
                date = input('Write the date you want in the year-month-date format, for example, 0035-06-09'
                             '(pay attention to the zeros that are added to the year if it consists of less than 4 digits)\n')
                date = datetime.datetime.strptime(date, '%Y-%m-%d')
                date = date.date()
                print(f"\nResult of request")
                search_q = f"select * from ev_info where ev_date = '{date} {era}';"
            case 3:
                break
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
                    "3. Find the event(s) by description\n"
                    "4. Insert into table bookings\n5. Update table tickets\n"
                    "6. Update table bookings\n7. Delete from tickets"
                    "\n8. Delete from bookings\n9. Exit\n"))
                match switch:
                    case 1:
                        search_by_date(cursor)
                    case 2:
                        search_by_date_range(cursor)
                    case 3:
                        break
                    case 4:
                        break
                    case 9:
                        break

    except Exception as _ex:
        print("Error while working with PostgreSQL: ", _ex)
    finally:
        if connection:
            connection.close()
            print("PostgreSQL connection closed")

if __name__ == '__main__':
    __main__()
