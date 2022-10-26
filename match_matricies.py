import os
import pandas as pd
import click


@click.command()
@click.option(
    "--left",
    "-l",
    type=click.Path(exists=True),
    help="Path to the directory containing the left matrix, must be either a mutation or copy number matrix",
    required=True,
)
@click.option(
    "--right",
    "-r",
    type=click.Path(exists=True),
    help="Path to the directory containing the right matrix, this is the data you wish to join to mutation or copy number matrix",
    required=True,
)
@click.option(
    "--index",
    "-i",
    type=str,
    help="The column to join on from the right df, default is `sample_id`",
    default="sample_id",
)
@click.option(
    "--outpath",
    "-o",
    type=click.Path(exists=False),
    help="Path to the output directory, default is `matched_data/`",
    default="matched_matrices/",
)
def main(left, right, index, outpath):
    """Join two matrices on a specified index,

    NOTE: The left matrix must be either a mutation or copy number matrix generated by this repo
    NOTE: The right matrix must have a column with the sample_id from the TCGA data, this column must be specified with the `-i` flag
    NOTE: The right matrix **MUST** have the cancer type as the first part of the name, followed by an underscore"""

    for matrix in os.listdir(right):
        if matrix.endswith(".csv"):
            cancer = matrix.split("_")[0]
            l = pd.read_csv(f"{left}/{cancer}.csv", index_col=0)
            r = pd.read_csv(f"{right}/{matrix}", index_col=index)

            joined = l.join(r, how="outer")

            data_type = left.split("/")[-1]  # is it mut or cnv data?
            # create the output directory if it doesn't exist
            if not os.path.isdir(f"{outpath}/{data_type}"):
                os.mkdir(f"{outpath}/{data_type}")

            joined.to_csv(f"{outpath}/{data_type}/{cancer}.csv")


if __name__ == "__main__":
    main()
