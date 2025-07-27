# PDF Heading Extractor

> **Welcome to the “Connecting the Dots” Challenge: Rethink Reading. Rediscover Knowledge!**
> 
> What if every time you opened a PDF, it didn’t just sit there—it spoke to you, connected ideas, and narrated meaning across your entire library? That’s the future we’re building — and we want you to help shape it.

A Python tool that automatically extracts the **document title** and a structured **outline of headings** (H1, H2, H3) from a PDF file based on font size, and outputs the result as a clean JSON file.

## Features

- **Automatic document title detection** (largest text block on page 1).
- **Section heading extraction** using PDF font size analysis.
- **Provides section outline with heading level and page number**.
- Outputs a user-friendly, structured JSON file.
- Command-line interface—run in one command.

## How It Works

1. The tool analyzes all text blocks and their font sizes using [`pdfminer.six`](https://github.com/pdfminer/pdfminer.six).
2. The largest text on the first page is the document title.
3. The top 1-3 largest font sizes in the document are mapped to heading levels H1, H2, H3.
4. All matching text blocks are exported to a JSON outline with heading level and page number.

## Example

Given the [sample.pdf](./sample.pdf), running the tool produces [sample.json](./sample.json):

{
"title": "COMPUTING MACHINERY AND INTELLIGENCE",
"outline": [
{ "level": "H1", "text": "COMPUTING MACHINERY AND INTELLIGENCE", "page": 1 },
{ "level": "H2", "text": "7. Learning Machines", "page": 17 },
// ...
]
}

_See included [sample.pdf](./sample.pdf) and [sample.json](./sample.json) for a real example._

## Quickstart

1. **Install Python 3.7+**
2. **Install dependencies**
    ```
    pip install pdfminer.six
    ```
3. **Place your PDF in the directory (default: `sample.pdf`)**
4. **Run the script**
    ```
    python app.py
    ```
    The result will be saved as `sample.json`.

### Using Docker

You can run this project inside a container—no Python setup required!

#### 1. Build the Docker image

docker build -t pdf-heading-extractor .

text

#### 2. Run the Docker container

docker run --rm
-v "$(pwd)/input:/app/input"
-v "$(pwd)/output:/app/output"
pdf-heading-extractor

text

- Your input PDF (`input/sample.pdf`) and resulting JSON (`output/sample.json`) will be shared between your computer and the container.
- Adjust paths if your layout differs.


## File List

- `app.py` — main processing script
- `sample.pdf` — sample input file (included)

## Troubleshooting

- **Output is empty or missing headings?**
  - Make sure your PDF uses consistent, larger fonts for headings.
  - Scanned/image-based PDFs are not supported (use OCR first).
- **File not found:** Ensure your input PDF file matches the filename in `app.py`.
- **Non-English PDFs:** May require further tuning.


## Credits

- Developed by [Team: MaHa]
- Built using [pdfminer.six](https://github.com/pdfminer/pdfminer.six)




