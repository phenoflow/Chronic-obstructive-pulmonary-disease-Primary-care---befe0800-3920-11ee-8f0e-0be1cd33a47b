# Eleanor L Axson, Jennifer K Quint, Mome Mukherjee, Hannah R Whittaker, Philip W Stone, Kate McLaren, 2023.

import sys, csv, re

codes = [{"code":"1222335015","system":"snomedct"},{"code":"161781000006116","system":"snomedct"},{"code":"1724351000006112","system":"snomedct"},{"code":"1856571000006116","system":"snomedct"},{"code":"2152091000000112","system":"snomedct"},{"code":"2716231000006114","system":"snomedct"},{"code":"2716351000006113","system":"snomedct"},{"code":"457168017","system":"snomedct"},{"code":"909711000006111","system":"snomedct"},{"code":"1222335015","system":"snomedct"},{"code":"2716231000006114","system":"snomedct"},{"code":"2716351000006113","system":"snomedct"},{"code":"457168017","system":"snomedct"},{"code":"909711000006111","system":"snomedct"},{"code":"H3...","system":"ctv3"},{"code":"H32yz","system":"ctv3"},{"code":"X101k","system":"ctv3"},{"code":"XaEIV","system":"ctv3"},{"code":"XaEIW","system":"ctv3"},{"code":"XaIes","system":"ctv3"},{"code":"XaK8Q","system":"ctv3"},{"code":"XaLqj","system":"ctv3"},{"code":"XaPZH","system":"ctv3"},{"code":"XaW9D","system":"ctv3"},{"code":"XaY05","system":"ctv3"},{"code":"XaY0w","system":"ctv3"},{"code":"XaZ8t","system":"ctv3"},{"code":"XaZoz","system":"ctv3"},{"code":"Xac33","system":"ctv3"},{"code":"14B3.12","system":"readv2"},{"code":"1J71.00","system":"readv2"},{"code":"2126F00","system":"readv2"},{"code":"8CMV.00","system":"readv2"},{"code":"8Hkw.00","system":"readv2"},{"code":"9e03.00","system":"readv2"},{"code":"H310100","system":"readv2"},{"code":"H31y000","system":"readv2"},{"code":"H320311","system":"readv2"},{"code":"H32yz11","system":"readv2"},{"code":"H36..00","system":"readv2"},{"code":"H3z..11","system":"readv2"},{"code":"H36..00","system":"readv2"},{"code":"H3z..11","system":"readv2"}];
REQUIRED_CODES = 1;
with open(sys.argv[1], 'r') as file_in, open('chronic-obstructive-pulmonary-disease-primary-care-potential-cases.csv', 'w', newline='') as file_out:
    csv_reader = csv.DictReader(file_in)
    csv_writer = csv.DictWriter(file_out, csv_reader.fieldnames + ["chronic-obstructive-pulmonary-disease-copd-primary-care---primary-identified"])
    csv_writer.writeheader();
    codes_identified = 0;
    for row in csv_reader:
        newRow = row.copy();
        for cell in row:
            # Iterate cell lists (e.g. codes)
            for item in re.findall(r'\(([^,]*)\,', row[cell]):
                if(item in list(map(lambda code: code['code'], codes))): codes_identified+=1;
                if(codes_identified>=REQUIRED_CODES):
                    newRow["chronic-obstructive-pulmonary-disease-copd-primary-care---primary-identified"] = "CASE";
                    break;
            if(codes_identified>=REQUIRED_CODES): break;
        if(codes_identified<REQUIRED_CODES):
            newRow["chronic-obstructive-pulmonary-disease-copd-primary-care---primary-identified"] = "UNK";
        codes_identified=0;
        csv_writer.writerow(newRow)
