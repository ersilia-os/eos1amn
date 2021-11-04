import sys
import csv
import json
import numpy as np

NBITS = 2048

infile = sys.argv[1]
outfile = sys.argv[2]

smiles = []
with open(infile, "r") as f:
    reader = csv.reader(f)
    next(reader)
    for r in reader:
        smiles += [r[0]]

from pmapper.pharmacophore import Pharmacophore as P
from rdkit import Chem
from rdkit.Chem import AllChem

R = []
for smi in smiles:
    mol = Chem.MolFromSmiles(smi)
    mol = Chem.AddHs(mol)
    AllChem.EmbedMolecule(mol, randomSeed=42)
    p = P()
    p.load_from_mol(mol)
    fp_ = p.get_fp(nbits=NBITS)
    fp = np.zeros(NBITS, np.int8)
    for i in fp_:
        fp[i] = 1
    R += [{"fp": [int(x) for x in fp]}]

with open(outfile, "w") as f:
    json.dump(R, f)
