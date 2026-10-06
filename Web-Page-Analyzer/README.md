# Web Page Analyzer

A small Python project I originally created during my Ethical Hacking course to practice working with web pages using `requests` and `BeautifulSoup`.

The script can inspect a web page and extract some basic information from it.

## Features

- Find links that point to external domains
- Detect linked files such as PDF, TXT, ZIP, APK and other common formats
- Find HTML forms on the page
- Display input field names and types
- Automatically adds `https://` if the user enters a URL without a protocol

## Requirements

- Python 3
- requests
- beautifulsoup4

Install the required packages with:

```bash
pip install requests beautifulsoup4
```

## Usage

Run the script with:

```bash
python web_page_analyzer.py
```

Enter a website when prompted, for example:

```text
example.com
```

The script will automatically convert it to:

```text
https://example.com
```

The second part of the script allows you to choose between:

1. Showing external links
2. Showing linked files
3. Showing forms and input fields

## Notes

This is a small educational project and is not intended to be a full web crawler or vulnerability scanner.

It was created as part of my cybersecurity studies to practice Python, HTTP requests, HTML parsing, and basic web reconnaissance.
