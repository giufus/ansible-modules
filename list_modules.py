import bs4
import requests

def print_modules():
    page = requests.get("https://docs.ansible.com/ansible/latest/collections/index_module.html")
    soup = bs4.BeautifulSoup(page.content, 'html.parser')
    modules = soup.find_all(id='index-of-all-modules')[0].find_all('li')
    for module in modules:
        print(module.text)
        print('\t', 'https://docs.ansible.com/ansible/latest/collections/' + module.find_all('a')[0]['href'])
        print()

if __name__ == '__main__':
    print_modules()