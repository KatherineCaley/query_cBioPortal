### Command line interface for downloading Mutation and Copy Number Alteration (CNA) data from the cBioPortal

 https://www.cbioportal.org/

#### Downloading `query_cBioPortal`

```shell
git clone https://github.com/KatherineCaley/query_cBioPortal.git
```

Install project dependencies 

```shell
pip install pandas 
pip install bravado
pip install progressbar
pip install click
```



#### Downloading the data 

There are two main scripts, `get_mut_matrix.py` and `get_cna_matrix.py` which download the mutation and CNA data respectively. 

By default, data for all 32 cancers listed in `cancers.txt` will be downloaded. 



> #### Mutation Data 

How to download mutation data for all cancers and all genes:

```shell
cd query_cbioportal
python3 get_mut_matrix.py
```

To download mutation data for *certain cancers*, create a .txt file of the cancers of interest (must be in TCGA abbreviation), and provide the path to that file following the -c flag

```shell
python3 get_mut_matrix.py -c path/to/cancer_list.txt
```

To only download mutation data for *certain genes*, create a .txt file in the `genes` directory, following the exact naming convention `{cancer}_mut.txt`, for example, for BRCA, it would be called `brca_mut.txt` **and ** add the -g flag

```shell
python3 get_mut_matrix.py -c path/to/cancer_list.txt -g
```

To overwrite a previously downloaded file, add the -o flag

```shell 
python3 get_mut_matrix.py -c path/to/cancer_list.txt -g -o 
```





> #### CNA Data 

How to download CNA data for all cancers and all genes:

```shell
cd query_cbioportal
python3 get_cna_matrix.py
```

To download CNA data for *certain cancers*, create a .txt file of the cancers of interest (must be in TCGA abbreviation and seperate by the newline character), and provide the path to that file following the -c flag

```shell
python3 get_cna_matrix.py -c path/to/cancer_list.txt
```

To only download CNA data for *certain genes*, create a .txt file in the `genes` directory, following the exact naming convention `{cancer}_cna.txt`, for example, for BRCA, it would be called `brca_cna.txt` **and ** add the -g flag

```shell
python3 get_cna_matrix.py -c path/to/cancer_list.txt -g
```

To overwrite a previously downloaded file, add the -o flag

```shell 
python3 get_cna_matrix.py -c path/to/cancer_list.txt -g -o 
```





