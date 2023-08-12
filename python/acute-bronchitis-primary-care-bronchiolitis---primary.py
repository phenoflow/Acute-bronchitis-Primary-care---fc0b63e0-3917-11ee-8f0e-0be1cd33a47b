# Eleftheria Vasileiou, Chukwuma Iwundu, Alex Williams, Clare MacRae, 2023.

import sys, csv, re

codes = [{"code":"H06..","system":"ctv3"},{"code":"H060.","system":"ctv3"},{"code":"H060z","system":"ctv3"},{"code":"H06z.","system":"ctv3"},{"code":"XE0Xr","system":"ctv3"},{"code":"H06..","system":"ctv3"},{"code":"H060.","system":"ctv3"},{"code":"H060z","system":"ctv3"},{"code":"H06z.","system":"ctv3"},{"code":"XE0Xr","system":"ctv3"},{"code":"12717061000006114","system":"snomedct"},{"code":"18268014","system":"snomedct"},{"code":"301095014","system":"snomedct"},{"code":"301122016","system":"snomedct"},{"code":"301132011","system":"snomedct"},{"code":"411057014","system":"snomedct"},{"code":"411520013","system":"snomedct"},{"code":"885041000006119","system":"snomedct"},{"code":"907481000006118","system":"snomedct"},{"code":"12717061000006114","system":"snomedct"},{"code":"18268014","system":"snomedct"},{"code":"301095014","system":"snomedct"},{"code":"301122016","system":"snomedct"},{"code":"301132011","system":"snomedct"},{"code":"411520013","system":"snomedct"},{"code":"885041000006119","system":"snomedct"},{"code":"907481000006118","system":"snomedct"},{"code":"12D1.11","system":"readv2"},{"code":"14B3.11","system":"readv2"},{"code":"H06..00","system":"readv2"},{"code":"H06..99","system":"readv2"},{"code":"H060.00","system":"readv2"},{"code":"H060z00","system":"readv2"},{"code":"H06z.00","system":"readv2"},{"code":"14B3.11","system":"readv2"},{"code":"H06..00","system":"readv2"},{"code":"H06..99","system":"readv2"},{"code":"H060.00","system":"readv2"},{"code":"H060z00","system":"readv2"},{"code":"H06z.00","system":"readv2"}];
REQUIRED_CODES = 1;
with open(sys.argv[1], 'r') as file_in, open('acute-bronchitis-primary-care-potential-cases.csv', 'w', newline='') as file_out:
    csv_reader = csv.DictReader(file_in)
    csv_writer = csv.DictWriter(file_out, csv_reader.fieldnames + ["acute-bronchitis-primary-care-bronchiolitis---primary-identified"])
    csv_writer.writeheader();
    codes_identified = 0;
    for row in csv_reader:
        newRow = row.copy();
        for cell in row:
            # Iterate cell lists (e.g. codes)
            for item in re.findall(r'\(([^,]*)\,', row[cell]):
                if(item in list(map(lambda code: code['code'], codes))): codes_identified+=1;
                if(codes_identified>=REQUIRED_CODES):
                    newRow["acute-bronchitis-primary-care-bronchiolitis---primary-identified"] = "CASE";
                    break;
            if(codes_identified>=REQUIRED_CODES): break;
        if(codes_identified<REQUIRED_CODES):
            newRow["acute-bronchitis-primary-care-bronchiolitis---primary-identified"] = "UNK";
        codes_identified=0;
        csv_writer.writerow(newRow)
