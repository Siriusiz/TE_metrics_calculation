import numpy as np
import pandas as pd
import xlwt
from collections import defaultdict

class Metric:
    def __init__(self, name, result, type):
        self.type = type
        self.name = name
        self.result = result
        self.normalized = self.get_normalized()
        self.pca_normalized = self.get_pca_normalized()

    def get_criterion(self):
        cache = []
        for key in self.result:
            cache.append(self.result[key])
        if self.type == True:
            return np.max(cache)
        else:
            return np.min(cache)

    def get_normalized(self):
        cache = {}
        if self.type == True:
            temp = self.get_criterion()
            for key in self.result:
                cache[key] = self.result[key]/temp
        else:
            temp = self.get_criterion()
            for key in self.result:
                cache[key] = temp / self.result[key]
        return cache

    def get_pca_avg(self):
        cache = []
        for key in self.normalized:
            cache.append(self.normalized[key])
        return np.average(cache)

    def get_pca_std(self):
        cache = []
        for key in self.normalized:
            cache.append(self.normalized[key])
        return np.std(cache)

    def get_pca_normalized(self):
        cache = {}
        pca_avg = self.get_pca_avg()
        pca_std = self.get_pca_std()
        for key in self.normalized:
            temp = (self.normalized[key]-pca_avg)/pca_std
            cache[key] = temp
        return cache


def TOPSIS(metrics):
    normalized = defaultdict(list)
    # pca_normalized = defaultdict(list)
    vertices = []
    for key in metrics[0].result:
        vertices.append(key)
    num_of_vertices = len(vertices)

    for metric in metrics:
        for key in metric.normalized:
            normalized[metric.name].append(metric.normalized[key])

    weight = get_pca_weight(metrics)                                    # 计算权重

    for key in normalized:
        for i in range(len(normalized[key])):
            normalized[key][i] = normalized[key][i] * weight[key]       # 得出加权标准化

    ideal_solution = defaultdict(list)                                  # 得出正、负理想解
    for key in normalized:
        ideal_solution[key].append(np.max(normalized[key]))
        ideal_solution[key].append(np.min(normalized[key]))

    distance = defaultdict(list)                                        # 计算欧氏距离
    for i in range(num_of_vertices):
        dist_positive = 0
        dist_negative = 0
        for key in ideal_solution:
            dist_positive += np.square(normalized[key][i] - ideal_solution[key][0])
            dist_negative += np.square(normalized[key][i] - ideal_solution[key][1])
        distance[i].append(np.sqrt(dist_positive))
        distance[i].append(np.sqrt(dist_negative))
    # print(distance)

    relative_closeness = {}                              # 计算贴进度
    for key in distance:
        relative_closeness[vertices[key]] = distance[key][1] / np.sum(distance[key])

    return relative_closeness

def get_pca_weight(metrics):
    pca_normalized = defaultdict(list)
    for metric in metrics:
        for key in metric.pca_normalized:
            pca_normalized[metric.name].append(metric.pca_normalized[key])

    df = pd.DataFrame(data=pca_normalized)
    corr = df.corr()

    eig = np.linalg.eig(corr)
    eigvalue = []
    for i in eig[0]:
        eigvalue.append(i)
    eigvalue.sort(reverse=True)                                      # 特征值排序

    principal_component = []
    temp_1 = 0
    for i in eigvalue:
        if temp_1 < 0.85:                                           # 判断累计方差贡献率
            temp_1 += i / np.sum(eigvalue)
            principal_component.append(i)
        else:
            break

    cache_1 = defaultdict(list)
    for i in range(len(eigvalue)):
        for j in range(len(eigvalue)):
            cache_1[eigvalue[i]].append(eig[1][j][i])

    cache_2 = defaultdict(list)
    for i in principal_component:
        for j in cache_1[i]:
            cache_2[i].append(j * i)
    weight = {}
    sum = 0
    for i in range(len(metrics)):
        temp_2 = 0
        for j in cache_2:
            temp_2 += cache_2[j][i]
        weight[metrics[i].name] = temp_2 / len(principal_component)
        sum += temp_2 / len(principal_component)
    for key in weight:
        weight[key] /= sum                                            # 得出权重

    return weight

def closeness_save(file_name, metrics):                # 将计算结果保存到xls文件中
    temp_list = [('节点名称', '贴进度')]
    for metric in metrics:
        temp_list.append((metric, metrics[metric]))

    file = xlwt.Workbook()
    sheet1 = file.add_sheet('sheet1', cell_overwrite_ok=True)
    style = xlwt.XFStyle()
    al = xlwt.Alignment()
    al.vert = 0x01
    al.horz = 0x02
    style.alignment = al

    for i in range(len(temp_list)):
        for j in range(len(temp_list[i])):
            sheet1.write(i, j, temp_list[i][j], style)
    file.save(file_name)

def save_all_metrics(file_name, metrics):
    metrics_list = defaultdict(list)
    temp_list = [['节点名称']]
    for metric in metrics:
        temp_list[0].append(metric.name)
    for metric in metrics:
        for key in metric.result:
            metrics_list[key].append(metric.result[key])
    for node in metrics_list:
        cache = [node]
        for value in metrics_list[node]:
            cache.append(value)
        temp_list.append(cache)

    file = xlwt.Workbook()
    sheet1 = file.add_sheet('sheet1', cell_overwrite_ok=True)
    style = xlwt.XFStyle()
    al = xlwt.Alignment()
    al.vert = 0x01
    al.horz = 0x02
    style.alignment = al

    for i in range(len(temp_list)):
        for j in range(len(temp_list[i])):
            sheet1.write(i, j, temp_list[i][j], style)
    file.save(file_name)
