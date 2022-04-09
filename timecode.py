from datetime import datetime
from calendar import monthrange


def setcode():
    # 현재 시간 설정
    current_time = datetime.now()
    print("{} connect".format(current_time))

    year = current_time.year
    month = current_time.month
    hour = current_time.hour
    day = current_time.day

    # airkroea url에 맞게 조정
    # 1. 00시는 그 전날의 24시로 표기
    # 2. 시간 값: 시간 + 1999
    # 3. tdate 값: 해당 월 초의 날짜 ex) "2021-12-01"

    if current_time.hour == 0:
        hour = 24
        if day == 1:
            day = monthrange(year, current_time.month-1)[1]
        else:
            day = current_time.day - 1

    hour_code = hour + 1999
    date = "{}-{}-{}".format(year, month, day)
    tdate = "{}-{}-01".format(current_time.year, current_time.month)
    monthday = monthrange(current_time.year, current_time.month)[1]

    return {"date": date,
            "hour_code": hour_code,
            "tdate": tdate,
            "monthday": monthday}
