import requests
from bs4 import BeautifulSoup
from timecode import setcode


areas = ['서울', '부산', '대구', '인천', '광주', '대전', '울산', '경기',
         '강원', '충북', '충남', '전북', '전남', '세종', '경북', '경남', '제주']
items = ['PM2.5', 'PM10']
area_code = {'서울': '02', '부산': '051', '대구': '053', '인천': '032',
             '광주': '062', '대전': '042', '울산': '052', '경기': '031', '강원': '033',
             '충북': '043', '충남': '041', '전북': '063', '전남': '061', '세종': '044',
             '경북': '054', '경남': '055', '제주': '064'}
item_code = {'PM2.5': '10008', 'PM10': '10007'}
data_name = ["측정소", "평균", "최대", "최소", "1시", "2시", "3시", "4시", "5시", "6시", "7시", "8시", "9시", "10시",
             "11시", "12시", "13시", "14시", "15시", "16시", "17시", "18시", "19시", "20시", "21시", "22시", "23시", "24시"]


def update(area, item):
    codes = setcode()
    date = codes["date"]
    hour_code = codes["hour_code"]
    tdate = codes["tdate"]
    monthday = codes["monthday"]

    # url 고칠 것
    url = "https://www.airkorea.or.kr/web/sidoAirInfo/sidoAirInfoDay01?itemCode={}&ymd={}%{}&areaCode={}&tDate={}&monthDay={}".format(
        item_code[item], date, hour_code, area_code[area], tdate, monthday)
    print(url)


headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
data = requests.get(
    'https://movie.naver.com/movie/sdb/rank/rmovie.naver?sel=pnt&date=20210829', headers=headers)

soup = BeautifulSoup(data.text, 'html.parser')
 # 데이터 추출
 data_rows = soup.find("table", attrs={"class": "st_1 stoke"}).find(
      "tbody").find_all("tr", attrs={"class": "al1"})

  # 반환되는 이중리스트
  tdata = []
   # 데이터 정제
   for row in data_rows:
        columns_name = row.find("th")
        columns = row.find_all("td")
        data = []
        data.append(columns_name.get_text())
        for column in columns:
            # text 정제
            tmp = column.get_text()
            tmp = tmp.replace(' ', "")
            tmp = tmp.replace('\r', "")
            tmp = tmp.replace('\n', "")
            data.append(tmp[:2])

        print(data)
        tdata.append(data)
    # writer.writerow(data)
    # print(tdata)

    return(tdata)
