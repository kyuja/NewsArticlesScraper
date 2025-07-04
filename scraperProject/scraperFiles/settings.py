BOT_NAME = "scrape news portals"

SPIDER_MODULES = ["scraperFiles.spiders"]
NEWSPIDER_MODULE = "scraperFiles.spiders"

# Crawl responsibly by identifying yourself (and your website) on the user-agent
USER_AGENT = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36 Edge/128.0.0.0"

# Obey robots.txt rules
ROBOTSTXT_OBEY = False

# Configure maximum concurrent requests performed by Scrapy (default: 16)
# CONCURRENT_REQUESTS = 32

# Configure a delay for requests for the same website (default: 0)
# See https://docs.scrapy.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
# DOWNLOAD_DELAY = 5
# The download delay setting will honor only one of:
# CONCURRENT_REQUESTS_PER_DOMAIN = 20
# CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
COOKIES_ENABLED = True

# Disable Telnet Console (enabled by default)
# TELNETCONSOLE_ENABLED = False
TELNETCONSOLE_PORT = None


ITEM_PIPELINES = {
    "scraperFiles.pipelines.CsvWriterPipeline": 300,
}

AUTOTHROTTLE_ENABLED = True
AUTOTHROTTLE_START_DELAY = 2
# The maximum download delay to be set in case of high latencies
# AUTOTHROTTLE_MAX_DELAY = 60
# The average number of requests Scrapy should be sending in parallel to
# each remote server
# AUTOTHROTTLE_TARGET_CONCURRENCY = 5.0
# Enable showing throttling stats for every response received:
# AUTOTHROTTLE_DEBUG = False


REQUEST_FINGERPRINTER_IMPLEMENTATION = "2.7"
TWISTED_REACTOR = "twisted.internet.asyncioreactor.AsyncioSelectorReactor"
FEED_EXPORT_ENCODING = "utf-8"

DEPTH_LIMIT = 1

COMMANDS_MODULE = "scraperFiles.commands"

CSV_INPUT_FILE = '../scraperProject/scraperFiles/data/Portale.csv'

CSV_OUTPUT_PATH = "C:/Users/Sophia/Desktop/Math stuff"

LOG_ENABLED = True
LOG_LEVEL = "INFO"
LOG_FILE = "logs.txt"

RETRY_ENABLED = True
RETRY_TIMES = 3

