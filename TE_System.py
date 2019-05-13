from Graph.DepthFirstTraversal import *
from Metric import *

TE_System = Graph(directed=True)

# Material Links
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

# Control Links of Feed Valves
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

# Control Links of Reactor
TE_System.addEdge('Reactor', 'FI5', 0)
TE_System.addEdge('Reactor', 'LI1', 0)
TE_System.addEdge('Reactor', 'PI1', 0)
TE_System.addEdge('PI1', 'PLC7', 0)      # Controller of purge valve
TE_System.addEdge('Reactor', 'TI2', 0)
TE_System.addEdge('Reactor', 'TI1', 0)
TE_System.addEdge('TI1', 'PLC5', 0)
TE_System.addEdge('PLC5', 'V5', 0)
TE_System.addEdge('V5', 'Reactor', 0)

# Control Links of Condenser
TE_System.addEdge('Condenser', 'TI3', 0)
TE_System.addEdge('TI4', 'PLC6', 0)
TE_System.addEdge('PLC6', 'V6', 0)
TE_System.addEdge('V6', 'Condenser', 0)
TE_System.addEdge('LI1', 'PLC6', 0)

# Control Links of Separator
TE_System.addEdge('Separator', 'TI4', 0)
TE_System.addEdge('Separator', 'FI6', 0)
TE_System.addEdge('PLC7', 'V7', 0)
TE_System.addEdge('V7', 'FI6', 0)
TE_System.addEdge('Separator', 'PI3', 0)
TE_System.addEdge('Separator', 'FI7', 0)
TE_System.addEdge('Separator', 'LI3', 0)
TE_System.addEdge('LI3', 'PLC8', 0)
TE_System.addEdge('PLC8', 'V8', 0)
TE_System.addEdge('V8', 'LI3', 0)

# Control Links of Stripper
TE_System.addEdge('Stripper', 'PI4', 0)
TE_System.addEdge('Stripper', 'LI4', 0)
TE_System.addEdge('LI4', 'PLC9', 0)
TE_System.addEdge('PLC9', 'V9', 0)
TE_System.addEdge('V9', 'LI4', 0)
TE_System.addEdge('V9', 'FI9', 0)
TE_System.addEdge('Stripper', 'FI9', 0)
TE_System.addEdge('Stripper', 'TI5', 0)
TE_System.addEdge('TI5', 'PLC10', 0)
TE_System.addEdge('PLC10', 'V10', 0)
TE_System.addEdge('V10', 'Stripper', 0)
TE_System.addEdge('V10', 'FI8', 0)

# Control Links of Compressor
TE_System.addEdge('Compressor', 'FI10', 0)
TE_System.addEdge('FI10', 'PLC11', 0)
TE_System.addEdge('PLC11', 'V11', 0)
TE_System.addEdge('V11', 'Compressor', 0)

cfs = Metric('cfs', TE_System.cfs_calculate(), True)
eri = Metric('eri', TE_System.eri_calculate(), True)
metrics = (cfs, eri)
relative_closeness = TOPSIS(metrics)

file_name_1 = 'TE_metrics.xls'
save_all_metrics(file_name_1, metrics)
file_name_2 = 'relative_closeness.xls'
closeness_save(file_name_2, relative_closeness)
