# -*- coding: utf-8 -*-

BOT_NAME = 'hebrew_frequency_list'

SPIDER_MODULES = ['hebrew_frequency_list.spiders']
NEWSPIDER_MODULE = 'hebrew_frequency_list.spiders'

ITEM_PIPELINES = {
    'hebrew_frequency_list.pipelines.HebrewFrequencyListPipeline': 500,
}

# Crawl responsibly by identifying yourself (and your website) on the user-agent
# USER_AGENT = 'hebrew_frequency_list (+http://www.yourdomain.com)'
