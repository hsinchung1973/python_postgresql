#幫我寫一個副程式連線到資料庫
# This script connects to a PostgreSQL database using psycopg2.
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import psycopg2
import sys
# 資料庫連線設定
import os


def execute_query(connection, query):
    cursor = connection.cursor()
    cursor.execute(query)
    result = cursor.fetchall()
    cursor.close()
    return result

def connect_db():
    """連接到 PostgreSQL 資料庫"""
    conn = psycopg2.connect(
        host='host.docker.internal',
        port='5432',
        dbname='postgres',
        password='respberry',
        user='postgres'
    )
    return conn

def main():
    conn = connect_db()
    try:
        if conn:
            print("成功連接到資料庫！")
            query = """
            SELECT count(*) AS "筆數"
            FROM "台鐵車站資訊";
            """
            result = execute_query(conn, query)
            print("台鐵車站資訊：", result)
            conn.close()
        else:
            print("無法連接到資料庫，請檢查設定。")
            return
    except Exception as e:
        print("連線失敗:", e)
        sys.exit(1)

if __name__ == "__main__":
    main()