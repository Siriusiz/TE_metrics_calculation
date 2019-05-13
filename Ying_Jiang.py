# This TEP-Critical-Node-Identification-Algorithm is proposed by Ying Jiang
# Ying J , Zheng W , Yan Q , et al.
# AHP-SDG model establishment and key node identification of chemical process system based on complex network[J].
# Chemical Industry and Engineering Progress, 2018.(In Chinese)
import networkx as nx
from Metric import *

TE_system = nx.DiGraph()

# Material Links
TE_system.add_edge('A', 'V1')
TE_system.add_edge('V1', 'Reactor')
TE_system.add_edge('D', 'V2')
TE_system.add_edge('V2', 'Reactor')
TE_system.add_edge('E', 'V3')
TE_system.add_edge('V3', 'Reactor')
TE_system.add_edge('A/C', 'V4')
TE_system.add_edge('V4', 'Stripper')
TE_system.add_edge('Reactor', 'Condenser')
TE_system.add_edge('Condenser', 'Separator')
TE_system.add_edge('Separator', 'V8')
TE_system.add_edge('Separator', 'Compressor')
TE_system.add_edge('V8', 'Stripper')
TE_system.add_edge('Stripper', 'V9')
TE_system.add_edge('Stripper', 'Reactor')
TE_system.add_edge('Compressor', 'Reactor')

# Control Links of Feed Valves
TE_system.add_edge('A', 'FI1')
TE_system.add_edge('FI1', 'PLC1')
TE_system.add_edge('PLC1', 'V1')
TE_system.add_edge('V1', 'FI1')

TE_system.add_edge('D', 'FI2')
TE_system.add_edge('FI2', 'PLC2')
TE_system.add_edge('PLC2', 'V2')
TE_system.add_edge('V2', 'FI2')

TE_system.add_edge('E', 'FI3')
TE_system.add_edge('FI3', 'PLC3')
TE_system.add_edge('PLC3', 'V3')
TE_system.add_edge('V3', 'FI3')

TE_system.add_edge('A/C', 'FI4')
TE_system.add_edge('FI4', 'PLC4')
TE_system.add_edge('PLC4', 'V4')
TE_system.add_edge('V4', 'FI4')

# Control Links of Reactor
TE_system.add_edge('Reactor', 'FI5')
TE_system.add_edge('Reactor', 'LI1')
TE_system.add_edge('Reactor', 'PI1')
TE_system.add_edge('PI1', 'PLC7')
TE_system.add_edge('Reactor', 'TI2')
TE_system.add_edge('Reactor', 'TI1')
TE_system.add_edge('TI1', 'PLC5')
TE_system.add_edge('PLC5', 'V5')
TE_system.add_edge('V5', 'Reactor')

# Control Links of Condenser
TE_system.add_edge('Condenser', 'TI3')
TE_system.add_edge('TI4', 'PLC6')
TE_system.add_edge('PLC6', 'V6')
TE_system.add_edge('V6', 'Condenser')
TE_system.add_edge('LI1', 'PLC6')

# Control Links of Separator
TE_system.add_edge('Separator', 'TI4')
TE_system.add_edge('Separator', 'FI6')
TE_system.add_edge('Separator', 'V7')
TE_system.add_edge('PLC7', 'V7')
TE_system.add_edge('V7', 'FI6')
TE_system.add_edge('Separator', 'PI3')
TE_system.add_edge('Separator', 'FI7')
TE_system.add_edge('Separator', 'LI3')
TE_system.add_edge('LI3', 'PLC8')
TE_system.add_edge('PLC8', 'V8')
TE_system.add_edge('V8', 'LI3')

# Control Links of Stripper
TE_system.add_edge('Stripper', 'PI4')
TE_system.add_edge('Stripper', 'LI4')
TE_system.add_edge('LI4', 'PLC9')
TE_system.add_edge('PLC9', 'V9')
TE_system.add_edge('V9', 'LI4')
TE_system.add_edge('V9', 'FI9')
TE_system.add_edge('Stripper', 'FI9')
TE_system.add_edge('Stripper', 'TI5')
TE_system.add_edge('TI5', 'PLC10')
TE_system.add_edge('PLC10', 'V10')
TE_system.add_edge('V10', 'Stripper')
TE_system.add_edge('V10', 'FI8')

# Control Links of Compressor
TE_system.add_edge('Compressor', 'FI10')
TE_system.add_edge('FI10', 'PLC11')
TE_system.add_edge('PLC11', 'V11')
TE_system.add_edge('V11', 'Compressor')

undirected_TE = TE_system.to_undirected()

DC = Metric('DC', nx.degree_centrality(TE_system), True)
CC = Metric('CC', nx.closeness_centrality(TE_system), True)
EC = Metric('EC', nx.eigenvector_centrality(TE_system), True)
C = Metric('C', nx.constraint(undirected_TE), False)
FBC = Metric('FBC', nx.current_flow_betweenness_centrality(undirected_TE), True)
metrics = (DC, CC, FBC, EC, C)
relative_closeness = TOPSIS(metrics)

file_name_1 = 'TE_metrics_Jiang.xls'
save_all_metrics(file_name_1, metrics)
file_name_2 = 'relative_closeness_Jiang.xls'
metric_save(file_name_2, relative_closeness)
