
import json
import string
import pyodbc

#Коннектимся к бд
conn = pyodbc.connect('Driver={SQL Server};Server=DESKTOP-H0E8CDQ\MSSQLSERVER01;Database=task1;Trusted_Connection=yes;')
conn.timeout = 60    
conn.autocommit = True

#Функция выполнения процедуры из БД
def exProc(num):
     if formNum == 1:
          numOfPr = 'task' + str(num) + 'ProcJSON' 
          with conn.cursor() as cursor:
               f = 'Task' + str(num) + 'JSON.json'
               cursor.execute('EXEC  ? ',numOfPr)
               result = str(cursor.fetchall())
               for row in result:
                    with open(f,'w') as file:
                         json.dump(result,file)
     elif formNum == 2:
          numOfPr = 'task' + str(num) + 'ProcXML' 
          with conn.cursor() as cursor:
               f = 'Task' + str(num) + 'XML.xml'
               cursor.execute('EXEC  ? ',numOfPr)
               result = str(cursor.fetchall())
               for row in result:
                    with open(f,'w') as file:
                         json.dump(result,file)


#Выбираем формат данных и таску
print("Выберите формат данных (1 - JSON, 2 - XML)")
formNum = int(input())

print("Выберите таску для выполнения (1,2,3,4)")
taskNum = int(input())
exProc(taskNum)


conn.close()
print('closed db connection')

