from Bio import Entrez
from Bio import Medline
import time
Entrez.email = "yousefa@colorado.edu"

name = ""

print("Choose faculty member:\n")
print("1: Natalie Ahn\n")
print("2: Kristi Anseth\n")
print("3: Stephanie Bryant\n")
print("4: Tom Cech\n")
print("5: Edward Chuong\n")
print("6: Aaron Clauset\n")
print("7: Robin Dowell\n")
print("8: Robert Garcea\n")
print("9: Loren Hough\n")
print("10: Joel Kralj\n")
print("11: Daniel Larremore\n")
print("12: Ryan Layer\n")
print("13: Leslie Leinwand\n")
print("14: Amy Palmer\n")
print("15: Orit Peleg\n")
print("16: John Rinn\n")
print("17: Sara Sawyer\n")

choice = input("Enter Corresponding Number:")
if choice == 1:
    name = "Natalie Ahn[FAU]"
elif choice == 2:
    name = "Kristi Anseth[FAU]"
elif choice == 3:
    name = "Stephanie Bryant[FAU]"
elif choice == 4:
    name = "Tom Cech[FAU]"
elif choice == 5:
    name = "Edward Chuong[FAU]"
elif choice == 6:
    name = "Aaron Clauset[FAU]"
elif choice == 7:
    name = "Robin Dowell[FAU]"
elif choice == 8:
    name = "Robert Garcea[FAU]"
elif choice == 9:
    name = "Loren Hough[FAU]"
elif choice == 10:
    name = "Joel Kralj[FAU]"
elif choice == 11:
    name = "Daniel Larremore[FAU]"
elif choice == 12:
    name = "Ryan Layer[FAU]"
elif choice == 13:
    name = "Leslie Leinwand[FAU]"
elif choice == 14:
    name = "Amy Palmer[FAU]"
elif choice == 15:
    name = "Orit Peleg[FAU]"
elif choice == 16:
    name = "John Rinn[FAU]"
elif choice == 17:
    name = "Sara Sawyer[FAU]"
else:
    "Not a valid input"

search_results = Entrez.read(Entrez.esearch(db="pubmed", term = name))

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

out_handle_final = open("output.xml", "w")

print("Writing records to XML please wait")
with open("test.txt") as trans_handle:
    for record in Medline.parse(trans_handle):
        title = record["TI"]
        print("\n")
        if "AB" in record:
            abstract = record["AB"]
        else:
            abstract = ""
        out_handle_final.write(title)
        out_handle_final.write("\n")
        out_handle_final.write(abstract)
        out_handle_final.write("\n")
        out_handle_final.write("\n")
out_handle_final.close()
