

# with open("C:/Users/User/PycharmProjects/PythonProject/PythonProject/PythonProject/PythonProject/day_25_fixed/weather_data.csv") as file:
#     content=file.readlines()
#
#     print(content[0])
#

# import csv
#
# with open("C:/Users/User/PycharmProjects/PythonProject/PythonProject/PythonProject/PythonProject/day_25_fixed/weather_data.csv") as file:
#     data =csv.reader(file)
#     tempertures = []
#     flag = 0
#
#     for i in data:
#         if flag == 0:
#             flag = 1
#             continue
#
#
#         # print(i)
#         current_temp = int(i[1])
#
#         tempertures.append(current_temp)
#
#     print(tempertures)
#     print(data)

    # tempertures.append()


import pandas


# data = pandas.read_csv("weather_data.csv")
# print(type(data))
# print(type(data["temp"]))
# data_dict = data.to_dict()
# print(data_dict)
#
# temp_list = data["temp"].to_list()
#
#
#
# print(len(temp_list))
# print(temp_list)
#
# temp_sum=sum(temp_list)
# avg_temp=temp_sum/len(temp_list)
# print(avg_temp)
#
#
#
# temp_max =(data["temp"].max())
#
# print(data[data.temp == temp_max])
#
# monday =data[data.day == "Monday"]
# print(monday.condition)
#
#
# monday.temp(monday.temp *1.8 +32)
#
#


data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")




fur_table_count =data["Primary Fur Color"].value_counts()

fur_table_count.to_csv("fur_count")