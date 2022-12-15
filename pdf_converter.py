from pdf2docx import Converter

print("PDF2DOCX by Solomon Taiwo\n" + "-" * 50 + "\nThis program converts a PDF to a docx file.\n")

try:
    pdf_file = input("Insert the name of the pdf file: ") # Ask the user for the name of the file
    pdf_file= pdf_file + ".pdf"                           # Add .pdf extension to the filename
    docx_file = "converted_" + pdf_file[0:-4] + ".docx"   # Add "converted" and ".docx" to converted filename
    file = Converter(pdf_file)                            # Open pdf file to convert
    file.convert(docx_file)                               # Convert file to docx
    file.close()                                          # Close file
    print("Done, your file has been converted! Closing program...")
except IOError as i:
    print(i)
except Exception as e:
    print(e)
