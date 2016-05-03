# The script parses a Hebrew frequency list page and generates convenient PDF file with the list

Parsed page:

http://www.teachmehebrew.com/hebrew-frequency-list.html

Generated PDF file:

[hebrew_frequency_list.pdf](./hebrew_frequency_list.pdf)

## Requirements

Python 2.7

## Libraries used
<ul>
  <li>Scrapy</li>
  <li>ReportLab</li>
</ul>

## Dependencies installation
    
	pip install Scrapy
	pip install reportlab
	
## How to run

	cd PATH_TO/python-hebrew-frequency-list
	scrapy crawl hebrew_frequency_list
