#!/usr/bin/env python

__author__ = "Samo Turk"
__copyright__ = "Copyright (C) 2014 by BioMed X GmbH"
__credits__ = ["Simone Fulle", "Katra Kolsek"]
__license__ = "GPL"
__version__ = "0.1"
__email__ = "turk@bio.mx"
__status__ = "Development"

import argparse
import sys
import os
import pybel

def gen3D(mol, pH=7.4, forcefield="MMFF94", s1=10, s2=500):
    """
    Add protons for certain pH and generates 3D conformation and minimizes molecule
    - pH: defaults to 7.4
    - forcefield: options - MMFF94, UFF or Ghemical, defaults to MMFF94
    - s1: how many steps for make3D, defaults to 10
    - s2: how many steps for localopt, defaults to 500
    """
    mol.OBMol.AddHydrogens(False, True, pH)
    mol.make3D(forcefield=forcefield, steps=s1)
    mol.localopt(forcefield=forcefield, steps=s2)
    return mol

def arg_parser():
    parser = argparse.ArgumentParser(description='Generate 3D structures of molecules.')
    parser.add_argument('-i', '--infile', help="Specifies input file")
    parser.add_argument('-o', '--outfile', help="Specifies output file")
    parser.add_argument('-p', '--ph', default=7.4, help="Specifies pH for hydrogen addition")
    parser.add_argument('-f', '--forcefield', default='MMFF94', help="Specifies forcefield. MMFF94, UFF or Ghemical, defaults to MMFF94")
    parser.add_argument('-s1', '--steps1', default=10, help="Specifies how many steps for make3D, defaults to 10")
    parser.add_argument('-s2', '--steps2', default=500, help="Specifies how many steps for localopt, defaults to 500")
    
    return parser

if __name__ == "__main__":
    parser = arg_parser()
    if len(sys.argv) == 1:
        argv = ['-h']
    else:
        argv = sys.argv[1:]
    args = parser.parse_args(argv)
    
    informat = args.infile.split(".")[-1]
    outformat = args.outfile.split(".")[-1]
    
    # Limit acceptable in and out formats
    informats = ['smi', 'ism', 'sdf', 'mol2', 'mol', 'pdb']
    outformats = ['mol2', 'sdf', 'pdbqt']
    
    
    if informat in informats and outformat in outformats:
        mols = pybel.readfile(informat, args.infile)
        numMols = 0
        for mol in mols:
            numMols += 1
        mols = pybel.readfile(informat, args.infile)
        os.system('cls' if os.name == 'nt' else 'clear') # Clear the terminal
        molsdetected = str(numMols) + " molecules detected."
        print(molsdetected)
        i = 1
        output = pybel.Outputfile(outformat, args.outfile, overwrite=True)
        for mol in mols:
            mol = gen3D(mol, pH=float(args.ph), forcefield=args.forcefield, s1=int(args.steps1), s2=int(args.steps2))
            os.system('cls' if os.name == 'nt' else 'clear')
            print(molsdetected)
            print("Processing molecule titled: " + str(mol.title))
            output.write(mol)
            print(str(i) + " out of " + str(numMols))
            i += 1
        output.close()
    else:
        print("Format either of infile or outfile not recognized!\nSupported formats are: " + " ".join(list(set(informats+outformats))))
    