# Eleanor L Axson, Jennifer K Quint, Mome Mukherjee, Hannah R Whittaker, Philip W Stone, Kate McLaren, 2023.

import sys, csv, re

codes = [{"code":"1488423019","system":"snomedct"},{"code":"1494601017","system":"snomedct"},{"code":"1856591000006115","system":"snomedct"},{"code":"845451000006118","system":"snomedct"},{"code":"1488423019","system":"snomedct"},{"code":"1494601017","system":"snomedct"},{"code":"1856591000006115","system":"snomedct"},{"code":"845451000006118","system":"snomedct"},{"code":"66YL.00","system":"readv2"},{"code":"66YL.11","system":"readv2"},{"code":"66YL.12","system":"readv2"},{"code":"66YL.00","system":"readv2"},{"code":"66YL.11","system":"readv2"},{"code":"66YL.12","system":"readv2"}];
REQUIRED_CODES = 1;
with open(sys.argv[1], 'r') as file_in, open('chronic-obstructive-pulmonary-disease-primary-care-potential-cases.csv', 'w', newline='') as file_out:
    csv_reader = csv.DictReader(file_in)
    csv_writer = csv.DictWriter(file_out, csv_reader.fieldnames + ["chronic-obstructive-pulmonary-disease-copd-primary-care-followup---primary-identified"])
    csv_writer.writeheader();
    codes_identified = 0;
    for row in csv_reader:
        newRow = row.copy();
        for cell in row:
            # Iterate cell lists (e.g. codes)
            for item in re.findall(r'\(([^,]*)\,', row[cell]):
                if(item in list(map(lambda code: code['code'], codes))): codes_identified+=1;
                if(codes_identified>=REQUIRED_CODES):
                    newRow["chronic-obstructive-pulmonary-disease-copd-primary-care-followup---primary-identified"] = "CASE";
                    break;
            if(codes_identified>=REQUIRED_CODES): break;
        if(codes_identified<REQUIRED_CODES):
            newRow["chronic-obstructive-pulmonary-disease-copd-primary-care-followup---primary-identified"] = "UNK";
        codes_identified=0;
        csv_writer.writerow(newRow)
