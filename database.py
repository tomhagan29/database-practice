import sqlite3
from sqlite3 import Error


def create_connection(db_file):
    
    """  Create database connection to SQLite Database  """
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        return conn
    except Error as e:
        print(e)
    
    return conn



def create_table(conn, create_table):
    
    """  Create a table in the database  """
    try:
        c = conn.cursor()
        c.execute(create_table)
    except Error as e:
        print(e)



def main():
    
    database = "database.db"
    
    create_trainers_table = """ CREATE TABLE IF NOT EXISTS trainers (
                                    id integer PRIMARY KEY,
                                    brand text NOT NULL,
                                    name text NOT NULL,
                                    size integer NOT NULL,
                                    price integer NOT NULL,
                                    source text
                                ); """
    
    # Create a database connection
    conn = create_connection(database)
    
    # create tables
    if conn is not None:
        
        # create trainers table
        create_table(conn, create_trainers_table)
        
    else:
        print("Error! Cannot create database connection.")
        

if __name__ == '__main__':
    main()