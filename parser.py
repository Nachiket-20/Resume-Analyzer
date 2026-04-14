import PyPDF2

def extract_text_from_pdf(file_path):
    text = ""

    with open(file_path, "rb") as file:
        reader = PyPDF2.PdfReader(file)

        for page in reader.pages:
            text += page.extract_text()

    return text


# Test code
if __name__ == "__main__":
    resume_path = "sample_resume.pdf"  # put your resume file here
    extracted_text = extract_text_from_pdf(resume_path)

    print("\n===== EXTRACTED TEXT =====\n")
    print(extracted_text)