import pandas as pd
import numpy as np
from tkinter import filedialog
from pathlib import Path
import os

#import PyPDF2


file_path = filedialog.askdirectory()
file_list = Path(file_path + '/').rglob('*.pdf')

file_names = os.listdir(file_path)
file_names = [file for file in file_names if file.endswith('.pdf')]
print(len(file_names))

file_df = []
context = []

for file in file_list:
    print(file.stem)
    file_name = file.stem

    pdf = PyPDF2.PdfFileReader(file)
    page_num = pdf.getNumPages()
    text = ''
    for i in range(0, page_num):
        PgOb = pdf.getPage(i)
        text += PgOb.extractText()
    # print(text)
    file_df.append(file_name)
    context.append(text)

pdf_df = pd.DataFrame({'File': file_df, 'Context': context})


pdf_df['Chair_Man_Check'] = np.nan
pdf_df.loc[pdf_df['Context'].str.contains('Chair Man'), 'Chair_Man_Check'] = 'Chair Man  - Yes'
print(pdf_df)