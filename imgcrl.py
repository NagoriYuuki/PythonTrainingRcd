import os
from warnings import filters

from icrawler.builtin import BingImageCrawler

arr = ['马嘉祺', '丁程鑫', '宋亚轩', '刘耀文', '张真源', '严浩翔', '贺峻霖']
path1 = 'tnt_images'

print('running')
for i in arr:
    loc = os.path.join(path1, i)
    print(f"{i}running")

    bing_crawler = BingImageCrawler(
        feeder_threads=1,
        parser_threads=2,
        downloader_threads=4,
        storage={'root_dir': loc}
    )
    bing_crawler.crawl(
        keyword=i,
        max_num=200
    )
    print(f"{i} on test in {loc}")
print("Pretest Accepted")

grouppath = os.path.join(path1, '时代少年团合照')
print("running")

filter2 = {
    'size': 'large',
    'color': 'blackandwhite'
}

groupcrl = BingImageCrawler(
    feeder_threads=1,
    parser_threads=2,
    downloader_threads=4,
    storage={'root_dir': grouppath}
)

groupcrl.crawl(
    keyword='时代少年团 合照',
    filters=filter2,
    max_num=30
)
print("Accepted")
