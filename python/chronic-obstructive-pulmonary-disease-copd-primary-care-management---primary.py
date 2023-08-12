# Eleanor L Axson, Jennifer K Quint, Mome Mukherjee, Hannah R Whittaker, Philip W Stone, Kate McLaren, 2023.

import sys, csv, re

codes = [{"code":"1811661000006110","system":"snomedct"},{"code":"1811741000006117","system":"snomedct"},{"code":"1885981000006112","system":"snomedct"},{"code":"2009511000006113","system":"snomedct"},{"code":"839001000006111","system":"snomedct"},{"code":"966841000006111","system":"snomedct"},{"code":"XaIUt","system":"ctv3"},{"code":"XaJYf","system":"ctv3"},{"code":"XaYZO","system":"ctv3"},{"code":"XaYbA","system":"ctv3"},{"code":"661M300","system":"readv2"},{"code":"661N300","system":"readv2"},{"code":"66YI.00","system":"readv2"},{"code":"8IEy.00","system":"readv2"},{"code":"661M300","system":"readv2"},{"code":"661N300","system":"readv2"},{"code":"66YI.00","system":"readv2"}];
REQUIRED_CODES = 1;
with open(sys.argv[1], 'r') as file_in, open('chronic-obstructive-pulmonary-disease-primary-care-potential-cases.csv', 'w', newline='') as file_out:
    csv_reader = csv.DictReader(file_in)
    csv_writer = csv.DictWriter(file_out, csv_reader.fieldnames + ["chronic-obstructive-pulmonary-disease-copd-primary-care-management---primary-identified"])
    csv_writer.writeheader();
    codes_identified = 0;
    for row in csv_reader:
        newRow = row.copy();
        for cell in row:
            # Iterate cell lists (e.g. codes)
            for item in re.findall(r'\(([^,]*)\,', row[cell]):
                if(item in list(map(lambda code: code['code'], codes))): codes_identified+=1;
                if(codes_identified>=REQUIRED_CODES):
                    newRow["chronic-obstructive-pulmonary-disease-copd-primary-care-management---primary-identified"] = "CASE";
                    break;
            if(codes_identified>=REQUIRED_CODES): break;
        if(codes_identified<REQUIRED_CODES):
            newRow["chronic-obstructive-pulmonary-disease-copd-primary-care-management---primary-identified"] = "UNK";
        codes_identified=0;
        csv_writer.writerow(newRow)
