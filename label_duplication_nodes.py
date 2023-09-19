import sys
import json
import os
import ete3 
from ete3 import Tree, PhyloTree


def label_duplication_nodes(tree_file):
    t = Tree(tree_file,format=1)
    for node in t.traverse("preorder"):
        if not node.is_leaf():
            children = node.get_children()
            ch1,ch2 = children
            leaves1 = [leaf.name for leaf in ch1.get_leaves()]
            leaves2 = [leaf.name for leaf in ch2.get_leaves()]
            node1_taxon = set()
            node2_taxon = set()
            for leaf in leaves1:
                taxid1 = leaf.split("_")[-1]
                node1_taxon.add(taxid1)
            for leaf2 in leaves2:
                taxid2 = leaf2.split("_")[-1]
                node2_taxon.add(taxid2)
            
            common_taxa = len(set.intersection(node1_taxon, node2_taxon))
            min_clade = min(len(node1_taxon),len(node2_taxon))
            if common_taxa:
                print(min_clade)
            if common_taxa >= 1 :
                node.name = "Dup:" +str(common_taxa) + "/" + str(min_clade)
     
    new_t = t
    new_t.write(outfile=tree_file.split(".")[0] + "_dup.nwk",format=1)
    return new_t

if __name__ == "__main__":
	tree_file = sys.argv[1]
	label_duplication_nodes(tree_file)



