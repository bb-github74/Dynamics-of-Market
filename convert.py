# Author: bbaasan
# File: convert.py
# Created: 2024-06-01
# Email: bbaasan@gmu.edu
# Purpose: convert bib file to csv dataframe

import bibtexparser
from bibtexparser.bparser import BibTexParser
import csv

class Convert:
    def __init__(self, bibfile):
        self.bibfile = bibfile
        self.load_bibfile()

    def load_bibfile(self):
        with open(self.bibfile, mode='r', encoding='utf-8') as bib_file:
            parser = BibTexParser(common_strings=True)
            self.bib_database = bibtexparser.load(bib_file, parser=parser)

    def review_database(self):
        """ Returns a list of all entries in the bib database. """
        return self.bib_database.entries

    def clean_text(self, text):
        """ Clean up text data by replacing newlines and stripping excess whitespace. """
        return text.replace('\n', ' ').strip()

    def convert_to_csv(self, output_file):
        """ Converts the loaded BibTeX data to a CSV file with specified fields. """
        fieldnames = ['ID', 'entrytype', 'title', 'author', 'year', 'journal', 'volume', 'number', 'pages', 'month', 'note', 'publisher', 'address', 'abstract']
        with open(output_file, 'w', newline='', encoding='utf-8') as csv_file:
            writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
            writer.writeheader()
            for entry in self.bib_database.entries:
                # Normalize and clean data: Ensure all fieldnames exist and clean them
                csv_entry = {field: self.clean_text(entry.get(field, '')) for field in fieldnames}
                writer.writerow(csv_entry)

        print(f"Conversion complete. Data written to {output_file}")
