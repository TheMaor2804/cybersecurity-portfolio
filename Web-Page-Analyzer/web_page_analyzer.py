import requests
from bs4 import BeautifulSoup

# First version: find external links and separate some common file types
print("-----" * 5 + " External Link Analysis " + "-----" * 5)

url = input('Enter URL: ').strip()


if not url.startswith(("http://", "https://")):
    url = "https://" + url

try:
    response = requests.get(url)

    # Stop if the page could not be loaded successfully
    if response.status_code != 200:
        print('Error with requested URL')
        exit()

    domain_name = url.split("/")[2]

    soup = BeautifulSoup(response.text, 'html.parser')

    # Find all links on the page
    links = soup.find_all('a')

    external_links = []
    pdf_links = []
    txt_links = []
    php_links = []

    # Store links that point to a different domain
    for link in links:
        href = link.get('href')

        if href and href.split("/")[0].startswith("http") and href.split("/")[2] != domain_name:
            external_links.append(href)

    # Separate external links by file type
    for link in external_links:
        if link.lower().endswith("pdf"):
            pdf_links.append(link)
        elif link.lower().endswith("txt"):
            txt_links.append(link)
        elif link.lower().endswith("php"):
            php_links.append(link)

    # Print the results
    if len(external_links) > 0:
        print(f'Non-local links: {external_links}')
    else:
        print('No non-local links')

    if len(pdf_links) > 0:
        print(f'PDFs: {pdf_links}')
    else:
        print('No PDFs')

    if len(txt_links) > 0:
        print(f'Texts: {txt_links}')
    else:
        print('No Texts')

    if len(php_links) > 0:
        print(f'PHPs: {php_links}')
    else:
        print('No PHPs')

except Exception as error:
    print(error)


print("-----" * 5 + " Web Page Analysis Menu " + "-----" * 5)


# Second version: allow the user to choose what information to display
url = input('Enter URL: ').strip()


if not url.startswith(("http://", "https://")):
    url = "https://" + url

try:
    response = requests.get(url)

    if response.status_code != 200:
        print('Error with requested URL')
        exit()

    domain_name = url.split("/")[2]

    soup = BeautifulSoup(response.text, 'html.parser')

    option = int(input(
        "Choose option:\n"
        "1. Show all non local links\n"
        "2. Show all files linked from the page\n"
        "3. Show forms and input fields\n"
    ))

    # Show links that point outside the current domain
    if option == 1:
        links = soup.find_all('a')
        external_links = []

        for link in links:
            href = link.get('href')

            if href and href.split("/")[0].startswith("http") and href.split('/')[2] != domain_name:
                external_links.append(href)

        for link in external_links:
            print(link)
            print('=====' * 5)

    # Show links that appear to point to files
    elif option == 2:
        links = soup.find_all('a')
        file_links = []

        common_file_extensions = [
            "txt", "pdf", "doc", "docx", "xls", "xlsx", "ppt", "pptx",
            "csv", "json", "xml", "html", "htm", "css", "js", "ts",
            "py", "java", "c", "cpp", "cs", "rb", "go", "php", "sh",
            "bat", "exe", "dll", "iso", "zip", "rar", "7z", "tar",
            "gz", "mp3", "wav", "flac", "aac", "ogg", "mp4", "mkv",
            "mov", "avi", "wmv", "jpg", "jpeg", "png", "gif", "bmp",
            "tiff", "svg", "webp", "psd", "ai", "eps", "ttf", "otf",
            "apk", "ipa", "log"
        ]

        for link in links:
            href = link.get('href')

            if href and href.startswith("http"):
                for extension in common_file_extensions:
                    if href.lower().endswith(f".{extension}"):
                        file_links.append(href)

        for link in file_links:
            print(link)
            print('=====' * 5)

    # Show forms and their input fields
    elif option == 3:
        forms = soup.find_all('form')

        print(f"Found {len(forms)} forms")

        form_number = 1

        for form in forms:
            print(f"Form: {form_number}")
            form_number += 1

            form_inputs = form.find_all('input')

            for form_input in form_inputs:
                if form_input.get('type'):
                    print('Type: ' + form_input.get('type'))

                if form_input.get('name'):
                    print('Name: ' + form_input.get('name'))
                else:
                    print("Name attribute is missing")

                print("=====" * 5)

except Exception as error:
    print(error)