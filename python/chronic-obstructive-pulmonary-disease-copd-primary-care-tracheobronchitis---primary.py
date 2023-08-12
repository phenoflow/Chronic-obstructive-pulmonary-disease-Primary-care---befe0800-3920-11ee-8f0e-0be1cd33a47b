# Eleanor L Axson, Jennifer K Quint, Mome Mukherjee, Hannah R Whittaker, Philip W Stone, Kate McLaren, 2023.

import sys, csv, re

codes = [{"code":"H31..","system":"ctv3"},{"code":"H310.","system":"ctv3"},{"code":"H3100","system":"ctv3"},{"code":"H310z","system":"ctv3"},{"code":"H311.","system":"ctv3"},{"code":"H3110","system":"ctv3"},{"code":"H311z","system":"ctv3"},{"code":"H3120","system":"ctv3"},{"code":"H3121","system":"ctv3"},{"code":"H312z","system":"ctv3"},{"code":"H313.","system":"ctv3"},{"code":"H31y.","system":"ctv3"},{"code":"H31y1","system":"ctv3"},{"code":"H31yz","system":"ctv3"},{"code":"H31z.","system":"ctv3"},{"code":"X101j","system":"ctv3"},{"code":"XE0YM","system":"ctv3"},{"code":"XE0ZN","system":"ctv3"},{"code":"Xaa7C","system":"ctv3"},{"code":"H300.00","system":"readv2"},{"code":"H301.00","system":"readv2"},{"code":"H31y100","system":"readv2"}];
REQUIRED_CODES = 1;
with open(sys.argv[1], 'r') as file_in, open('chronic-obstructive-pulmonary-disease-primary-care-potential-cases.csv', 'w', newline='') as file_out:
    csv_reader = csv.DictReader(file_in)
    csv_writer = csv.DictWriter(file_out, csv_reader.fieldnames + ["chronic-obstructive-pulmonary-disease-copd-primary-care-tracheobronchitis---primary-identified"])
    csv_writer.writeheader();
    codes_identified = 0;
    for row in csv_reader:
        newRow = row.copy();
        for cell in row:
            # Iterate cell lists (e.g. codes)
            for item in re.findall(r'\(([^,]*)\,', row[cell]):
                if(item in list(map(lambda code: code['code'], codes))): codes_identified+=1;
                if(codes_identified>=REQUIRED_CODES):
                    newRow["chronic-obstructive-pulmonary-disease-copd-primary-care-tracheobronchitis---primary-identified"] = "CASE";
                    break;
            if(codes_identified>=REQUIRED_CODES): break;
        if(codes_identified<REQUIRED_CODES):
            newRow["chronic-obstructive-pulmonary-disease-copd-primary-care-tracheobronchitis---primary-identified"] = "UNK";
        codes_identified=0;
        csv_writer.writerow(newRow)
