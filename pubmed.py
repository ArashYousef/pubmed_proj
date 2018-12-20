from Bio import Entrez
from Bio import Medline
import time
Entrez.email = "yousefa@colorado.edu"

search_results = Entrez.read(Entrez.esearch(db="pubmed", term = "Garcea, Robert[FAU]"))

idList = search_results["IdList"]

count = int(search_results["Count"])
print("Found %i results" % count)
out_handle = open("test.txt", "w")

for i in range(0, count):
    print("Downloading record %i of %i" % (i+1, count))
    fetch_handle = Entrez.efetch(db = "pubmed", id = idList, rettype = "medline", retmode = "text")

    data = fetch_handle.read()
    fetch_handle.close()
    out_handle.write(data)
out_handle.close()
