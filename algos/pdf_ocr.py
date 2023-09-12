#OCR - Optical Character Recognition, extragere text din imagini/ doc scanate

#Folosim tesseract
#https://pypi.org/project/pytesseract/ atentie ca trebuie sa descarcati niste fisiere
from PIL import Image #librarie de manipulare imagini
import pytesseract
#pip install pytesseract
#pentru pdf, folosim pymupdf, import fitz
import fitz
import io

pytesseract.pytesseract.tesseract_cmd = "B:/All_Software/Tesseract-OCR/tesseract.exe"

def citire_text_imagini_png(img_path):
    #extragre text din png, adica imagini cu extensia png
    text_extras = pytesseract.image_to_string(imagine_cu_text, lang="ron")
    return text_extras

imagine_cu_text = "B:/pyx/SDA/SDA_52/Screenshot_2.png"
print(citire_text_imagini_png(imagine_cu_text))
#extrage text din pdf scanat

def citire_text_pdf(full_path_pdf):
    pdf_binar = fitz.open(full_path_pdf)
    tot_textul = ""
    for page in pdf_binar:
        imagine_pagina = page.get_pixmap(matrix=fitz.Matrix(2,2), colorspace=fitz.csRGB, alpha=True)
        imagine_data = imagine_pagina.tobytes()
        img = Image.open(io.BytesIO(imagine_data))
        text_extras_pagina = pytesseract.image_to_string(img)
        tot_textul += f"{text_extras_pagina}\n{'_'*40}\n"
    return tot_textul
# tx = "Salut ce mai faci"
# print(f"{tx}\n{'_'*40}\n")

pdf_path = "B:/pyx/SDA/SDA_52/Sample_Scanned_PDF.pdf"
print(citire_text_pdf(pdf_path))