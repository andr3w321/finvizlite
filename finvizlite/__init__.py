import requests
from bs4 import BeautifulSoup
import pandas as pd
import time

def rows_to_pages(rows):
    """ round up to the nearest 20, then divide by 20 
    eg 105 rounds to 120 then divides by 20 to returns 6"""
    return (rows - rows % -20) / 20

def get_new_query_url(old_url, param_field, new_param_value):
    """ Returns a new url with an updated query param value """
    query = requests.utils.urlparse(old_url).query
    params = dict(x.split('=') for x in query.split("&"))
    params[param_field] = new_param_value
    pre_query_url = old_url.split("?")[0]
    new_url = pre_query_url + "?" + '&'.join('{}={}'.format(key, val) for key, val in params.items())
    return new_url

def get_html(url):
    hdr = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11'}
    res = requests.get(url, headers=hdr)
    if res.status_code == 200:
        return res.text
    else:
        raise ValueError("{} getting {}", res.status_code, url)

def get_pagination_urls(url, page_options):
    urls = []
    for i in range(0, len(page_options)):
        # don't append the current url
        if "selected" not in page_options[i].attrs:
            urls.append(get_new_query_url(url, 'r', page_options[i]['value']))
    return urls

def get_df(tables):
    data = []
    trs = tables[3].find_all("tr")
    for tr in trs:
        row = []
        tds = tr.find_all("td")
        for td in tds:
            row.append(td.text)
        data.append(row)
    # don't return the header row
    df = pd.DataFrame(data[1:], columns=data[0])
    return df

def scrape(url, return_df_only=True, print_urls=False):
    if print_urls:
        print(url)
    soup = BeautifulSoup(get_html(url), "lxml")
    if soup.text == "Too many requests.":
        # TODO could sleep then retry the request here
        raise ValueError("too many requests while getting {}".format(url))
    page_select = soup.select("#pageSelect")
    if len(page_select) < 1:
        raise ValueError("ERROR: No pages element found at {}.\nPrinting url text\n{}".format(url, soup.text))

    page_options = page_select[0].find_all("option")
    urls = get_pagination_urls(url, page_options)

    tables = soup.select("#screener-content table")
    df = get_df(tables)
    if return_df_only:
        return df
    else:
        return urls, df

def scrape_all(url, sleep_interval=0.1, print_urls=False, rows=100000):
    pagination_urls, df = scrape(url, return_df_only=False, print_urls=print_urls)
    max_pages = rows_to_pages(rows)
    for i in range(0, len(pagination_urls)):
        if i >= max_pages-1:
            break
        time.sleep(sleep_interval)
        next_df = scrape(pagination_urls[i], return_df_only=True, print_urls=print_urls)
        df = df.append(next_df, ignore_index=True)
    return df[:rows]
