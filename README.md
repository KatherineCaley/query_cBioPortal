### Downloading mutation and CNV matrices from the bioportal 

Running the `get_mut_matrix.ipynb` script will download the mutation matrix for the cancers of interest (provided in the `cancers.txt` file). The mutation matrix will be saved as a csv file in the queried_data folder, sample_ids are the row labels, and gene names are the column labels. The value in the matrix are binary, 0 if no mutation, 1 if the gene is mutated in the sample. 


Running the `get_cnv_matrix.ipynb` script will download the discrete copy number alteration matrix for the cancers of interest (provided in the `cancers.txt` file). The mutation matrix will be saved as a csv file in the queried_data folder, sample_ids are the row labels, and gene names are the column labels. The values in the matrix are the alteration. 


`cancers.txt` is a file containing the list of cancer types of interest. The cancer names should be in the first column of the file. The file should be newline-delimited.


`genes.txt` is a file containing the list of gene of interest. The gene names should be in the first column of the file. The file should be newline-delimited. 

 - If the `gene_list` variable is not set to `True`, the script will download the mutation and CNV matrices for all genes in the bioportal.


### Matching the queried data with the metadata for the slides


`match_TCGA_slide_rna` is a directory containing dataframes that match the location of TCGA slides to the metadata. For each file in this directory, which corresponds to a different cancer, the code will query the bioportal for the corresponding mutation and CNV data.

The naming convention for the files in match_TCGA_slide_rna is: <cancer type>_slide_matched.csv, this is important and used to match to the queried mutation and CNV data.

