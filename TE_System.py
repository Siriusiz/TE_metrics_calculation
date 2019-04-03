from Graph.DepthFirstTraversal import *
import numpy as np

def TOPSIS(metrics):
    num_of_properties = len(metrics)
    max = []
    for metric in metrics:
        temp_list = []
        for i in metric:
            temp_list.append(metric[i])
        max.append(np.max(temp_list))

    # standardized
    for i in range(num_of_properties):
        for j in metrics[i]:
            metrics[i][j] = metrics[i][j] / max[i]
    print(metrics)

    # PCA
    avg = []
    std_dev = []
    pca_metrics = metrics
    for metric in pca_metrics:
        temp_list = []
        for i in metric:
            temp_list.append(metric[i])
        avg.append(np.average(temp_list))
        std_dev.append(np.std(temp_list))
    print(avg)
    print(std_dev)
    for i in range(num_of_properties):
        for j in pca_metrics[i]:
            pca_metrics[i][j] = (pca_metrics[i][j] - avg[i])/std_dev[i]

    print(pca_metrics)

TE_System = Graph(directed=True)

# 物料流动链路
TE_System.addEdge('A', 'V1', 1)
TE_System.addEdge('V1', 'Reactor', 1)
TE_System.addEdge('D', 'V2', 1)
TE_System.addEdge('V2', 'Reactor', 1)
TE_System.addEdge('E', 'V3', 1)
TE_System.addEdge('V3', 'Reactor', 1)
TE_System.addEdge('A/C', 'V4', 1)
TE_System.addEdge('V4', 'Stripper', 1)
TE_System.addEdge('Reactor', 'Condenser', 1)
TE_System.addEdge('Condenser', 'Separator', 1)
TE_System.addEdge('Separator', 'Compressor', 1)
TE_System.addEdge('Separator', 'V8', 1)
TE_System.addEdge('Compressor', 'Reactor', 1)
TE_System.addEdge('V8', 'Stripper', 1)
TE_System.addEdge('Stripper', 'V9', 1)
TE_System.addEdge('Stripper', 'Reactor', 1)

# 进料阀信息链路
TE_System.addEdge('A', 'FI1', 0)
TE_System.addEdge('FI1', 'PLC1', 0)
TE_System.addEdge('PLC1', 'V1', 0)
TE_System.addEdge('V1', 'FI1', 0)

TE_System.addEdge('D', 'FI2', 0)
TE_System.addEdge('FI2', 'PLC2', 0)
TE_System.addEdge('PLC2', 'V2', 0)
TE_System.addEdge('V2', 'FI2', 0)

TE_System.addEdge('E', 'FI3', 0)
TE_System.addEdge('FI3', 'PLC3', 0)
TE_System.addEdge('PLC3', 'V3', 0)
TE_System.addEdge('V3', 'FI3', 0)

TE_System.addEdge('A/C', 'FI4', 0)
TE_System.addEdge('FI4', 'PLC4', 0)
TE_System.addEdge('PLC4', 'V4', 0)
TE_System.addEdge('V4', 'FI4', 0)

# 反应器信息链路
TE_System.addEdge('Reactor', 'FI5', 0)
TE_System.addEdge('Reactor', 'LI1', 0)
TE_System.addEdge('Reactor', 'PI1', 0)
TE_System.addEdge('Reactor', 'TI1_A', 0)
TE_System.addEdge('TI1_A', 'PLC5', 0)
TE_System.addEdge('Reactor', 'TI1_B', 0)
TE_System.addEdge('TI1_B', 'PLC5', 0)
TE_System.addEdge('PLC5', 'V5', 0)
TE_System.addEdge('V5', 'Reactor', 0)

# 冷凝器信息链路
TE_System.addEdge('Condenser', 'TI2', 0)
TE_System.addEdge('TI2', 'PLC6', 0)
TE_System.addEdge('PLC6', 'V6', 0)
TE_System.addEdge('V6', 'Condenser', 0)

# 分离器信息链路
TE_System.addEdge('Separator', 'PI3', 0)
TE_System.addEdge('Separator', 'FI6', 0)
TE_System.addEdge('FI6', 'PLC7', 0)
TE_System.addEdge('PLC7', 'V7', 0)
TE_System.addEdge('V7', 'FI6', 0)
TE_System.addEdge('Separator', 'TI3', 0)
TE_System.addEdge('Separator', 'LI3', 0)
TE_System.addEdge('Separator', 'FI7', 0)
TE_System.addEdge('FI7', 'PLC8', 0)
TE_System.addEdge('PLC8', 'V8', 0)
TE_System.addEdge('V8', 'FI7', 0)

# 汽提塔信息链路
TE_System.addEdge('Stripper', 'LI4', 0)
TE_System.addEdge('Stripper', 'PI4', 0)
TE_System.addEdge('Stripper', 'FI8', 0)
TE_System.addEdge('FI8', 'PLC9', 0)
TE_System.addEdge('PLC9', 'V9', 0)
TE_System.addEdge('V9', 'FI8', 0)
TE_System.addEdge('Stripper', 'TI4', 0)
TE_System.addEdge('TI4', 'PLC10', 0)
TE_System.addEdge('PLC10', 'V10', 0)
TE_System.addEdge('V10', 'Stripper', 0)

# 压缩器信息链路
TE_System.addEdge('Compressor', 'FI9', 0)
TE_System.addEdge('FI9', 'PLC11', 0)
TE_System.addEdge('PLC11', 'V11', 0)
TE_System.addEdge('V11', 'Compressor', 0)

print(TE_System.num_of_vertices())
cfs = TE_System.cfs_calculate()
eri = TE_System.eri_calculate()
# print(cfs)
# print(eri)
# print(sorted(metrics.items(), key=lambda item: item[1], reverse=True))
metrics = (cfs, eri)
# file_name = 'TE_metrics_02.xls'
# metrics_save(filename, metrics)
# save_all_metrics(file_name, metrics)
# print(metrics)
TOPSIS(metrics)
