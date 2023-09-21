# XPA_evolution

This repository contains three Python scripts ('midpoint_rooting.py', 'add_lineage.py', and 'label_duplication_nodes.py') that were used in the analysis of phylogenetic trees for determining functional homologs of a protein. These scripts are designed to aid in tree manipulation, taxonomic lineage annotation, and the identification of duplication nodes in the tree.

## `midpoint_rooting.py`

The midpoint_rooting.py script is used for applying midpoint rooting to a phylogenetic tree. Midpoint rooting is a technique that helps to place the root of a tree at a midpoint, typically equidistant from its most distant tips. In the context of this project, the second hit for XPA was used as a reference point to manually place the tree root.

```python midpoint_rooting.py input_tree_file output_tree_file```


## `add_lineage.py`

The add_lineage.py script is utilized to add taxonomic lineage information to the nodes of a phylogenetic tree. It assigns the most common lowest taxonomic level of clades to each node in the tree. This step is crucial for understanding the evolutionary relationships between different species in the tree.

```python add_lineage.py input_tree_file output_tree_file```


## `label_duplication_nodes.py`

The label_duplication_nodes.py script is employed to identify duplication nodes within a phylogenetic tree. It counts the common species between clades and annotates the nodes as duplication nodes if there is more than one common species. This information is invaluable for pinpointing duplication and deletion events in the evolutionary history of the protein.

```python label_duplication_nodes.py input_tree_file output_tree_file```
