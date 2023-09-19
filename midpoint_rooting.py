import sys
import ete3
from ete3 import Tree

tree_file = sys.argv[1]
t = Tree(tree_file,format=1)
R = t.get_midpoint_outgroup()
t.set_outgroup(R)
t.write(outfile=tree_file.replace(".nwk", "_mid.nwk"),format=1)

