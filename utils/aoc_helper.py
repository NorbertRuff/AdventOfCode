from aocd import get_data

session_id = "" # "your session id
def get_dayly_data(day):
    data = get_data(session=session_id, day=day, year=2023)

    print(data)
    return data
