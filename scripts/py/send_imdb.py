import psycopg2
import os
import time

conn = psycopg2.connect(database="job", host="127.0.0.1", port=5433)
cursor = conn.cursor()

imdb_sql_file = open("../../workloads/job_light/job_light_queries.sql")
res_file = open("./job_res.txt",'w')
queries = imdb_sql_file.readlines()
imdb_sql_file.close()

if os.path.exists("/home/gjbox/Projects/End-to-End-CardEst-Benchmark/postgresql-13.1/pgsql/join_est_record_job.txt"):
    os.remove("/home/gjbox/Projects/End-to-End-CardEst-Benchmark/postgresql-13.1/pgsql/join_est_record_job.txt")

# cursor.execute('SET debug_card_est=true')
#cursor.execute('SET print_sub_queries=true')
# cursor.execute('SET print_single_tbl_queries=true')
res_file.write(str(time.time()) + "start\n")
for no, query in enumerate(queries):
    cursor.execute(query.split("||")[0])
    res = cursor.fetchall()
    res_file.write(str(time.time()) + " {}-th query finished.\n".format(no))

cursor.close()
conn.close()
