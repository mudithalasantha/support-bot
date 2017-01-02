#!/usr/bin/python
import psycopg2
import user
import ast
import json
import urllib, json
import infermedica_api
import diagnose
from config import config

def connect():
    """ Connect to the PostgreSQL database server """
    conn = None
    try:
        # read connection parameters
        params = config()
        
        # connect to the PostgreSQL server
        print('Connecting to the PostgreSQL database...')
        conn = psycopg2.connect(**params)
        
        # create a cursor
        cur = conn.cursor()
        
        # execute a statement
        print('PostgreSQL database version:')
        cur.execute('SELECT version()')
        
        # display the PostgreSQL database server version
        db_version = cur.fetchone()
        print(db_version)
        
        # close the communication with the PostgreSQL
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print("sql connect error : " + str(error))
    finally:
        if conn is not None:
            conn.close()
            print('Database connection closed.')


if __name__ == '__main__':
    connect()

def insert_user(user):
    """ insert a new user into the vendors table """
    sql = "insert into users (id,gender,age,first_name,last_name,nic,stage) VALUES("+str(user.id)+",'"+str(user.gender)+"',"+str(user.age)+",'"+str(user.first_name).replace("'", "")+"','"+str(user.last_name).replace("'", "")+"','"+str(user.nic)+"','"+str(user.stage)+"')"
    conn = None
    try:
        # read database configuration
        params = config()
        # connect to the PostgreSQL database
        conn = psycopg2.connect(**params)
        # create a new cursor
        cur = conn.cursor()
        # execute the INSERT statement
        cur.execute(sql)
        # commit the changes to the database
        conn.commit()
        # close communication with the database
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print("sql insert_user error : " + str(error))
    finally:
        if conn is not None:
            conn.close()


def get_user(id):
    """ query data from the users table """
    conn = None
    Muser = user.MyUser()
    try:
        params = config()
        conn = psycopg2.connect(**params)
        cur = conn.cursor()
        cur.execute("select id,gender,age,first_name,last_name,nic,stage,last_edit FROM users where id = "+str(id))
        print("The number of users: ", cur.rowcount)
        row = cur.fetchone()
        print(row)
        Muser.id = row[0]
        Muser.gender = row[1]
        Muser.age = row[2]
        Muser.first_name = row[3]
        Muser.last_name = row[4]
        Muser.nic = row[5]
        Muser.stage = row[6]
        Muser.last_edit = row[7]
        
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print("sql get_user error : " + str(error))
    finally:
        if conn is not None:
            conn.close()
    return Muser

def is_user_available(id):
    """ query data from the users table """
    conn = None
    row_count = 0
    try:
        params = config()
        conn = psycopg2.connect(**params)
        cur = conn.cursor()
        cur.execute("select id,first_name,last_name FROM users where id = "+str(id))
        print("The number of users: ", cur.rowcount)
        row_count = cur.rowcount
        row = cur.fetchone()
        print(row)
        
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print("sql is_user_available error : " + str(error))
    finally:
        if conn is not None:
            conn.close()
    return row_count


def update_user(id, user):
    """ update user based on the id """
    conn = None
    updated_rows = 0
    try:
        # read database configuration
        params = config()
        # connect to the PostgreSQL database
        conn = psycopg2.connect(**params)
        # create a new cursor
        cur = conn.cursor()
        # execute the UPDATE  statement
        cur.execute("update users set gender = '"+str(user.gender)+"',age = "+str(user.age)+" ,first_name = '"+str(user.first_name).replace("'", "")+"',last_name = '"+str(user.last_name).replace("'", "")+"',nic = '"+str(user.nic).replace("'", "")+"',stage = '"+str(user.stage).replace("'", "")+"',last_edit = now()  where id = "+str(id))
        # get the number of updated rows
        updated_rows = cur.rowcount
        # Commit the changes to the database
        conn.commit()
        # Close communication with the PostgreSQL database
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print("sql update_user error : " + str(error))
    finally:
        if conn is not None:
            conn.close()

    return updated_rows
