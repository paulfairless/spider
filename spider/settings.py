# -*- coding: utf-8 -*-

# Scrapy settings for spider project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://doc.scrapy.org/en/latest/topics/settings.html
#     https://doc.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://doc.scrapy.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'spider'

SPIDER_MODULES = ['spider.spiders']
NEWSPIDER_MODULE = 'spider.spiders'


# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'spider (+http://www.yourdomain.com)'

# Obey robots.txt rules
ROBOTSTXT_OBEY = True

# Configure maximum concurrent requests performed by Scrapy (default: 16)
#CONCURRENT_REQUESTS = 32

# Configure a delay for requests for the same website (default: 0)
# See https://doc.scrapy.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
#DOWNLOAD_DELAY = 3
# The download delay setting will honor only one of:
#CONCURRENT_REQUESTS_PER_DOMAIN = 16
#CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
#COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
#TELNETCONSOLE_ENABLED = False

# Override the default request headers:
#DEFAULT_REQUEST_HEADERS = {
#   'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
#   'Accept-Language': 'en',
#}

# Enable or disable spider middlewares
# See https://doc.scrapy.org/en/latest/topics/spider-middleware.html
#SPIDER_MIDDLEWARES = {
#    'spider.middlewares.SpiderSpiderMiddleware': 543,
#}

# Enable or disable downloader middlewares
# See https://doc.scrapy.org/en/latest/topics/downloader-middleware.html
#DOWNLOADER_MIDDLEWARES = {
#    'spider.middlewares.SpiderDownloaderMiddleware': 543,
#}

# Enable or disable extensions
# See https://doc.scrapy.org/en/latest/topics/extensions.html
#EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
#}

# Configure item pipelines
# See https://doc.scrapy.org/en/latest/topics/item-pipeline.html
ITEM_PIPELINES = {
   'spider.pipelines.SpiderPipeline': 300,
   'scrapy.pipelines.images.ImagesPipeline': 1,
   'spider.pipelines.FirestorePipeline': 1000
}

# Enable and configure the AutoThrottle extension (disabled by default)
# See https://doc.scrapy.org/en/latest/topics/autothrottle.html
AUTOTHROTTLE_ENABLED = True
# The initial download delay
#AUTOTHROTTLE_START_DELAY = 5
# The maximum download delay to be set in case of high latencies
#AUTOTHROTTLE_MAX_DELAY = 60
# The average number of requests Scrapy should be sending in parallel to
# each remote server
AUTOTHROTTLE_TARGET_CONCURRENCY = 0.5
# Enable showing throttling stats for every response received:
#AUTOTHROTTLE_DEBUG = False

# Enable and configure HTTP caching (disabled by default)
# See https://doc.scrapy.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
#HTTPCACHE_ENABLED = True
#HTTPCACHE_EXPIRATION_SECS = 0
#HTTPCACHE_DIR = 'httpcache'
#HTTPCACHE_IGNORE_HTTP_CODES = []
#HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'
AWS_ACCESS_KEY_ID='AKIAJZRV3YOR3KC7NI5Q'
AWS_SECRET_ACCESS_KEY='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'
IMAGES_STORE_S3_ACL = 'public-read'
IMAGES_STORE = 's3://modum-image/download/'
IMAGES_RESULT_FIELD = 'images'

FIREBASE="""{
  "type": "service_account",
  "project_id": "modum-e2bbb",
  "private_key_id": "2745fac00f4c47dbd6c2eb6cb40394661fa89bb7",
  "private_key": "-----BEGIN PRIVATE KEY-----\\nMIIEvgIBADANBgkqhkiG9w0BAQEFAASCBKgwggSkAgEAAoIBAQDMU0fgow2paGGl\\nx4+XYgvN34r528AP9KMOCVlJverkXEhlj7OlAxpf+QvKgvrCwbpkj1QL6srKTVqp\\nbyRWEgKmAaX+82FTf+zEzlVbW+9tsM2egVHgDhiV3Q7OFPC79LZ+6j+q8XLogqQv\\nIGeXCIDe46GoyQbCjg8kZhzkW3aGOsWIQgP8mdmi45mfhivdSO5HErHKYA6f3x/O\\nPrlfnLWE0u5EugBgf9i3lb0yGKcmpmCtUaV4Cw91YrDGBfU+fy+0lEzubnQfKhII\\nBZZlq9hOJwNL8NMtGll+zGOEijCUZB6Gc6XGjdLOFohk67TnjUeRN6sELQ8KOqS3\\nRUpcRjL/AgMBAAECggEAN4UpstCblbzXS8S+L9RkgLyNdvdPaQaAh//iUzdX7FVn\\nFrHFjsEZGZsCqTSODv21OD36CIL0N6RtTjz1Eq4yKgmooW5gs9++5ntqljiVBqlU\\nNg3NwaQS6iX3L+hgwbHtJO9h/YE+SA+3rVaQz2lwGyCffM2jGJqhYrKchzCTNEWn\\nEuqrkSNoM5FniLbqzgXZ+xo3WnfCibJKiA5ihsf245sHWO0eYYncd3sbtCbKz4V2\\nUlb1fF+Mc/V7Gr/xtzafoiSVaXp1ZVb0KrqRpKftSGRS/RhNHT5I+f/tr3YCTvHb\\n0nDtDxBlLetDI2yerqphouU8oDYBI4yzsH89EkrlAQKBgQD9jFKOThbKBQxwab3X\\nIXD3j08TnNWOzEUw58kGUuuiByL//6F+5pmb6tH4DAW7FY7svL0pfli6UfN/riYF\\nYN7aZjPY+vwEPTbTY7r9AJ5752KqTbQ86MKNl9VXHmDL+Zfyim8YulLJ2Dn9DdMQ\\nyEWLRRPY8A9eAFY8U3U/awCruQKBgQDOTRp+QJUY8lh/FoYJrgicT4J9cwQ3lTMO\\n8+bxE+azpBI3lf6jxE3FLQeTtRqHAIbsWjF3yY1nfRwsB52D43yVWkbQNmGpniZm\\naLy8XgOsNcCA/ojNnpKW4Yv72OIQlIcDq8qYjGHYc+ZrY0pK8kxU1SBgmxfsA3um\\nTXWvJZlgdwKBgQDe4lq0RAseff+oVhwPIJOY2/7Mo+LLy9/LFQaPK5d98L4gwowp\\n7Pb9rBf18EOdaV8h1uyGrE29REtEY0eDFNvyq0NKq5+c7l7ixtnajI/FJeuDABnA\\nLXDRXbaqBcdbp8ad7HmrCCe8zfpz7JItP5B61DeVTbqEjNFB6K+6FwsY6QKBgHfy\\nLG0rb4TJotqBZf1KyobXU69MqC8I+F7BQIz6XTAlPNJEy4C8Kdtyiu0+ZuYHUGsr\\nJYfYD/cTrsWKx/Je2ZicnH+CntXXtcvlKZb7snb16a8WTsP+ZoyDJriPKSEqujVQ\\nNMLtHBaVjGrzl8ZriiXopKKGiioW/FV8w+fJnJuRAoGBAOXfvy2W+CgZasG7saA9\\nw88MkBWxwLvUuw8nFcXoiLLUidmXpPLv93TBdjc/xQmxjEU+6VEBNcIhA7cnaBmh\\nGRz430BxlDHSRl5N9x+YOPw5s850ZN5/8GI3dVPAVodxTHtPGNIRGtR1Xk7eAOeL\\nYXxmj298R1IC44pe2R8R+OyV\\n-----END PRIVATE KEY-----\\n",
  "client_email": "firebase-adminsdk-p83pz@modum-e2bbb.iam.gserviceaccount.com",
  "client_id": "106740250856022359029",
  "auth_uri": "https://accounts.google.com/o/oauth2/auth",
  "token_uri": "https://oauth2.googleapis.com/token",
  "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
  "client_x509_cert_url": "https://www.googleapis.com/robot/v1/metadata/x509/firebase-adminsdk-p83pz%40modum-e2bbb.iam.gserviceaccount.com"
}"""