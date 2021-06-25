import bs4
import requests
import argparse
import art

def print_modules(keyword):

    page = requests.get("https://docs.ansible.com/ansible/latest/collections/index_module.html")
    soup = bs4.BeautifulSoup(page.content, 'html.parser')
    try:
        modules = soup.find_all(id='index-of-all-modules')[0].find_all('li')
        for module in modules:
            description = module.text

            if(keyword in description):
                print(description)
                print('\t', 'https://docs.ansible.com/ansible/latest/collections/' + module.find_all('a')[0]['href'])
                print()
    except Exception as ex:
        print(f'Unable to get module catalog: {ex}')



if __name__ == '__main__':

    text_art = art.text2art("ansible-modules", font='bulbhead')
    print(text_art)

    parser = argparse.ArgumentParser(description='Search Ansible Modules.')
    parser.add_argument('keyword', type=str, help='keyword to look for')
    args = parser.parse_args()

    print_modules(args.keyword)