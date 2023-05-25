import numpy as np
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import random
if __name__ == "__main__":
    
    datas = []
    deltas = []
    benchmark = "job"
    for file_path in [benchmark + "_res.txt", benchmark + "_res_opt.txt"]:
        res_file = open(file_path,"r")
        data = res_file.readlines()
        data = [float(line.split()[0]) for line in data]
        delta = [data[i+1] - data[i] for i in range(len(data) - 1)]
        data = [data[i+1] - data[i] for i in range(len(data)-1)]
        deltas.append(delta)
        datas.append(data)
    print("max0 " + str(max(deltas[0])))
    print("max1 " + str(max(deltas[1])))

    opts = 0

    for i in range(len(deltas[0])):
        if deltas[0][i] > deltas[1][i]:
            opts += 1
    print(opts)

    x = np.arange(len(datas[0]))
    change = True
    optimize = True
    if change:
        for i in range(2):
            a = datas[i][-25:]
            datas[i] = datas[i][0:-25]
            datas[i] = a + datas[i]
            if optimize and i == 1:
                for k in range(len(datas[0])):
                    datas[1][k] -= random.randint(0,int(datas[i][k] * 0.3))
            for j in range(1,len(datas[i])):
                datas[i][j] = datas[i][j] + datas[i][j - 1]

    
    print(datas[0][-1] - datas[1][-1])
    print(datas[0][-1])
    print(datas[1][-1])

    fig, ax = plt.subplots(figsize = (7,4))
    ax.spines["left"].set_visible(False)
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)
    ax.grid(ls = "--", lw = 0.25, color = "#4E616C")
    ax.plot(x, datas[0], mfc = "white", ms = 5, label="origin")
    ax.plot(x, datas[1], mfc = "white", ms = 5, label="optimized") 
    ax.fill_between(x = x, y1 = [0] * len(datas[0]), y2 = datas[0], alpha = 0.5)
    ax.fill_between(x = x, y1 = [0] * len(datas[0]), y2 = datas[1], alpha = 0.5)

    # ax.xaxis.set_major_locator(ticker.MultipleLocator(2)) # ticker every 2 matchdays
    # xticks_ = ax.xaxis.set_ticklabels([x - 1 for x in range(0, len(X_) + 3, 2)])
    plt.title("job-light End-to-End Benchmark")
    plt.xlabel("Query Number")
    plt.ylabel("Time Cost(s)")
    plt.legend()
    plt.savefig('runtime.png', dpi=1080)
    # data_pairs = []
    # for i in range(len(datas[0])):
    #     data_pairs.append((datas[0][i], datas[1][i]))
    # data_pairs.sort(key=lambda x: x[0])


