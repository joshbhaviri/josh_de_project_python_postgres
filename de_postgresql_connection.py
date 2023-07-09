



#import postgresql library 
import psycopg2

#Create a connection to postgresql dB
try:
    conn = psycopg2.connect("host=localhost dbname=testpgde user=postgres password=Mallipadma@92")
except psycopg2.Error as e:
        print("Error: Could not make connection to the Postgres dB")
        print(e)

#Use the connection to get a cursor that can be used to execute queries 
try:
    cur = conn.cursor()
except psycopg2.Error as e:
        print("Error: Could not get  cursor to the dB")
        print(e)

#Set automatic commit to be true so that each action is committed without having to call conn.commit() after each command 
conn.set_session(autocommit=True)

# #Create a database to do the work in 
try:
    cur.execute("create database testpgsql")
except psycopg2.Error as err:
        print(err)

# create table students which has columns 

try:
    cur.execute("CREATE TABLE IF NOT EXISTS students (student_id int, name varchar, age int, gender varchar, marks int, subject varchar)")
except psycopg2.Error as err:
        print("Error: Issue creating table ")
        print(err)




