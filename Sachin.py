import requests
from bs4 import BeautifulSoup
import csv

url = "https://www.easyleadz.com/lists/List-of-Logistics-Companies-in-India"
response = requests.get(url)

if response.status_code == 200:
    soup = BeautifulSoup(response.content, 'html.parser')
    companies = soup.find_all('a', style="color:#50a1ff !important")

    data = []
    for company in companies:
        company_name = company.find('span', itemprop='name').text
        company_info = company.find_next('td', colspan='2').p.get_text(strip=True)
        employees_td = company.find_next('td', itemprop='numberOfEmployees')
        location_td = company.find_previous('td', itemprop='location')
        if location_td:
            location = location_td.text.strip().replace(":", "")
        else:
            location = "N/A"

        if employees_td:
            number_of_employees = employees_td.text.strip().replace(":", "")
        else:
            number_of_employees = "N/A"
        
        data.append([company_name, company_info, number_of_employees, location])

    # Column names
    columns = ["Company Name", "Company Info", "Number of Employees", "Location"]

    # Append data to CSV
    with open("Sachin_sharma_9034283082.csv", "a", newline="", encoding="utf-8") as file:
        csv_writer = csv.writer(file)
        if file.tell() == 0:  # Check if file is empty
            csv_writer.writerow(columns)
        csv_writer.writerows(data)

    print("Data appended to Sachin_Sharma.csv.")
else:
    print("Failed to fetch data from the website.")
