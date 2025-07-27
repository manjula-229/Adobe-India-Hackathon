import os
import json
from collections import defaultdict
from pdfminer.high_level import extract_pages
from pdfminer.layout import LTTextBox, LTTextContainer, LTChar

def extract_title(text_boxes):
    # Pick the largest text block on page 1
    candidates = [(box['size'], box['text']) for box in text_boxes if box['text'].strip()]
    if not candidates:
        return ""
    candidates.sort(reverse=True)
    return candidates[0][1].strip()

def extract_headings(pdf_path):
    fontsizes = defaultdict(int)
    all_text_boxes = []
    outlines = []

    for page_num, layout in enumerate(extract_pages(pdf_path), start=1):
        for element in layout:
            if isinstance(element, (LTTextBox, LTTextContainer)):
                for text_line in element:
                    text = text_line.get_text().strip()
                    if not text:
                        continue
                    sizes = [obj.size for obj in text_line if isinstance(obj, LTChar)]
                    if sizes:
                        max_size = max(sizes)
                        fontsizes[max_size] += 1
                        all_text_boxes.append({
                            "text": text,
                            "size": max_size,
                            "page": page_num
                        })

    if not fontsizes:
        return "", []

    # Identify most common sizes (assume top 3 are H1, H2, H3)
    sorted_sizes = sorted(fontsizes.items(), key=lambda x: (-x[0], -x[1]))
    top_sizes = [s[0] for s in sorted_sizes[:3]]

    # Map sizes to heading levels
    heading_map = {}
    if len(top_sizes) == 1:
        heading_map[top_sizes[0]] = "H1"
    elif len(top_sizes) == 2:
        heading_map[top_sizes[0]] = "H1"
        heading_map[top_sizes[1]] = "H2"
    else:
        heading_map[top_sizes[0]] = "H1"
        heading_map[top_sizes[1]] = "H2"
        heading_map[top_sizes[2]] = "H3"

    # Extract title from first page
    title = extract_title([b for b in all_text_boxes if b["page"] == 1])

    for box in all_text_boxes:
        if box["size"] in heading_map:
            outlines.append({
                "level": heading_map[box["size"]],
                "text": box["text"],
                "page": box["page"]
            })

    return title, outlines

def main():
    input_pdf = "sample.pdf"  # <- replace with your PDF
    output_json = "sample.json"

    if not os.path.exists(input_pdf):
        print("PDF file not found.")
        return

    title, outline = extract_headings(input_pdf)

    result = {
        "title": title,
        "outline": outline
    }

    with open(output_json, "w", encoding="utf-8") as f:
        json.dump(result, f, indent=2, ensure_ascii=False)

    print(f"✅ Done! JSON saved to: {output_json}")

if __name__ == "__main__":
    main()