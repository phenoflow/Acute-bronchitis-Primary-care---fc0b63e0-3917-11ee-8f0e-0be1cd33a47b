# Eleftheria Vasileiou, Chukwuma Iwundu, Alex Williams, Clare MacRae, 2023.

import sys, csv, re

codes = [{"code":"H060C","system":"ctv3"},{"code":"H060D","system":"ctv3"},{"code":"H060F","system":"ctv3"},{"code":"H060C","system":"ctv3"},{"code":"H060D","system":"ctv3"},{"code":"H060F","system":"ctv3"},{"code":"456001000006113","system":"snomedct"},{"code":"4780521000006116","system":"snomedct"},{"code":"4780541000006111","system":"snomedct"},{"code":"456001000006113","system":"snomedct"},{"code":"4780521000006116","system":"snomedct"},{"code":"4780541000006111","system":"snomedct"},{"code":"H060C00","system":"readv2"},{"code":"H060D00","system":"readv2"},{"code":"H060F00","system":"readv2"},{"code":"H060C00","system":"readv2"},{"code":"H060D00","system":"readv2"},{"code":"H060F00","system":"readv2"}];
REQUIRED_CODES = 1;
with open(sys.argv[1], 'r') as file_in, open('acute-bronchitis-primary-care-potential-cases.csv', 'w', newline='') as file_out:
    csv_reader = csv.DictReader(file_in)
    csv_writer = csv.DictWriter(file_out, csv_reader.fieldnames + ["acute-bronchitis-primary-care-echovirus---primary-identified"])
    csv_writer.writeheader();
    codes_identified = 0;
    for row in csv_reader:
        newRow = row.copy();
        for cell in row:
            # Iterate cell lists (e.g. codes)
            for item in re.findall(r'\(([^,]*)\,', row[cell]):
                if(item in list(map(lambda code: code['code'], codes))): codes_identified+=1;
                if(codes_identified>=REQUIRED_CODES):
                    newRow["acute-bronchitis-primary-care-echovirus---primary-identified"] = "CASE";
                    break;
            if(codes_identified>=REQUIRED_CODES): break;
        if(codes_identified<REQUIRED_CODES):
            newRow["acute-bronchitis-primary-care-echovirus---primary-identified"] = "UNK";
        codes_identified=0;
        csv_writer.writerow(newRow)
