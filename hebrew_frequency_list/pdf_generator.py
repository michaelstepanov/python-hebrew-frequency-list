from reportlab.lib import colors
from reportlab.lib.units import mm
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.platypus import SimpleDocTemplate, Table

pdfmetrics.registerFont(TTFont('Hebrew', 'ArialHB.ttf'))


class PdfGenerator(object):
    def __init__(self):
        pass

    @staticmethod
    def generate_table(file_name, data):
        doc = SimpleDocTemplate(file_name, topMargin=-6, rightMargin=-6, bottomMargin=-10, leftMargin=-6)

        elements = []

        table_style = [
            ('VALIGN', (0, 0), (-1, -1), 'TOP'),
            ('BOX', (0, 0), (-1, -1), 0.5, colors.grey),
            ('GRID', (0, 0), (-1, -1), 0.5, colors.grey),
            ('ALIGN', (3, 2), (3, 2), 'LEFT'),
            ('FONTNAME', (0, 0), (-1, -1), 'Hebrew'),
            ('TEXTCOLOR', (0, 0), (-1, 1), colors.beige),
            ('TEXTCOLOR', (0, 1), (-1, -1), colors.black),
            ('BACKGROUND', (0, 0), (-1, 1), colors.black),
            ('BACKGROUND', (0, 1), (-1, -1), colors.beige),
        ]

        last_color = colors.lightgrey
        for i, row in enumerate(data):
            # Skips header row
            if i == 0:
                continue
            # Changes background color only for each hebrew word
            if row[0]:
                last_color = colors.darkgrey if last_color == colors.lightgrey else colors.lightgrey

            table_style.append(('BACKGROUND', (0, i), (-1, i), last_color))

        t = Table(data, style=table_style, colWidths=(14*mm, None, 38*mm, 29*mm))

        elements.append(t)
        # Writes the document to disk
        doc.build(elements)
