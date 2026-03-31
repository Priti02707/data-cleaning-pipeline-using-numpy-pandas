data = """EmployeeID,Name,Age,Department,Salary,JoiningDate,PerformanceScore
101,  Amit Sharma ,25,IT,50000,2020-01-15,4.5
102,Riya Verma,28,HR,45000,2019-03-10,4.0
103,rahul singh,,Finance,55000,2021-07-23,3.8
104,Neha Gupta,32,IT,not_available,2018-11-01,4.2
105,Amit Sharma ,25,IT,50000,2020-01-15,4.5
106,Pooja Mehta,29,hr,48000,2020/05/12,4.1
107, ,30,Finance,60000,2017-09-30,3.5
108,Karan Malhotra,27,IT,,2022-02-20,4.7
109,Sneha Kapoor,twenty six,Marketing,52000,2019-06-18,4.0
110,Arjun Rao,31,IT,58000,2018-04-25,
111,Meena Iyer,45,Finance,72000,2016-12-01,4.8
112,Rohit Das,38,IT,61000,2015-08-19,3.9
113,Anjali Singh,NaN,HR,47000,2019-13-01,4.1
114,Vikram Patel,29,Marketing,53000,2020-10-10,excellent
115,  Kunal Shah,34,IT,59000,2018-07-07,4.3
116,Simran Kaur,27,finance,51000,2021-04-31,3.7
117,Aditya Roy,26,IT,50000,,4.0
118,,33,HR,46000,2017-02-15,3.6
119,Nisha Jain,28,Marketing,not_available,2019-09-09,4.2
120,Deepak Yadav,30,IT,57000,2018-03-21,4.4
"""

with open("employee_data.csv", "w", encoding="utf-8") as file:
    file.write(data)

print("employee_data.csv file successfully created!")
