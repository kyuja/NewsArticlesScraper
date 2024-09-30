# Scraping News Articles

* <strong>Title:</strong> News Articles Scraper
* <strong>Creator:</strong> Esther von der Weiden
* <strong>E-Mail-Address:</strong> esther.von-der-weiden@stud.uni-due.de
* <strong>Description:</strong> This Python tool retrieves the homepages of given news portals and scrapes the HTML text of the articles found. Each text is saved in a separate file. For each portal, an overview file is created for each call, which contains the metadata of the articles and the corresponding file paths.
* <strong>Database:</strong> No Database is used. Data is saved directly to the filesystem
* <strong>Input data:</strong> As an Input a csv file with URLs of news portals, the HTML tag to find the articles on the homepage and the tag to find the text of the news articles is needed
* <strong>Output data:</strong> The output consists of several text files containing the HTML text of the articles, a csv file containing an overview of the articles for each portal and a log file. The overview file contains the portal name, the date of scraping, the URL of the article, the title of the article, the keywords of the article, the path to the article text and the date of the article.
The output is structured as follows: [![](https://mermaid.ink/img/pako:eNp1kmFrgzAQhv-K5NNW9A_4YVBYGYO2G3UwGMI4klNDY05irEjpf1_SVGm7ep_Mve89OS93ZJwEspQVinpegbHRepfryEVDxoIqSAk0TwWkBSThkFCDOloEXUONi1BwHUGMQsFz0B1ccoXtPFKAfQTzIUCqYULcgnl7-DigOUjsR6pUOIsLKFeU0KUq8v77Ll2qvcFdlMhKq-baPDt7aauR46j_xxklycvdOGZMV7_2aIi3IN-xd7GY1WhqkMI97NFncqZgoM7mLHXfAkqDOYuDot0CfCrgWKO2mTVuaOUQjOv37Wq5-81Wb5vV9iubShTRPji4graVfFJs5TDjLWY_5Wt3ENTrZWfp20DjLQWoFnN9cu2CS2eD5iy1psOYGerKiqVnR8y6xr_kq3RtQz1lUUhLZhPW97zFMWtA_xCNntMfdTHtsw?type=png)](https://mermaid.live/edit#pako:eNp1kmFrgzAQhv-K5NNW9A_4YVBYGYO2G3UwGMI4klNDY05irEjpf1_SVGm7ep_Mve89OS93ZJwEspQVinpegbHRepfryEVDxoIqSAk0TwWkBSThkFCDOloEXUONi1BwHUGMQsFz0B1ccoXtPFKAfQTzIUCqYULcgnl7-DigOUjsR6pUOIsLKFeU0KUq8v77Ll2qvcFdlMhKq-baPDt7aauR46j_xxklycvdOGZMV7_2aIi3IN-xd7GY1WhqkMI97NFncqZgoM7mLHXfAkqDOYuDot0CfCrgWKO2mTVuaOUQjOv37Wq5-81Wb5vV9iubShTRPji4graVfFJs5TDjLWY_5Wt3ENTrZWfp20DjLQWoFnN9cu2CS2eD5iy1psOYGerKiqVnR8y6xr_kq3RtQz1lUUhLZhPW97zFMWtA_xCNntMfdTHtsw)
* <strong>Installation:</strong>
  1.  download the code :smile:
  2.  install dependencies from [requirements.txt](https://github.com/EstherKuerbis/NewsArticlesScraper/blob/main/requirements.txt)
  3.  set settings in [settings.py](https://github.com/EstherKuerbis/NewsArticlesScraper/blob/main/scraperProject/scraperFiles/settings.py)
  4.  open terminal and run `scrapy crawl_from_csv` from project folder
* <strong>Notes:</strong> The path to the output directory needs to be changed as it's an absolute path for now. The input file is included in the project's [data folder](https://github.com/EstherKuerbis/NewsArticlesScraper/tree/main/scraperProject/scraperFiles/data), but it's path can be changed. The log file is saved in the project directory. Every paths can be set in the [settings.py](https://github.com/EstherKuerbis/NewsArticlesScraper/blob/main/scraperProject/scraperFiles/settings.py) file. 
