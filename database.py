import sqlite3
from sqlite3 import Error

"""  Create database connection to SQLite Database  """
def create_connection(db_file):
    
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        return conn
    except Error as e:
        print(e)
    
    return conn


"""  Create a table in the database  """
def create_table(conn, new_table):
    
    try:
        c = conn.cursor()
        c.execute(new_table)
    except Error as e:
        print(e)


"""  Creates the entire database  """
def create_database(conn):
    
    # create table for sites
    create_sites_table = """ CREATE TABLE IF NOT EXISTS Sites (
                                site_id INTEGER PRIMARY KEY autoincrement,
                                name text NOT NULL,
                                url text NOT NULL,
                                region text NOT NULL
                            ); """
    
    # create table for trainers
    create_trainers_table = """ CREATE TABLE IF NOT EXISTS Trainers (
                                    trainer_id INTEGER PRIMARY KEY autoincrement,
                                    brand TEXT NOT NULL,
                                    name TEXT NOT NULL,
                                    size INTEGER NOT NULL,
                                    price INTEGER NOT NULL,
                                    site_id INTEGER NOT NULL,
                                    FOREIGN KEY(site_id)
                                        REFERENCES Sites(site_id)
                                ); """
    
    # create tables
    if conn is not None:
        create_table(conn, create_sites_table)
        create_table(conn, create_trainers_table)
    else:
        print("Error! Cannot create database connection.")
        


"""  Insert record into site table  """
def create_site(conn, site):
    
    sql = """ INSERT INTO Sites(name, url, region)
                VALUES(?,?,?) """
    
    c = conn.cursor()
    c.execute(sql, site)
    conn.commit()
    
    return c.lastrowid


"""  Insert record into trainers table  """
def create_trainer(conn, trainer):
    
    sql = """ INSERT INTO Trainers(brand, name, size, price, site_id)
                VALUES(?,?,?,?,?)"""
    c = conn.cursor()
    c.execute(sql, trainer)
    conn.commit()


""" Runtime code  """
if __name__ == '__main__':
    database = "database.db"
    conn = sqlite3.connect(database)
    create_database(conn)
    
    site = ('Site Name', 'Site URL', 'Site Region')
    site_id = create_site(conn, site)
    
    trainer = ('Trainer Brand', 'Trainer Name', 'Trainer Size', 'Trainer Price', site_id)
    create_trainer(conn, trainer)
    conn.close()
    
    
    