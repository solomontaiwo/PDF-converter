from pdf2docx import Converter

print("\n- " + "PDF Converter: convert a PDF to a docx file" + " -\n")

try:
    # Ask the user for the name of the file
    pdf_file = input("Insert the name of the pdf file: ")

    print()

    # Add .pdf extension to the filename
    pdf_file = pdf_file + ".pdf"

    # Add "converted" and ".docx" to converted filename
    docx_file = "converted_" + pdf_file[0:-4] + ".docx"

    # Open pdf file to convert
    file = Converter(pdf_file)

    # Convert file to docx
    file.convert(docx_file)

    # Close file
    file.close()

    print("\nDone, your file has been converted! Closing program...\n")

# Print error if file is not found
except IOError as i:
    print(i)

# Print error if convertion can't be done
except Exception as e:
    print(e)