import fitz
import glob
from os.path import basename

pdf_dir = glob.glob(r"D:\progect_work\Трудовые книжки2\*.pdf")

for pdf_ in pdf_dir:
    doc = fitz.open(pdf_)
    print(doc.metadata)
    page_count = 0
    name_doc = basename(pdf_)
    for i in range(len(doc)):
        for img in doc.getPageImageList(i):
            xref = img[0]
            pix = fitz.Pixmap(doc, xref)
            pix1 = fitz.Pixmap(fitz.csRGB, pix)

            page_count += 1

            pix1.writePNG("D:\progect_work\work_books_2\doc_"+name_doc+"_%s_from_page_%s.jpg" % (page_count, i+1))
            print("Image number ", page_count, " writed...")

            pix1 = None
