from Bio import Entrez
from Bio import Medline
import time
Entrez.email = "yousefa@colorado.edu"
with open("test.txt") as handle:
    for record in Medline.parse(handle):
        print(record["TI"])
        print("\n")
        print(record["FAU"])
        print("\n")
        if(record["AB"]):
            print(record["AB"])
            print("\n")
            print("\n")
            print("\n")
        else:
            print("\n")
            print("\n")
            print("\n")
