import os
from bravado.client import SwaggerClient
import pandas as pd
import click

from utils import get_muts, muts_to_df, get_sample_ids


@click.command()
@click.option(
    "--gene_list",
    "-g",
    is_flag=True,
    show_default=True,
    default=False,
    help="If True, only genes in the gene list in `genes.txt` file will be returned",
)
@click.option(
    "--overwrite",
    "-o",
    is_flag=True,
    show_default=True,
    default=False,
    help="If True, overwrite the existing file",
)
@click.option(
    "--cancer_list",
    "-c",
    type=click.Path(exists=True),
    help="Path to a .txt file containing list of cancers to query, default is all 32 cancers",
    default="cancers.txt",
)
def main(gene_list, cancer_list, overwrite):
    """Get mutation matrix for all cancers in the cancer list"""
    if gene_list:
        assert os.path.isdir(
            "genes"
        ), "No `genes` directory found, either create one or run without the `-g` flag"
        assert (
            len(os.listdir("genes")) > 0
        ), "No gene files found in `genes` directory, either add some or run without the `-g` flag"

    cbioportal = SwaggerClient.from_url(
        "https://www.cbioportal.org/api/v2/api-docs",
        config={
            "validate_requests": False,
            "validate_responses": False,
            "validate_swagger_spec": False,
        },
    )

    # read in the cancers from the cancers.txt file
    with open(cancer_list, "r") as f:
        cancers = [cancer.strip() for cancer in f]

    for cancer in cancers:
        if (
            os.path.isfile(f"queried_data/mutation_matrices/{cancer}_mut_matrix.csv")
            and not overwrite
        ):
            print(f"mutation data for {cancer} already exists, skipping")
            continue
        print(f"downloading mutation matrix for {cancer}")

        # read in the genes from the genes.txt file
        if gene_list and os.path.isfile(f"genes/{cancer}_cna.txt"):
            with open(f"genes/{cancer.lower()}.txt", "r") as f:
                genes = [gene.strip() for gene in f]
        else:
            genes = None

        sample_info = get_sample_ids(cancer, cbioportal)

        # create dataframe with sampleIDs as index and patientIDs as columns
        df_blank = pd.DataFrame(index=sample_info.keys())
        df_patient = pd.DataFrame.from_dict(
            sample_info, orient="index", columns=["patient_id"]
        )
        df = pd.merge(df_blank, df_patient, left_index=True, right_index=True)

        # query the bioportal for the mutation information
        muts = get_muts(cancer, cbioportal)

        mutation_df = muts_to_df(muts, genes, df)

        mutation_df.to_csv(f"queried_data/mutation_matrices/{cancer}.csv")


if __name__ == "__main__":
    main()
