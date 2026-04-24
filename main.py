# CodeGrade step0

# Run this cell without changes

import pandas as pd
import sqlite3

# Create the connection
# Note the connect is 'conn1' since there will be multiple .db used
conn1 = sqlite3.connect('planets.db')

# Select all
pd.read_sql("""SELECT * FROM planets; """, conn1)

# CodeGrade step1
# Replace None with your code
df_no_moons = pd.read_sql("""
                          SELECT * FROM planets
                          WHERE num_of_moons =0;
                          """
                          ,conn1)

# CodeGrade step2
# Replace None with your code
df_name_seven = pd.read_sql("""
                            SELECT name, mass
                            FROM planets
                            WHERE LENGTH(name) =7
                            
                            """
                            , conn1)
print(df_name_seven)

# CodeGrade step3
# Replace None with your code
df_mass = pd.read_sql("""
                    SELECT name, mass
                    FROM planets
                    WHERE mass <=1.0;
                      """
                      ,conn1)
print(df_mass)

# CodeGrade step4
# Replace None with your code
df_mass_moon = pd.read_sql("""
                        SELECT num_of_moons, mass
                        FROM planets
                        WHERE num_of_moons > 1
                        AND
                        mass < 100;  
                        """
                        , conn1)
print(df_mass_moon)

# CodeGrade step5
# Replace None with your code
df_blue = pd.read_sql("""
                     SELECT name, color
                     FROM planets 
                     WHERE color = "blue";
                      """
                      , conn1)
print(df_blue)

# CodeGrade step0

# Run this cell without changes

# Create a connection
# Note the connect is 'conn2' since they will be multiple .db used
conn2 = sqlite3.connect('dogs.db')

# Select all
pd.read_sql("SELECT * FROM dogs;", conn2)

# CodeGrade step6
# Replace None with your code
import sqlite3
df_hungry = pd.read_sql("""
                     SELECT name, age , breed
                     FROM dogs
                     WHERE hungry = 1
                     ORDER BY age ASC;
                     """
                        ,conn2)
print(df_hungry)

# CodeGrade step7
# Replace None with your code
df_hungry_ages = pd.read_sql("""
                             SELECT name, age, hungry
                             FROM dogs
                             WHERE hungry=1
                             AND age BETWEEN 2 AND 7
                             ORDER BY name ASC;
                             """
                             ,conn2)
print(df_hungry)

# CodeGrade step8
# Replace None with your code
df_4_oldest = pd.read_sql("""
                        SELECT name, age, breed
                        FROM dogs
                        WHERE age = 4
                        ORDER BY name ASC;                          
                          """
                          , conn2)
print(df_4_oldest)

# CodeGrade step0

# Run this cell without changes

# Create a connection
# Note the connect is 'conn3' since they will be multiple .db used
conn3 = sqlite3.connect('babe_ruth.db')

# Select all
pd.read_sql("""
SELECT * FROM babe_ruth_stats; """, conn3)

# CodeGrade step9
# Replace None with your code
df_ruth_years = pd.read_sql("""
                        SELECT year
                        FROM babe_ruth_stats;                            
                            """
                            , conn3)
print(df_ruth_years)

# CodeGrade step10
# Replace None with your code
df_hr_total = pd.read_sql("""
                        SELECT SUM(HR)
                        FROM babe_ruth_stats;
                        """
                        , conn3)
print(df_hr_total)

# CodeGrade step11
# Replace None with your code
df_teams_years = pd.read_sql("""
                            SELECT team,
                            COUNT(DISTINCT year) AS number_years
                            FROM babe_ruth_stats
                            GROUP BY team;
                            """
                            ,conn3)
print(df_teams_years)

# CodeGrade step12
# Replace None with your code
df_at_bats = pd.read_sql("""
                        SELECT team, at_bats AS average_at_bats
                        FROM babe_ruth_stats
                        WHERE at_bats > 200
                        ORDER BY team ASC;
                        """
                        , conn3)
print(df_at_bats)

# Run this cell without changes

conn1.close()
conn2.close()
conn3.close()