import PyPDF2
import sys

def cut_pages(filename="sample.pdf", endpoint="split_file", unit=0):
    # 取得pdf頁數
    reader = PyPDF2.PdfReader(filename)
    # 不解密的話可能會報錯
    if reader.is_encrypted:
        reader.decrypt('')
    page = len(reader.pages)
    # 取得頁數的結尾
    with open(filename, 'rb') as file:
        filecount = 1
        acc = 1
        writer = PyPDF2.PdfWriter()
        for x in range(page):
            if acc != unit:
                acc += 1
                writer.add_page(reader.pages[x])
            elif acc == unit:
                writer.add_page(reader.pages[x])
                with open(f"{endpoint}/{(filecount - 1) * unit + 1}-{filecount * unit}.pdf", 'wb') as output:
                    writer.write(output)
                acc = 1
                writer = PyPDF2.PdfWriter()
                filecount += 1
        if acc != 1:
            with open(f"{endpoint}/{(filecount - 1) * unit + 1}-{page}.pdf", 'wb') as output:
                writer.write(output)

# 取得參數
_, origin_file, endpoint_file, number_count = sys.argv
cut_pages(origin_file, endpoint_file, int(number_count))
# cut_pages("C:\Users\happy\Desktop\project_ourself\P00011出差辦法(20230818).pdf", "end", 1)
