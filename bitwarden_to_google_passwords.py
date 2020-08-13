#!/usr/local/bin/python3

import sys, csv

def main(argv):
    inputfile = ''
    i = len(sys.argv)
    if ((i == 1) or (i > 2)):
        print ("Usage: bitwarden_to_google_passwords.py <bitwarden csv file>")
        exit()
    else:
        inputfile = str (sys.argv[1])
    
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