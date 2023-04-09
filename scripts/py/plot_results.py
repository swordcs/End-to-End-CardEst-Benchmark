import numpy as np
import matplotlib.pyplot as plt

def plot_bars(data, title, xlabel, ylabel, save_path, x=None, xticklabels=None, dpi=1080):
    # [(data, label), (data, label), (data, label)...]
    if x is None:
        x = np.arange(len(data[0][0]))
    else:
        x = np.array(x)

    # 设置图形大小
    fig, ax = plt.subplots(figsize=(8, 5))

    for i in range(len(data)):
        # TODO some bug here
        ax.bar(x - 1/6 + i * 2/(3*len(data)) - 1/(3*len(data)),
               data[i][0], width=2/(3*len(data)), label=data[i][1], edgecolor='black')

    # 绘制条形图
    ax.set_xlabel(xlabel)
    ax.set_ylabel(ylabel)
    ax.set_title(title)
    # 设置x轴标签
    ax.set_xticks(x)
    if xticklabels:
        ax.set_xticklabels([3, 5, 10])

    # 设置图例
    ax.legend()
    # 显示图形
    plt.savefig(save_path, dpi=dpi)

if __name__ == "__main__":
    
    datas = []
    for file_path in ["job_res.txt", "job_res_opt.txt"]:
        res_file = open(file_path,"r")
        data = res_file.readlines()
        data = [float(line.split()[0]) for line in data]
        data = [data[i+1] - data[i] for i in range(len(data) - 1)]
        datas.append(data)
    data_pairs = []
    for i in range(len(datas[0])):
        data_pairs.append((datas[0][i], datas[1][i]))
    data_pairs.sort(key=lambda x: x[0])
    step = 15
    for i in range(0, len(data_pairs), step):
        data_tmp = []
        data0 = [data[0] for data in data_pairs[i: min(i + step, len(data_pairs))]]
        data1 = [data[1] for data in data_pairs[i: min(i + step, len(data_pairs))]]
        data_tmp.append((data0, "origin"))
        data_tmp.append((data1, "opt"))
        plot_bars(data_tmp,"Time cost","index_number","Time (s)","../../results/job/Job{}.png".format(i), dpi=1080)

