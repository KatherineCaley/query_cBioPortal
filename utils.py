from progressbar import ProgressBar


def get_muts(cancer, portal):
    return portal.Mutations.getMutationsInMolecularProfileBySampleListIdUsingGET(
        molecularProfileId=f"{cancer}_tcga_pan_can_atlas_2018_mutations",
        sampleListId=f"{cancer}_tcga_pan_can_atlas_2018_all",
        projection="DETAILED",
    ).result()


def get_cnas(cancer, portal):
    return portal.Discrete_Copy_Number_Alterations.getDiscreteCopyNumbersInMolecularProfileUsingGET(
        molecularProfileId=f"{cancer}_tcga_pan_can_atlas_2018_gistic",
        sampleListId=f"{cancer}_tcga_pan_can_atlas_2018_all",
        projection="DETAILED",
    ).result()


def muts_to_df(mutations, genes, df):
    pbar = ProgressBar()
    if genes:
        mutations = [m for m in mutations if m["gene"]["hugoGeneSymbol"] in genes]

    for m in pbar(mutations):
        df.loc[m["sampleId"], m["gene"]["hugoGeneSymbol"]] = 1

    df.fillna(0, inplace=True)
    return df


def cnas_to_df(cnas, genes, df):
    pbar = ProgressBar()
    if genes:
        cnas = [c for c in cnas if c["gene"]["hugoGeneSymbol"] in genes]

    for cna in pbar(cnas):
        df.loc[cna["sampleId"], cna["gene"]["hugoGeneSymbol"]] = cna["alteration"]

    df.fillna(1, inplace=True)
    return df


def get_sample_ids(cancer, portal):
    samples = (
        portal.Samples.getAllSamplesInStudyUsingGET(
            studyId=f"{cancer}_tcga_pan_can_atlas_2018"
        )
        .response()
        .result
    )
    return {sample["sampleId"]: sample["patientId"] for sample in samples}
