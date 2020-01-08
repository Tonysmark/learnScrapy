from scrapy.commands import ScrapyCommand
from scrapy.utils.project import get_project_settings


class Command(ScrapyCommand):
    requires_project = True

    def syntax(self):
        return '[options]'

    def short_desc(self):
        return 'Run all of your spiders'

    def run(self, args, opts):
        spiders = self.crawler_process.spider_loader.list()
        for spider in spiders:
            self.crawler_process.crawl(spider, **opts.__dict__)
        self.crawler_process.start()
