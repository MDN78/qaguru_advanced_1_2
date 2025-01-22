










# import socket
#
# def test_check_server(ip="http://localhost2", port=8002):
#     # создаем объект socket
#     s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#     try:
#         # подключаемся к серверу
#         s.connect((ip, port))
#         # закрываем соединение
#         s.shutdown(socket.SHUT_RDWR)
#         return True
#     except:
#         return False
#         print("Non exist")
#     finally:
#         s.close()


# import requests
# import csv
# import time
# import urllib3
#
# urllib3.disable_warnings()
#
# SLEEP = 0  # время в секундах между следующими запросами
# url_list = []
# url_statuscodes = []
# url_statuscodes.append(["url", "status_code"])  # установка заголовков выходного файла
#
# def getStatuscode(url):
#     try:
#         r = requests.head(url, verify=False, timeout=5)  # для ускорения делаем запрос заголовка
#         return (r.status_code)
#
#     except:
#         return -1


# проверяемые url во входном файле
# используйте один url в строке
# with open('url_list.csv', newline='') as f:
#     reader = csv.reader(f)
#     for row in reader:
#         url_list.append(row[0])


# проход всего списка url
# for url in url_list:
#     print(url)
#     check = [url, getStatuscode(url)]
#     time.sleep(SLEEP)
#     url_statuscodes.append(check)
#
# # Выходной файл
# with open("url_status.csv", "w", newline="") as f:
#     writer = csv.writer(f)
#     writer.writerows(url_statuscodes)
#
# def test_smoke():
#     gets = getStatuscode("http://localhost:8002/")
#     print(gets)

