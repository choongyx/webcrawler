import time
from concurrent.futures import ThreadPoolExecutor

from crawllazada import crawl_lazada
from crawlqoo10 import crawl_qoo10

class ParallelWebCrawler:
    def __init__(self):
        # Create a pool of workers to run crawlers in parallel
        self.pool = ThreadPoolExecutor(max_workers=3)
        self.result = []

    # Run multiple crawlers in parallel
    def run_crawlers(self, keyword, num):
        job_1 = self.pool.submit(crawl_lazada, keyword, num)
        job_1.add_done_callback(self.crawler_callback)

        job_2 = self.pool.submit(crawl_qoo10, keyword, num)
        job_2.add_done_callback(self.crawler_callback)

        self.sort_and_print_results()

    def crawler_callback(self, res):
        result = res.result()
        self.result.extend(result)

    def sort_and_print_results(self):
        self.pool.shutdown()
        time.sleep(60)

        sorted_result = sorted(self.result, key=lambda x: x[1])

        print('Total results:', len(sorted_result))
        print('\n')

        for r in sorted_result:
            print('Product:', r[0])
            print('Price: $' + str(r[1]))
            print('Link:', r[2])
            print('\n')

# Initialize the parallel web crawler
if __name__ == '__main__':
    product = input('What product do you want to compare prices for?\n')
    num = input('How many results do you want from each website at most?\n')
    print('\nComparing prices for:', product, '\n')
    ParallelWebCrawler().run_crawlers(product, int(num))
