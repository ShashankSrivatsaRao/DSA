import os
import pypyodbc as odbc

def bulk_insert(data_file,target_table):
    sql= f"""
    BULK INSERT {target_table}
    FROM '{data_file}'
    WITH
    (   FORMAT = 'CSV',         
        FIELDTERMINATOR = ',',
        ROWTERMINATOR = '\\n',
        FIRSTROW = 2
    )
    """.strip()
    return sql

#STEP 1: Connect to SQL Server
SERVICE_NAME=r'DESKTOP-RUEBP2D\SQLEXPRESS'
DATABASE_NAME='PREP'
target_table='Obesity'

conn=odbc.connect(f"""  
    Driver={{SQL Server}};
    Server={SERVICE_NAME};
    Database={DATABASE_NAME};
    Trusted_Connection=yes;
    """.strip())
print(conn)

#Step 2: Iterate through the data files and upload
data_file_folder = os.path.join(os.getcwd(), 'data')
data_files = os.listdir(data_file_folder)

cursor = conn.cursor()
try:
    # here we can use with statement to automatically close connection once the operation is complete
    with cursor:
        for data_file in data_files:
            if data_file.endswith('.csv'):
                cursor.execute(bulk_insert(os.path.join(data_file_folder, data_file), target_table))
                print(os.path.join(data_file_folder, data_file), target_table + ' inserted')
        cursor.commit()
except Exception as e:
    print(e)
    conn.rollback()
    print('Transaction rollback')