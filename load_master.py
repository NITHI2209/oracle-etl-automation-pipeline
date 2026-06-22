import pandas as pd 
import oracledb 

df = pd.read_excel("master.xlsx")
print(df)

conn = oracledb.connect(
    user = "sys",
    password = "********",
    dsn = "localhost:1521/XEPDB1",
    mode = oracledb.AUTH_MODE_SYSDBA
)

print("Connected to oracle successfully!")

cursor = conn.cursor()
print("cursor created successfully!")

cursor.execute("SELECT COUNT(*) FROM MASTER_TABLE ")
count = cursor.fetchone()
print("Records in MASTER_TABLE:", count[0])

for index, row in df.iterrows():
    cursor.execute(
        """
        INSERT INTO MASTER_TABLE
        (
            ACCOUNT_ID,
            NAME,
            BALANCE,
            TRANSACTION_TYPE,
            TRANSACTION_DATE,
            SOURCE,
            REMARKS
        )
        VALUES
        (:1,:2,:3,:4,:5,:6,:7)
        """,
        (
            row["account_id"],
            row["name"],
            row["balance"],
            row["transaction_type"],
            row["transaction_date"],
            row["source"],
            row["remarks"]
        )
    )

conn.commit()

print("Data inserted successfully!")
