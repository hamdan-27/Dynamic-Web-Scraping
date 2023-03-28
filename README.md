# Dynamic-Web-Scraping
Dynamic web scraper of online directory

This python script scrapes a dynamic webpage containing faculty information. The term 'dynamic' here means that all the data is loaded into html from the server side using javascript, only when the "Show More" button is clicked.
To overcome this issue, instead of kust using BS4 to scrape statically, I used selenium to find the show more button and defined a function to click it and load all the data into html. Then grabbed the html source using selenium itself and then passed in into BS4 to be parsed and scraped.
The data is then recorded and stored in an MS Excel file locally.
