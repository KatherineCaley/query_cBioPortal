### Downloading mutation and CNV matrices from the bioportal 

`genes.txt` is a file containing the list of gene of interest. The gene names should be in the first column of the file. The file should be newline-delimited. 

`cancers.txt` is a file containing the list of cancer types of interest. The cancer names should be in the first column of the file. The file should be newline-delimited.

`get_mut_matrix.ipynb` will download the mutation matrix for the genes and cancers of interest. The mutation matrix will be saved as a csv file in the queried_data folder.

`get_cnv_matrix.ipynb` will download the CNV matrix for the genes and cancers of interest. The CNV matrix will be saved as a csv file in the queried_data folder.


### Matching the queried data with the metadata for the slides


`match_TCGA_slide_rna` is a directory containing dataframes that match the location of TCGA slides to the metadata. For each file in this directory, which corresponds to a different cancer, the code will query the bioportal for the corresponding mutation and CNV data.

The naming convention for the files in match_TCGA_slide_rna is: <cancer type>_slide_matched.csv, this is important and used to query the bioportal for the corresponding mutation and CNV data.

