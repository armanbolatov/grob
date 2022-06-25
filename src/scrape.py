from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd
import time

titles, lyrics = [], []
driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get("https://www.gr-oborona.ru/texts/")

blocks = driver.find_elements_by_tag_name("ul#abc_list")
for block in blocks:
    title_elements = block.find_elements_by_tag_name("a")
    for title_element in title_elements:
        link = title_element.get_attribute("href")
        driver.get(link)
        time.sleep(2)
        title = driver.find_element_by_xpath('//*[@id="headers"]/h3').text
        content = driver.find_element_by_xpath('//*[@id="cont"]').text
        try:
            sub_str = "Песни из этого же альбома или этого автора:"
            res = content[:content.index(sub_str) + len(sub_str)]
            recs = True
        except:
            recs = False
        splitted = str(res).splitlines()
        if splitted[0].startswith("Автор:"):
            del splitted[0]
        if splitted[0].startswith("Альбом:"):
            del splitted[0]
        if recs:
            del splitted[-1]
        lyrics.append("\n".join(splitted))
        titles.append(title)
        driver.back()
        time.sleep(2)

pd.DataFrame(
    {'Title': titles, 'Lyrics': lyrics}
).to_excel("all_lyrics.xlsx")