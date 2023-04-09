stats_single_table_file = open(
    '../../workloads/job_light/sub_plan_queries/job_light_single_table_sub_query.sql')
stats_single_est_file = open('job_light_single_table_est.txt', 'w')
queries = stats_single_table_file.readlines()


for query in queries:
    est = query.split('||')[-1]
    stats_single_est_file.write(est[:-1] + '.0\n')

