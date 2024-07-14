"""
File: webcrawler.py
Name: Vicky
--------------------------
This file collects more data from
https://www.ssa.gov/oact/babynames/decades/names2010s.html
https://www.ssa.gov/oact/babynames/decades/names2000s.html
https://www.ssa.gov/oact/babynames/decades/names1990s.html
Please print the number of top200 male and female on Console
You should see:
---------------------------
2010s
Male Number: 10905209
Female Number: 7949058
---------------------------
2000s
Male Number: 12979118
Female Number: 9210073
---------------------------
1990s
Male Number: 14146775
Female Number: 10644698
"""

import requests
from bs4 import BeautifulSoup


def main():
    for year in ['2010s', '2000s', '1990s']:
        print('---------------------------')
        print(year)
        url = 'https://www.ssa.gov/oact/babynames/decades/names'+year+'.html'
        response = requests.get(url)
        html = response.text
        # ----- Write your code below this line ----- #
        soup = BeautifulSoup(html, features='html.parser')
        tags = soup.find_all('tbody')
        male_total = 0
        female_total = 0
        for tag in tags:
            tds = tag.find_all('tr')
            for td in tds:
                token = td.get_text().split()
                if len(token) == 5:
                    male_number = int(token[2].replace(',', ''))
                    female_number = int(token[4].replace(',', ''))
                    male_total += male_number
                    female_total += female_number
            print('Male Number: ' + str(male_total))
            print('Female Number: ' + str(female_total))


if __name__ == '__main__':
    main()
