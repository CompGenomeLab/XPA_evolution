import os
import sys
import re
import ete3
from ete3 import Tree
from ete3 import NCBITaxa
from fasta_dict import *
ncbi = NCBITaxa()


def get_most_common_specific_tax_rank(tree_file):
	t = Tree(tree_file,format=1)
	i=1
	for node in t.traverse("postorder"):
		if not node.is_leaf():
			leaf_names = node.get_leaf_names()
			leaf_tax = []
			for leaf in leaf_names:
				tax_id = leaf.split("_")[-1]
				lineage = ncbi.get_lineage(tax_id)
				leaf_tax.append(lineage)
			common_items = set.intersection(*map(set, leaf_tax))
			positions = []

			for common_item in common_items:
				positions.append(leaf_tax[0].index(common_item))
			
			common_tax = leaf_tax[0][max(positions)]
			taxid2name = ncbi.get_taxid_translator([common_tax])

			common_tax_with_name = str(common_tax)+"_"+taxid2name[common_tax]
			common_tax_with_name = re.sub('[\W_]+', '_',common_tax_with_name) 
			node.name = common_tax_with_name+"/node_"+str(i)
			t.write(outfile=tree_file.split(".")[0] + "_lineage.nwk",format=1)
			i += 1



if __name__ == "__main__":
	tree_file = sys.argv[1]
	get_most_common_specific_tax_rank(tree_file)
	
	
