
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

               #Задаём имя для будущего json файла с нумерацией
               f = 'Task' + str(num) + 'JSON.json'

               cursor.execute('EXEC  ? ',numOfPr)
               result = str(cursor.fetchall())
               with open(f,'w') as file:
                    json.dump(result,file)
     elif formNum == 2:
          numOfPr = 'task' + str(num) + 'ProcXML' 
          with conn.cursor() as cursor:

               #Задаём имя для будущего xml файла
               f = 'Task' + str(num) + 'XML.xml'
               
               cursor.execute('EXEC  ? ',numOfPr)
               result = str(cursor.fetchall())
               with open(f,'w') as file:
                    json.dump(result,file)



#Записываем данные из json в БД
print("Введите путь к файлу rooms")
rrr = input()
#"C:\\Users\\Dora Ritchik\\Desktop\\rooms.json"
with open(rrr,"r",encoding='utf-8') as read_file:
     data = json.load(read_file)
     json_string = json.dumps(data)    
try:        
        cursor = conn.cursor()
        cursor.execute('EXEC insertRooms @json = ?', json_string)
        print('inserted data')    

except pyodbc.Error as err:
        print('Error !!!!! %s' % err)
except:
        print('something else failed miserably')


#Записываем данные из json в БД
print("Введите путь к файлу students")
rrr = input()
#"C:\\Users\\Dora Ritchik\\Desktop\\students.json"
with open(rrr,"r",encoding='utf-8') as read_file:
     data = json.load(read_file)
json_string = json.dumps(data) 

try:        
        cursor = conn.cursor()
        cursor.execute('EXEC insertStudents @json = ?', json_string)
        print('inserted data')    

except pyodbc.Error as err:
        print('Error !!!!! %s' % err)
except:
        print('something else failed miserably')





#Выбираем формат данных и таску
print("Выберите формат данных (1 - JSON, 2 - XML)")
formNum = int(input())

print("Выберите таску для выполнения (1,2,3,4)")
taskNum = int(input())
exProc(taskNum)

#Закрываем соединение
conn.close()
print('closed db connection')

