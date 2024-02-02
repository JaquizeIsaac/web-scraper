import requests
from bs4 import BeautifulSoup

def get_citations_needed_count(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    citations_needed = soup.find_all('sup', class_='noprint Inline-Template Template-Fact')
    return len(citations_needed)

def get_citations_needed_report(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    citations_needed = soup.find_all('sup', class_='noprint Inline-Template Template-Fact')
    report = ""
    for citation in citations_needed:
        passage = citation.find_next('p').text.strip()
        report += f"{passage} [citation needed]\n"
    return report

def get_citations_needed_by_section(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    sections = soup.find_all(['h1', 'h2', 'h3', 'h4', 'h5', 'h6'])
    citations_by_section = {}
    for section in sections:
        section_name = section.text.strip()
        citations = section.find_all('sup', class_='noprint Inline-Template Template-Fact')
        citations_list = [citation.find_next('p').text.strip() for citation in citations]
        citations_by_section[section_name] = citations_list
    return citations_by_section

