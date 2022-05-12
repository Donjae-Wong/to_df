from lxml import etree
import pandas as pd


def save_html_df(file_path, out_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        t_list = etree.HTML(f.read()).xpath(r'//*[@id="write"]/figure/table')
        text_list = [etree.tostring(t).decode('utf-8') for t in t_list]
        [pd.read_html(t)[0].to_csv(out_path) for t in text_list]
