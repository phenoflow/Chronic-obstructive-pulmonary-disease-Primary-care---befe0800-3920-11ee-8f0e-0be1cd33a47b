# Eleanor L Axson, Jennifer K Quint, Mome Mukherjee, Hannah R Whittaker, Philip W Stone, Kate McLaren, 2023.

import sys, csv, re

codes = [{"code":"1484924013","system":"snomedct"},{"code":"1484971019","system":"snomedct"},{"code":"1780380013","system":"snomedct"},{"code":"1780381012","system":"snomedct"},{"code":"1856491000006119","system":"snomedct"},{"code":"1856501000006110","system":"snomedct"},{"code":"1856581000006118","system":"snomedct"},{"code":"1882371000006118","system":"snomedct"},{"code":"189761000000117","system":"snomedct"},{"code":"198471000000111","system":"snomedct"},{"code":"199481000000116","system":"snomedct"},{"code":"2308511000000113","system":"snomedct"},{"code":"2423731000000115","system":"snomedct"},{"code":"940131000006118","system":"snomedct"},{"code":"940141000006111","system":"snomedct"},{"code":"940151000006113","system":"snomedct"},{"code":"940161000006110","system":"snomedct"},{"code":"967531000006119","system":"snomedct"},{"code":"967571000006116","system":"snomedct"},{"code":"1484924013","system":"snomedct"},{"code":"1484971019","system":"snomedct"},{"code":"1780380013","system":"snomedct"},{"code":"1780381012","system":"snomedct"},{"code":"1856491000006119","system":"snomedct"},{"code":"1856501000006110","system":"snomedct"},{"code":"1856581000006118","system":"snomedct"},{"code":"1882371000006118","system":"snomedct"},{"code":"189761000000117","system":"snomedct"},{"code":"198471000000111","system":"snomedct"},{"code":"199481000000116","system":"snomedct"},{"code":"2308511000000113","system":"snomedct"},{"code":"2423731000000115","system":"snomedct"},{"code":"940131000006118","system":"snomedct"},{"code":"940141000006111","system":"snomedct"},{"code":"940151000006113","system":"snomedct"},{"code":"940161000006110","system":"snomedct"},{"code":"967531000006119","system":"snomedct"},{"code":"967571000006116","system":"snomedct"},{"code":"66YB.00","system":"readv2"},{"code":"66YB200","system":"readv2"},{"code":"66YD.00","system":"readv2"},{"code":"66YS.00","system":"readv2"},{"code":"66YT.00","system":"readv2"},{"code":"9Oi..00","system":"readv2"},{"code":"9Oi0.00","system":"readv2"},{"code":"9Oi1.00","system":"readv2"},{"code":"9Oi2.00","system":"readv2"},{"code":"9Oi3.00","system":"readv2"},{"code":"66YB.00","system":"readv2"},{"code":"66YB200","system":"readv2"},{"code":"66YD.00","system":"readv2"},{"code":"66YS.00","system":"readv2"},{"code":"66YT.00","system":"readv2"},{"code":"9Oi..00","system":"readv2"},{"code":"9Oi0.00","system":"readv2"},{"code":"9Oi1.00","system":"readv2"},{"code":"9Oi2.00","system":"readv2"},{"code":"9Oi3.00","system":"readv2"}];
REQUIRED_CODES = 1;
with open(sys.argv[1], 'r') as file_in, open('chronic-obstructive-pulmonary-disease-primary-care-potential-cases.csv', 'w', newline='') as file_out:
    csv_reader = csv.DictReader(file_in)
    csv_writer = csv.DictWriter(file_out, csv_reader.fieldnames + ["chronic-obstructive-pulmonary-disease-copd-primary-care-monitor---primary-identified"])
    csv_writer.writeheader();
    codes_identified = 0;
    for row in csv_reader:
        newRow = row.copy();
        for cell in row:
            # Iterate cell lists (e.g. codes)
            for item in re.findall(r'\(([^,]*)\,', row[cell]):
                if(item in list(map(lambda code: code['code'], codes))): codes_identified+=1;
                if(codes_identified>=REQUIRED_CODES):
                    newRow["chronic-obstructive-pulmonary-disease-copd-primary-care-monitor---primary-identified"] = "CASE";
                    break;
            if(codes_identified>=REQUIRED_CODES): break;
        if(codes_identified<REQUIRED_CODES):
            newRow["chronic-obstructive-pulmonary-disease-copd-primary-care-monitor---primary-identified"] = "UNK";
        codes_identified=0;
        csv_writer.writerow(newRow)
