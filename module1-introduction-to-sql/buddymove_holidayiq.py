import pandas as pd
import  sqlite3

df = pd.read_csv('https://archive.ics.uci.edu/ml/machine-learning-databases/00476/buddymove_holidayiq.csv')
conn = sqlite3.connect('buddymove_holidayiq.sqlite3')
df.to_sql('table', conn, index=False, if_exists='fail')
cur = conn.cursor()

q = """
SELECT COUNT(*) AS Rows
FROM "general"
"""
df1 = pd.read_sql(q, conn)
df1.to_sql('question_1', conn, index=False, if_exists='replace')


q2 = """
SELECT COUNT("User Id") AS "100Nat&100Shop"
FROM "table" t 
WHERE Nature >= 100 AND Shopping >= 100
"""
df2 = pd.read_sql(q2, conn)
df2.to_sql('question_2', conn, index=False, if_exists='replace')


q3 = """
SELECT ROUND(AVG(Sports), 2) AS AverageSports, 
	   ROUND(AVG(Religious), 2) AS AverageReligious, 
	   ROUND(AVG(Nature), 2) AS AverageNature,
	   ROUND(AVG(Theatre), 2) AS AverageTheatre, 
	   ROUND(AVG(Shopping), 2) AS AverageShopping, 
	   ROUND(AVG(Picnic), 2) AS AveragePicnic
FROM "table" t 
"""
df3 = pd.read_sql(q3, conn)
df3.to_sql('question_3', conn, index=False, if_exists='replace')
