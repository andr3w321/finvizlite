# Finvizlite

[![Build Status](https://travis-ci.org/andr3w321/finvizlite.svg?branch=main)](https://travis-ci.org/andr3w321/finvizlite)

A lightweight finviz.com screener scraper for https://finviz.com/screener.ashx
All the code is about 80 lines long and can be found in `finvizlite/__init__.py`


## Install
`pip install finvizlite`

## Quick start

```
import finvizlite as fl

# To scrape a single page use fl.scrape(url)
df = fl.scrape("https://finviz.com/screener.ashx?v=141&o=-marketcap")

# To scrape multiple pages use fl.scrape_all(url)
# scrape the dow tickers
df = fl.scrape_all("https://finviz.com/screener.ashx?v=141&f=idx_dji&o=-marketcap")

# To print the scraped urls pass print_urls=True to scrape_all() or scrape()
>>> df = fl.scrape_all("https://finviz.com/screener.ashx?v=161&f=idx_dji&o=-marketcap", print_urls=True)
https://finviz.com/screener.ashx?v=161&f=idx_dji&o=-marketcap
https://finviz.com/screener.ashx?v=161&f=idx_dji&o=-marketcap&r=21

# To limit the amount of tickers scraped pass rows=max_rows to scrape_all
>>> df = fl.scrape_all("https://finviz.com/screener.ashx?v=121&o=-marketcap", print_urls=True, rows=50)
https://finviz.com/screener.ashx?v=121&o=-marketcap
https://finviz.com/screener.ashx?v=121&o=-marketcap&r=21
https://finviz.com/screener.ashx?v=121&o=-marketcap&r=41

# Download all the tickers from Overview page (takes ~2.5 mins)
df = fl.scrape_all("https://finviz.com/screener.ashx?v=111&o=-marketcap", print_urls=True)

# Save to csv
df.to_csv("all_tickers.csv", index=False)

# Speed up scraping. By default scrape_all sleeps 0.1 seconds between requests. You can shorten(or lengthen it) by passing the sleep_interval=time_in_seconds to scrape_url to speed up or slow down scraping, but you may run into "Too many requests" errors from finviz.com if you set it too low and make too many requests in a short time.
>>>df = fl.scrape_all("https://finviz.com/screener.ashx?v=111&o=-marketcap", sleep_interval=0)
ValueError: too many requests while getting https://finviz.com/screener.ashx?v=111&o=-marketcap&r=241

# If you want a list of the pagination urls for some reason, pass print_df_only=False to scrape()
>>> urls, df = fl.scrape("https://finviz.com/screener.ashx?v=111&f=sec_energy&o=-marketcap", return_df_only=False)
>>> urls
['https://finviz.com/screener.ashx?v=111&f=sec_energy&o=-marketcap&r=21', 'https://finviz.com/screener.ashx?v=111&f=sec_energy&o=-marketcap&r=41', 'https://finviz.com/screener.ashx?v=111&f=sec_energy&o=-marketcap&r=61', 'https://finviz.com/screener.ashx?v=111&f=sec_energy&o=-marketcap&r=81', 'https://finviz.com/screener.ashx?v=111&f=sec_energy&o=-marketcap&r=101', 'https://finviz.com/screener.ashx?v=111&f=sec_energy&o=-marketcap&r=121', 'https://finviz.com/screener.ashx?v=111&f=sec_energy&o=-marketcap&r=141', 'https://finviz.com/screener.ashx?v=111&f=sec_energy&o=-marketcap&r=161', 'https://finviz.com/screener.ashx?v=111&f=sec_energy&o=-marketcap&r=181', 'https://finviz.com/screener.ashx?v=111&f=sec_energy&o=-marketcap&r=201', 'https://finviz.com/screener.ashx?v=111&f=sec_energy&o=-marketcap&r=221', 'https://finviz.com/screener.ashx?v=111&f=sec_energy&o=-marketcap&r=241', 'https://finviz.com/screener.ashx?v=111&f=sec_energy&o=-marketcap&r=261', 'https://finviz.com/screener.ashx?v=111&f=sec_energy&o=-marketcap&r=281']
```
