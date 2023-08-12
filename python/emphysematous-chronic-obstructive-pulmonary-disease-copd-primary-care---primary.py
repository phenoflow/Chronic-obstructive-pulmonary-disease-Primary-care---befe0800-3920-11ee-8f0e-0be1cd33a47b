# Eleanor L Axson, Jennifer K Quint, Mome Mukherjee, Hannah R Whittaker, Philip W Stone, Kate McLaren, 2023.

import sys, csv, re

codes = [{"code":"12704691000006117","system":"snomedct"},{"code":"19421011","system":"snomedct"},{"code":"2578911000006118","system":"snomedct"},{"code":"27096010","system":"snomedct"},{"code":"285100019","system":"snomedct"},{"code":"301460019","system":"snomedct"},{"code":"301468014","system":"snomedct"},{"code":"301469018","system":"snomedct"},{"code":"301477019","system":"snomedct"},{"code":"301572010","system":"snomedct"},{"code":"301835010","system":"snomedct"},{"code":"3611791000006110","system":"snomedct"},{"code":"3764021000006117","system":"snomedct"},{"code":"3764031000006119","system":"snomedct"},{"code":"3921361000006112","system":"snomedct"},{"code":"396109014","system":"snomedct"},{"code":"396110016","system":"snomedct"},{"code":"457581000006111","system":"snomedct"},{"code":"4732991000006119","system":"snomedct"},{"code":"4781471000006112","system":"snomedct"},{"code":"4781821000006113","system":"snomedct"},{"code":"640491000006111","system":"snomedct"},{"code":"909721000006115","system":"snomedct"},{"code":"285100019","system":"snomedct"},{"code":"301460019","system":"snomedct"},{"code":"301468014","system":"snomedct"},{"code":"301469018","system":"snomedct"},{"code":"301835010","system":"snomedct"},{"code":"3921361000006112","system":"snomedct"},{"code":"396110016","system":"snomedct"},{"code":"4732991000006119","system":"snomedct"},{"code":"4781471000006112","system":"snomedct"},{"code":"640491000006111","system":"snomedct"},{"code":"909721000006115","system":"snomedct"},{"code":"No found code","system":"snomedct"},{"code":"H32..00","system":"readv2"},{"code":"H320.00","system":"readv2"},{"code":"H320200","system":"readv2"},{"code":"H320z00","system":"readv2"},{"code":"H32y.00","system":"readv2"},{"code":"H32y000","system":"readv2"},{"code":"H32y100","system":"readv2"},{"code":"H32y200","system":"readv2"},{"code":"H32yz00","system":"readv2"},{"code":"H32z.00","system":"readv2"},{"code":"Hyu3000","system":"readv2"},{"code":"H32..00","system":"readv2"},{"code":"H320.00","system":"readv2"},{"code":"H320z00","system":"readv2"},{"code":"H32y.00","system":"readv2"},{"code":"H32z.00","system":"readv2"}];
REQUIRED_CODES = 1;
with open(sys.argv[1], 'r') as file_in, open('chronic-obstructive-pulmonary-disease-primary-care-potential-cases.csv', 'w', newline='') as file_out:
    csv_reader = csv.DictReader(file_in)
    csv_writer = csv.DictWriter(file_out, csv_reader.fieldnames + ["emphysematous-chronic-obstructive-pulmonary-disease-copd-primary-care---primary-identified"])
    csv_writer.writeheader();
    codes_identified = 0;
    for row in csv_reader:
        newRow = row.copy();
        for cell in row:
            # Iterate cell lists (e.g. codes)
            for item in re.findall(r'\(([^,]*)\,', row[cell]):
                if(item in list(map(lambda code: code['code'], codes))): codes_identified+=1;
                if(codes_identified>=REQUIRED_CODES):
                    newRow["emphysematous-chronic-obstructive-pulmonary-disease-copd-primary-care---primary-identified"] = "CASE";
                    break;
            if(codes_identified>=REQUIRED_CODES): break;
        if(codes_identified<REQUIRED_CODES):
            newRow["emphysematous-chronic-obstructive-pulmonary-disease-copd-primary-care---primary-identified"] = "UNK";
        codes_identified=0;
        csv_writer.writerow(newRow)
