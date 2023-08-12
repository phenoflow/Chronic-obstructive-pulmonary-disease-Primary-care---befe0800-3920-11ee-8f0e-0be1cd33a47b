# Eleanor L Axson, Jennifer K Quint, Mome Mukherjee, Hannah R Whittaker, Philip W Stone, Kate McLaren, 2023.

import sys, csv, re

codes = [{"code":"105519017","system":"snomedct"},{"code":"2240631000000119","system":"snomedct"},{"code":"285104011","system":"snomedct"},{"code":"301450011","system":"snomedct"},{"code":"301455018","system":"snomedct"},{"code":"301457014","system":"snomedct"},{"code":"301458016","system":"snomedct"},{"code":"301459012","system":"snomedct"},{"code":"4733001000006118","system":"snomedct"},{"code":"4733011000006115","system":"snomedct"},{"code":"4733021000006111","system":"snomedct"},{"code":"4733031000006114","system":"snomedct"},{"code":"851261000006116","system":"snomedct"},{"code":"907481000006118","system":"snomedct"},{"code":"No found code","system":"snomedct"},{"code":"105519017","system":"snomedct"},{"code":"285104011","system":"snomedct"},{"code":"301455018","system":"snomedct"},{"code":"301457014","system":"snomedct"},{"code":"301458016","system":"snomedct"},{"code":"301459012","system":"snomedct"},{"code":"4733001000006118","system":"snomedct"},{"code":"4733011000006115","system":"snomedct"},{"code":"4733021000006111","system":"snomedct"},{"code":"4733031000006114","system":"snomedct"},{"code":"851261000006116","system":"snomedct"},{"code":"14B3.11","system":"readv2"},{"code":"H30..12","system":"readv2"},{"code":"H302.00","system":"readv2"},{"code":"H30z.00","system":"readv2"},{"code":"H31..00","system":"readv2"},{"code":"H310.00","system":"readv2"},{"code":"H310000","system":"readv2"},{"code":"H310z00","system":"readv2"},{"code":"H311.00","system":"readv2"},{"code":"H311000","system":"readv2"},{"code":"H311100","system":"readv2"},{"code":"H311z00","system":"readv2"},{"code":"H312.00","system":"readv2"},{"code":"H312000","system":"readv2"},{"code":"H312011","system":"readv2"},{"code":"H312100","system":"readv2"},{"code":"H312300","system":"readv2"},{"code":"H312z00","system":"readv2"},{"code":"H313.00","system":"readv2"},{"code":"H31y.00","system":"readv2"},{"code":"H31yz00","system":"readv2"},{"code":"H31z.00","system":"readv2"},{"code":"H583200","system":"readv2"},{"code":"H30z.00","system":"readv2"},{"code":"H31..00","system":"readv2"},{"code":"H310.00","system":"readv2"},{"code":"H310z00","system":"readv2"},{"code":"H311.00","system":"readv2"},{"code":"H311z00","system":"readv2"},{"code":"H312.00","system":"readv2"},{"code":"H312100","system":"readv2"},{"code":"H312z00","system":"readv2"},{"code":"H31z.00","system":"readv2"}];
REQUIRED_CODES = 1;
with open(sys.argv[1], 'r') as file_in, open('chronic-obstructive-pulmonary-disease-primary-care-potential-cases.csv', 'w', newline='') as file_out:
    csv_reader = csv.DictReader(file_in)
    csv_writer = csv.DictWriter(file_out, csv_reader.fieldnames + ["chronic-obstructive-pulmonary-disease-copd-primary-care-bronchiolitis---primary-identified"])
    csv_writer.writeheader();
    codes_identified = 0;
    for row in csv_reader:
        newRow = row.copy();
        for cell in row:
            # Iterate cell lists (e.g. codes)
            for item in re.findall(r'\(([^,]*)\,', row[cell]):
                if(item in list(map(lambda code: code['code'], codes))): codes_identified+=1;
                if(codes_identified>=REQUIRED_CODES):
                    newRow["chronic-obstructive-pulmonary-disease-copd-primary-care-bronchiolitis---primary-identified"] = "CASE";
                    break;
            if(codes_identified>=REQUIRED_CODES): break;
        if(codes_identified<REQUIRED_CODES):
            newRow["chronic-obstructive-pulmonary-disease-copd-primary-care-bronchiolitis---primary-identified"] = "UNK";
        codes_identified=0;
        csv_writer.writerow(newRow)
