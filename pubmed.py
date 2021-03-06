from Bio import Entrez #Initialize Library
from Bio import Medline
import time
Entrez.email = "yousefa@colorado.edu" #Always tell biopython who you are

name = "" #User input for their choice of author

print("Choose faculty member:\n") #Display choices
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

choice = input("Enter Corresponding Number:\n") #Read user input and assign choice to name
if choice == 1:
    name = " Ahn, Natalie[FAU]"
elif choice == 2:
    name = "Anseth, Kristi[FAU]"
elif choice == 3:
    name = "Bryant, Stephanie[FAU]"
elif choice == 4:
    name = " Cech, Tom[FAU]"
elif choice == 5:
    name = "Chuong, Edward[FAU]"
elif choice == 6:
    name = "Clauset, Aaron[FAU]"
elif choice == 7:
    name = "Dowell, Robin[FAU]"
elif choice == 8:
    name = "Garcea, Robert[FAU]"
elif choice == 9:
    name = "Hough, Loren[FAU]"
elif choice == 10:
    name = "Kralj, Joel[FAU]"
elif choice == 11:
    name = "Larremore, Daniel[FAU]"
elif choice == 12:
    name = "Layer, Ryan[FAU]"
elif choice == 13:
    name = "Leinwand, Leslie[FAU]"
elif choice == 14:
    name = "Palmer, Amy[FAU]"
elif choice == 15:
    name = "Peleg, Orit[FAU]"
elif choice == 16:
    name = "Rinn, John[FAU]"
elif choice == 17:
    name = "Sawyer, Sara[FAU]"
else:
    "Not a valid input"

search_results = Entrez.read(Entrez.esearch(db="pubmed", term = name)) #Search PubMed data base for all corresponding search results

idList = search_results["IdList"] #Save search results into an ID List

count = int(search_results["Count"]) #Save total number of results into count
print("\nFound %i results" % count) #Print out how many results were found
out_handle = open("test.txt", "w") #Create test.txt to write results to


#The following loop fetches all the records stored in idList
#Writes fetched result into test.txt
for i in range(0, count):
    print("Downloading record %i of %i" % (i+1, count))
    fetch_handle = Entrez.efetch(db = "pubmed", id = idList, rettype = "medline", retmode = "text")

    data = fetch_handle.read()
    fetch_handle.close()
    out_handle.write(data)
out_handle.close()

out_handle_final = open("output.xml", "w") #Create output.xml for the final output

#The following function parses through test.txt and outputs the title and abstract of each record into output.xml
print("\nWriting records to XML please wait\n")
with open("test.txt") as trans_handle:
    for record in Medline.parse(trans_handle):
        title = record["TI"]
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

print("Finished\n")
