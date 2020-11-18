import sqlite3
import pandas as pd

conn = sqlite3.connect('rpg_db.sqlite3')

cur = conn.cursor()

# How many total Characters are there?
query1 = """
SELECT COUNT(character_id) 
FROM charactercreator_character cc 
"""
cur.execute(query1)
result_list = cur.fetchall()
cols = [ii[0] for ii in cur.description]
df1 =  pd.DataFrame(result_list, columns=cols)

my_conn1 = sqlite3.connect("my_db1.sqlite")
df1.to_sql('my_table1', my_conn1, index=False, if_exists='replace')

# How many of each specific subclass?
query2 = """
SELECT COUNT(DISTINCT cf.character_ptr_id) AS TotalFighter, 
	   COUNT(DISTINCT cc.character_ptr_id) AS TotalCleric,
	   COUNT(DISTINCT cm.character_ptr_id) AS TotalMage,
	   COUNT(DISTINCT cn.mage_ptr_id) AS TotalNecromancer,
	   COUNT(DISTINCT ct.character_ptr_id) AS TotalThief
FROM charactercreator_fighter cf, charactercreator_cleric cc,
     charactercreator_mage cm, charactercreator_necromancer cn,
     charactercreator_thief ct
"""
df2 = pd.read_sql(query2, conn)
my_conn2 = sqlite3.connect("my_db2.sqlite")
df2.to_sql('my_table2', my_conn2, index=False, if_exists='replace')

# How many total Items?
query3 = """
SELECT COUNT(item_id) AS ItemTotal 
FROM armory_item ai 
"""

df3 = pd.read_sql(quer3, conn)
my_conn3 = sqlite3.connect("my_db3.sqlite")
df3.to_sql('my_table3', my_conn3, index=False, if_exists='replace')

# How many of the Items are weapons? How many are not?
query4 = """
SELECT COUNT(DISTINCT aw.item_ptr_id) AS TotalWeapons,
	   COUNT(DISTINCT ai.item_id) - COUNT(DISTINCT aw.item_ptr_id) AS TotalNotWeapons
FROM armory_item ai, armory_weapon aw  
"""

df4 =  pd.read_sql(quer4, conn)
my_conn4 = sqlite3.connect("my_db4.sqlite")
df4.to_sql('my_table', my_conn4, index=False, if_exists='replace')

# How many Items does each character have? (Return first 20 rows)
query5 = """
SELECT character_id, COUNT(item_id) AS ItemsTotal 
FROM charactercreator_character_inventory cci 
GROUP BY character_id 
LIMIT 20 
"""

df5 = pd.read_sql(quer5, conn)
my_conn5 = sqlite3.connect("my_db5.sqlite")
df5.to_sql('my_table5', my_conn5, index=False, if_exists='replace')

# How many Weapons does each character have? (Return first 20 rows)
query6 = """
SELECT cci.character_id, COUNT(aw.item_ptr_id) AS Weapons
FROM charactercreator_character_inventory cci
LEFT JOIN armory_weapon aw
	ON cci.item_id = aw.item_ptr_id 
GROUP BY cci.character_id 
LIMIT 20 
"""

df6 = pd.read_sql(quer6, conn)
my_conn6 = sqlite3.connect("my_db6.sqlite")
df6.to_sql('my_table6', my_conn6, index=False, if_exists='replace')

# On average, how many Items does each Character have?
query7 = """
SELECT AVG(ItemsTotal) AS Average
FROM (
	SELECT COUNT(item_id) AS ItemsTotal
	FROM charactercreator_character_inventory cci 
	GROUP BY character_id
    )
"""

df7 = pd.read_sql(quer7, conn)
my_conn7 = sqlite3.connect("my_db7.sqlite")
df7.to_sql('my_table7', my_conn7, index=False, if_exists='replace')

# On average, how many Weapons does each character have?
query8 = """
SELECT AVG(Weapons)
FROM (
	SELECT COUNT(aw.item_ptr_id) AS Weapons
	FROM charactercreator_character_inventory cci
	LEFT JOIN armory_weapon aw
		ON cci.item_id = aw.item_ptr_id 
	GROUP BY cci.character_id
"""

df8 = pd.read_sql(quer8, conn)
my_conn8 = sqlite3.connect("my_db8.sqlite")
df8.to_sql('my_table8', my_conn8, index=False, if_exists='replace')
