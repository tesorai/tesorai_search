"""
Reads the data, removes decoys and maps I -> L
Created on 2025/03/17
@author: Maximilien Burq
"""

import pandas as pd


def map_peaks_modifications(peptide):
    return (
        peptide.replace("A(+42.01)", "Z")
        .replace("(+42.01)", "")  # Unclear why some n-term residues are acetylated here
        .replace("M(+15.99)", "M(ox)")
        .replace("C(+57.02)", "C")
    )


def remove_modifications(peptide):
    return (
        peptide.replace("(ox)", "")
        .replace("(de)", "")
        .replace("C(ca)", "C")
        .replace("Z", "")
        .replace("(ac)", "")
        .replace("(py)", "")
        .replace("(ph)", "")
        .replace("(tm)", "")
    )


def get_maxquant_peptides(filepath, files=None):
    maxquant_ids = pd.read_csv(
        filepath,
        usecols=[
            "Raw file",
            "Scan number",
            "Scan index",
            "Sequence",
            "Modified sequence",
            "Reverse",
        ],
        sep="\t",
    )
    # print(maxquant_ids.shape)
    # Remove decoys and filter only the raw files of interest
    if files is not None:
        maxquant_ids = maxquant_ids[maxquant_ids["Raw file"].isin(files)]
    maxquant_ids = maxquant_ids.query('Reverse != "+"').copy()
    maxquant_peptides = maxquant_ids.Sequence.str.replace("I", "L").unique()
    print(
        f"Found {len(maxquant_peptides)} peptides by maxquant from {len(maxquant_ids)} unique rows"
    )
    return maxquant_peptides


def get_fragpipe_peptides(filepath, files=None):
    fragpipe = pd.read_csv(filepath, sep="\t")

    fragpipe["is_decoy"] = fragpipe.Protein.apply(lambda x: "rev_" in x)
    fragpipe = fragpipe.query("~is_decoy").copy()
    fragpipe_peptides = fragpipe.Peptide.str.replace("I", "L").unique()
    print(
        f"Found {len(fragpipe_peptides)} peptides by fragpipe from {len(fragpipe)} unique rows"
    )
    return fragpipe_peptides


def get_peaks_peptides(filepath, files=None):
    df = pd.read_csv(filepath)
    df["peptide"] = df.Peptide.apply(map_peaks_modifications)
    df["clean_peptide"] = df.peptide.str.replace("I", "L").apply(remove_modifications)
    df_peptides = df.clean_peptide.unique()
    print(f"Found {len(df_peptides)} peptides by PEAKS from {len(df)} unique rows")
    return df_peptides


def get_pd_peptides(filepath, files=None):
    df = pd.read_excel(filepath)
    peptides = df.Sequence.str.replace("I", "L").unique()
    print(f"Found {len(peptides)} peptides by PD from {len(df)} unique rows")
    return peptides


def get_tesorai_peptides(filepath):
    tesorai = pd.read_csv(filepath)
    tesorai["clean_sequence"] = tesorai.clean_sequence.str.replace("I", "L").apply(
        remove_modifications
    )
    tesorai_peptides = tesorai.query("~is_decoy").clean_sequence.unique()
    print(f"Found {len(tesorai_peptides)} peptides by TS")
    return tesorai_peptides
