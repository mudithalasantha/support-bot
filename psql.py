#!/usr/bin/python
import psycopg2
import user
import movie_tickets
import ast
import json
import urllib, json
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
    sql = "insert into users (id,gender,mobile,age,first_name,last_name,nic,stage) VALUES("+str(user.id)+",'"+str(user.gender)+"','"+str(user.mobile)+"',"+str(user.age)+",'"+str(user.first_name).replace("'", "")+"','"+str(user.last_name).replace("'", "")+"','"+str(user.nic)+"','"+str(user.stage)+"')"
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
        cur.execute("select id,gender,mobile,age,first_name,last_name,nic,stage,last_edit FROM users where id = "+str(id))
        print("The number of users: ", cur.rowcount)
        row = cur.fetchone()
        print(row)
        Muser.id = row[0]
        Muser.gender = row[1]
        Muser.mobile = row[2]
        Muser.age = row[3]
        Muser.first_name = row[4]
        Muser.last_name = row[5]
        Muser.nic = row[6]
        Muser.stage = row[7]
        Muser.last_edit = row[8]
        
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
        cur.execute("update users set gender = '"+str(user.gender)+"',mobile = '"+str(user.mobile)+"',age = "+str(user.age)+" ,first_name = '"+str(user.first_name).replace("'", "")+"',last_name = '"+str(user.last_name).replace("'", "")+"',nic = '"+str(user.nic).replace("'", "")+"',stage = '"+str(user.stage).replace("'", "")+"',last_edit = now()  where id = "+str(id))
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

def insert_purchase_movie_tickets(myMovie):
    """ insert a new user into the vendors table """
    sql = "insert into purchase_movie_tickets (fbid,movie,theater,date,time,status) VALUES("+str(myMovie.fbid)+",'"+str(myMovie.movie)+"','"+str(myMovie.theater)+"','"+str(myMovie.date)+"','"+str(myMovie.time)+"','"+str(myMovie.status)+"')"
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
        print("sql insert_purchase_movie_tickets error : " + str(error))
    finally:
        if conn is not None:
            conn.close()


def is_purchase_movie_tickets_available(id):
    """ query data from the purchase_movie_tickets table """
    conn = None
    row_count = 0
    try:
        params = config()
        conn = psycopg2.connect(**params)
        cur = conn.cursor()
        cur.execute("select movie,theater,date,time FROM purchase_movie_tickets where fbid = "+str(id) + " and status != 'Completed'")
        print("The number of mymovie: ", cur.rowcount)
        row_count = cur.rowcount
        row = cur.fetchone()
        print(row)
        
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print("sql is_purchase_movie_tickets_available error : " + str(error))
    finally:
        if conn is not None:
            conn.close()
    return row_count

def get_purchase_movie_tickets(id):
    """ query data from the purchase_movie_tickets table """
    conn = None
    Mmovie = movie_tickets.MyMovie()
    try:
        params = config()
        conn = psycopg2.connect(**params)
        cur = conn.cursor()
        cur.execute("select fbid,movie,theater,date,time,status,id,last_edit FROM users where fbid = "+str(id) + " and status != 'Completed'")
        print("The number of users: ", cur.rowcount)
        row = cur.fetchone()
        print(row)
        Mmovie.fbid = row[0]
        Mmovie.movie = row[1]
        Mmovie.theater = row[2]
        Mmovie.date = row[3]
        Mmovie.time = row[4]
        Mmovie.status = row[5]
        Mmovie.id = row[6]
        Mmovie.last_edit = row[7]
        
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print("sql get_purchase_movie_tickets error : " + str(error))
    finally:
        if conn is not None:
            conn.close()
    return Mmovie

def update_purchase_movie_tickets(id, Mmovie):
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
        cur.execute("update purchase_movie_tickets set fbid = '"+str(Mmovie.fbid)+"',movie = '"+str(Mmovie.movie)+"',theater = '"+str(Mmovie.theater)+"' ,date = '"+str(Mmovie.date)+"',time = '"+str(Mmovie.time)+"',status = '"+str(Mmovie.status)+"',last_edit = now()  where id = "+str(id))
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