import string

from bs4 import BeautifulSoup
import requests


alphabet = list(string.ascii_lowercase)


with open("ISO 693-3 codes.tsv", "w") as fout:
    for letter in alphabet:
        r = requests.get(f"https://en.wikipedia.org/wiki/ISO_639:{letter}")

        data = r.text
        parsed_html = BeautifulSoup(data, "html.parser")

        table = parsed_html.body.find("tbody")
        rows = table.findAll("tr")

        for row in rows:

            ret = []

            codecell = row.findAll("th")
            cells = row.findAll("td")

            if len(codecell) > 1:
                continue

            ret.append(codecell[0].text.strip())

            for cell in cells:
                content = cell.text
                ret.append(content.strip())

            print("\t".join(ret), file=fout)