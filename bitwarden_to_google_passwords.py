#!/usr/local/bin/python3

import sys, getopt, csv

def main(argv):
    inputfile = ''
    outputfile = ''
    try:
        opts, args = getopt.getopt(argv,"hi:o:",["ifile=","ofile="])
    except getopt.GetoptError:
        print ('test.py -i <inputfile> -o <outputfile>')
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            print ('test.py -i <inputfile> -o <outputfile>')
            sys.exit()
        elif opt in ("-i", "--ifile"):
            inputfile = arg
        elif opt in ("-o", "--ofile"):
            outputfile = arg
    print ('Input file is "', inputfile)
    print ('Output file is "', outputfile)

    with open ("chrome_passwords.csv", 'w', newline = '') as google_csv:
        google_writer = csv.writer (google_csv, delimiter = ',', quoting=csv.QUOTE_MINIMAL)
        google_writer.writerow (['name', 'url', 'username', 'password'])
        with open (inputfile, newline = '') as bitwarden_csv:
            bitwarden_reader = csv.reader(bitwarden_csv, delimiter = ',')
            for row in bitwarden_reader:
                if (row[2] == 'login'):
                    google_writer.writerow ([row[3], row[6], row[7], row[8]])



if __name__ == "__main__":
   main(sys.argv[1:])