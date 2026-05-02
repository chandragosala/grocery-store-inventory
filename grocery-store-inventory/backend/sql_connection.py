import sqlite3

__cnx = None

def get_sql_connection():
  global __cnx

  if __cnx is None:
    __cnx = sqlite3.connect('grocery_store.db', check_same_thread=False)

  return __cnx

