from archivenow import archivenow
from datetime import datetime
import pandas as pd

def load_files():
    df = pd.read_csv('doh_summary.csv')
    case_pages = df['covid_case'].dropna().tolist()
    main_pages = df['covid_main'].dropna().tolist()
    return case_pages, main_pages

def archive_page(page_url):
    results = [page_url]
    results.append(archivenow.push(page_url, "wc"))
    results.append(archivenow.push(page_url, "ia"))
    results.append(archivenow.push(page_url, "is"))
    return results

def run_archive_task():
    case_pages, main_pages = load_files()
    pages_to_archive = case_pages + main_pages
    responses = []
    for page in pages_to_archive:
        responses.append(archive_page(page))
    return responses

