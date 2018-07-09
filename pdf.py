import PyPDF2, os

# Get all the PDF sig pages.
pdfFiles = []
path = './tmp'
for filename in os.listdir(path):
    if filename.endswith('.pdf'):
        pdfFiles.append(filename)
pdfFiles.sort()

pdfWriter = PyPDF2.PdfFileWriter()

# Loop through all the PDF sig pages.
for filename in pdfFiles:
    pdfFileObj = open('./tmp/' + filename, 'rb')
    pdfReader = PyPDF2.PdfFileReader(pdfFileObj)

    # Loop through all the pages (except the first) and add them.
    for pageNum in range(0, pdfReader.numPages):
        pageObj = pdfReader.getPage(pageNum)
        pdfWriter.addPage(pageObj)

# Save the resulting PDF to a file.
pdfOutput = open('sig_pages_combined.pdf', 'wb')
pdfWriter.write(pdfOutput)
pdfOutput.close()

#clean up tmp directory
for the_file in os.listdir(path):
    file_path = os.path.join(path, the_file)
    try:
        if os.path.isfile(file_path):
            os.unlink(file_path)
        #elif os.path.isdir(file_path): shutil.rmtree(file_path)
    except Exception as e:
        print(e)

