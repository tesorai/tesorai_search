# tesorai_search
Generate results for Tesorai Search publication

## 1. System Requirements

The code in this repository is meant to analyze results from the Tesorai Search platform, accessible at console.tesorai.com.

It was run with Python version 3.11.4. Requirements are listed in requirements.txt

## 2. Installation Guide

To install the dependencies, run the following command:
```
pip install -r requirements.txt
```

Typical installation time is 1-2 minutes.

## 3. Demo

### 3.1. Set up an account on console.tesorai.com

Follow the guide on https://docs.tesorai.com/docs/console/getting-started/ to create an account.

### 3.2. [Optional] Download the data from PRIDE and run the search

- Download 190416_FPTMT_MS3_HCDOT_R1 from https://www.ebi.ac.uk/pride/archive/projects/PXD030340. 

- Download human FASTA dataset from Uniprot: https://www.uniprot.org/uniprotkb?query=homo+sapiens&facets=reviewed%3Atrue

- Upload the data to the console.tesorai.com platform.
- Run the search. Expected runtime is under 1 hour.
- Download the peptides.tsv file to the `data` folder.
- Run the notebooks to generate the figures and tables.

### 3.3. Download other tools' data from mendeley

The processed data that was used for benchmarking purposes (FragPipe, PEAKS, Prosit, MaxQuant), is available [here](https://data.mendeley.com/datasets/znkr2dm8fb/1): 
Burq, Maximilien; Stepec, Dejan (2025), “Tesorai Search”, Mendeley Data, V1, doi: 10.17632/znkr2dm8fb.1

To run the notebooks, you need to download the data from mendeley and put it in the `data` folder.

### 3.4. Run the notebooks

Each notebook is self-contained and can be run independently. They correspond to individual figures and tables in the manuscript.

## 4. Citation

If you use this code, or the Tesorai Platform in your research, please cite:

```
Back to Basics: Spectrum and Peptide Sequence are Sufficient for Top-tier Mass Spectrometry Proteomics Identification
Maximilien Burq, Dejan Stepec, Juan Restrepo, Jure Zbontar, Shamil Urazbakhtin, Bryan Crampton, Shivani Tiwary, Rehan Chinoy, Melissa Miao, Juergen Cox, Peter Cimermancic
```

## 5. License

This project is licensed under the MIT License. See the LICENSE file for details.