pip PyPDF2


def pdf_to_text(pdf_path, text_path):
    try:
        with open(pdf_path, 'rb') as pdf_file:
            reader = PyPDF2.PdfReader(pdf_file)
            text = ''
            for page_num in range(reader.numPages):
                page = reader.getPage(page_num)
                text += page.extract_text()  # Updated method name

        with open(text_path, 'w') as text_file:
            text_file.write(text)
        print(f"Text has been successfully extracted and saved to {text_path}")

    except FileNotFoundError:
        print(f"The file {pdf_path} does not exist.")
    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    pdf_path = input("Enter the path to the PDF file: ")
    text_path = input("Enter the path to save the text file: ")
    pdf_to_text(pdf_path, text_path)
