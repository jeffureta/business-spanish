from pathlib import Path
import pdfplumber

def extract_dialogue_pages(pdf_path, start_page=3, end_page=71):
    extracted_text = []
    
    with pdfplumber.open(pdf_path) as pdf:
        total_pages = len(pdf.pages)
        actual_end = min(end_page, total_pages)
        
        for page_num in range(start_page - 1, actual_end):
            text = pdf.pages[page_num].extract_text()
            if not text:
                continue
                
            # Clean running headers and footers
            lines = [
                line for line in text.split("\n")
                if not line.strip().startswith("Manual of business spanish")
                and not line.strip().startswith("Business situations")
                and not line.strip().isdigit()
            ]
            extracted_text.append("\n".join(lines))
            
    return "\n\n".join(extracted_text)


if __name__ == "__main__":
    # Locate the PDF in the exact same directory as this Python script
    current_dir = Path(__file__).parent
    pdf_file = current_dir / "manual-of-business-spanish.pdf"
    output_file = current_dir / "extracted_dialogues.txt"

    if not pdf_file.exists():
        print(f"Error: Could not find '{pdf_file.name}' in {current_dir}")
    else:
        print("Extracting dialogues...")
        dialogues = extract_dialogue_pages(pdf_file)
        
        # Save output to a text file
        with open(output_file, "w", encoding="utf-8") as f:
            f.write(dialogues)
            
        print(f"Extraction complete. Output saved to: {output_file.name}")