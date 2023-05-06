# JetBrains Academy Web Scraper Project

An example of a passing solution to the final phase of the JetBrains Academy Python Web Scraper project.

## Description

This project is a Python script that scans article list pages at www.nature.com. The user may enter the number of article list pages to scan and the type of articles to search for. Articles matching the requested type are saved into folders created for each article list page.

[Beautiful Soup](https://www.crummy.com/software/BeautifulSoup/) is used to parse web site elements.

## Notes

This is a single file script.

Beautiful Soup may be installed with this command:

```
pip install beautifulsoup4
```

The script expects two input items. The first input item is a number indicating the maximum number of article list pages to go through. For example, entering 3 indicates that article list pages 1, 2 and 3 should be searched. The second input item is the type of article to save. For example, entering "News" saves articles tagged as news articles.

Here is an example of a run of the script:

```
> python scraper.py
> 3
> News
Saved all articles.
Saved all articles.
Saved all articles.
```

The above matches the project specifications. No input prompts were shown for the specification example. The phrase 'Saved all articles.' was shown as the specification example for output. To not potentially confuse the automated tester, the specification examples were followed exactly.

Running the above script created three output directories with each containing news articles from article list pages 1, 2 and 3.
