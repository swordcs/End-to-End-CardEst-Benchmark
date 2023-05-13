import numpy as np
from scipy.stats.mstats import gmean


for workload in ["job","stats"]:
    old = []
    new = []
    act = []

    with open("results/{}/old_new_join_est.txt".format(workload),'r') as f:
        data = f.readlines()
        for e in data:
            old_est, new_est = e.split(":")
            old.append(float(old_est))
            new.append(float(new_est))
    with open("results/{}/{}_sub_queries_default.txt".
              format(workload, workload + ("_CEB" if workload == "stats" else "_light")),'r') as f:
        data = f.readlines()
        for e in data:
            act.append(float(e))
    
    old = np.array(old)
    new = np.array(new)
    act = np.array(act)

    old_q_error = []
    new_q_error = []

    for i in range(len(old)):
        old_q_error.append(max(old[i]/act[i], act[i]/old[i]))
        new_q_error.append(max(new[i]/act[i], act[i]/new[i]))
    
    old_q_error = np.array(old_q_error)
    new_q_error = np.array(new_q_error)
    old_q_error.sort()
    new_q_error.sort()

    old_q_error = old_q_error[:-1]
    new_q_error = new_q_error[:-1]
    print("-----------------------------{}-------------------------------".format(workload))
    for q_error_arr,type in [(old_q_error,"old"),(new_q_error,"new")]:
        print(type + " max:  " + str(np.max(q_error_arr)))
        print(type + " 99th: " + str(np.percentile(q_error_arr,99)))
        print(type + " 95th: " + str(np.percentile(q_error_arr,95)))
        print(type + " 90th: " + str(np.percentile(q_error_arr,90)))
        print(type + " mid:  " + str(np.percentile(q_error_arr,50)))
        print(type + " mean: " + str(np.mean(q_error_arr)))
        print(type + " gmean:" + str(gmean(q_error_arr)))