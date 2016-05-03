# -*- coding: utf-8 -*-

from reportlab.platypus import Paragraph
from reportlab.lib.styles import getSampleStyleSheet
from hebrew_frequency_list.pdf_generator import PdfGenerator


class HebrewFrequencyListPipeline(object):
    def __init__(self):
        self.words = [[
            'Rank',
            'English',
            'Transliteration',
            'Hebrew',
        ]]

    def process_item(self, item, spider):
        styles = getSampleStyleSheet()

        values = [
            item['rank'],
            Paragraph(item['english'], styles['Normal']),
            item['transliteration'],
            unicode(item['hebrew'], 'utf-8')[::-1],  # Reverses a hebrew word
        ]
        self.words.append(values)

    def close_spider(self, spider):
        PdfGenerator.generate_table('hebrew_frequency_list.pdf', self.words)
