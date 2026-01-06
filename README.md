# Azure Content Understanding Service Demo

This repository contains a Jupyter notebook demonstrating how to use Azure Foundry Content Understanding service for OCR (Optical Character Recognition) on PDF documents and images.

## Features

- 📓 Jupyter notebook with complete examples
- 🐍 Simple Python function that takes a file path as input
- 📄 Sample PDF documents (invoices, receipts)
- 🖼️ Sample images (business cards, signs)
- 🔄 Batch processing capabilities
- 💾 JSON response handling and storage

## Prerequisites

- Python 3.8 or higher
- pip (Python package manager)
- Azure Foundry account with Content Understanding service access
- Azure Foundry API credentials (endpoint and API key)

## Installation

1. Clone this repository:
```bash
git clone https://github.com/qkfang/cu-demo.git
cd cu-demo
```

2. Install required Python packages:
```bash
pip install -r requirements.txt
```

3. Set up your Azure credentials:
   - Copy `.env.example` to `.env`
   - Edit `.env` and add your Azure Foundry endpoint and API key:
   ```
   AZURE_FOUNDRY_ENDPOINT=https://your-endpoint.azure.com
   AZURE_FOUNDRY_API_KEY=your-api-key
   ```

4. Generate sample documents:
```bash
python generate_samples.py
```

## Usage

### Running the Jupyter Notebook

1. Start Jupyter Notebook:
```bash
jupyter notebook
```

2. Open `azure_content_understanding_demo.ipynb` in your browser

3. Run the cells in order to:
   - Configure Azure credentials
   - Process individual PDF and image files
   - Run batch processing on all sample documents
   - Save results to JSON

### Using the Python Function

The core function `process_file_with_content_understanding(file_path)` can be used in your own scripts:

```python
from azure_content_understanding_demo import process_file_with_content_understanding

# Process a file
result = process_file_with_content_understanding("path/to/your/file.pdf")

# Access the JSON response
print(result)
```

## Project Structure

```
cu-demo/
├── azure_content_understanding_demo.ipynb  # Main Jupyter notebook
├── generate_samples.py                      # Script to create sample documents
├── requirements.txt                         # Python dependencies
├── .env.example                            # Example environment configuration
├── .gitignore                              # Git ignore rules
├── README.md                               # This file
└── sample_documents/                       # Generated sample files (after running generate_samples.py)
    ├── sample_invoice.pdf
    ├── sample_receipt.pdf
    ├── business_card.png
    └── sign_text.png
```

## Sample Documents

The repository includes a script to generate sample documents for testing:

- **sample_invoice.pdf**: A simple invoice with line items
- **sample_receipt.pdf**: A retail receipt with multiple items
- **business_card.png**: A business card image with contact information
- **sign_text.png**: A parking sign with text

## Azure Foundry Content Understanding Service

The Azure Foundry Content Understanding service provides:
- Document analysis and OCR
- Text extraction from PDFs and images
- Table detection and extraction
- Key-value pair identification
- Form recognition
- Layout analysis

## Configuration

The notebook expects the following environment variables in `.env`:

- `AZURE_FOUNDRY_ENDPOINT`: Your Azure Foundry service endpoint
- `AZURE_FOUNDRY_API_KEY`: Your API key for authentication

## Output

The service returns JSON responses containing:
- Extracted text content
- Page information
- Tables (if detected)
- Key-value pairs (if detected)
- Bounding box coordinates
- Confidence scores

Results can be saved to `content_understanding_results.json` for further analysis.

## Error Handling

The notebook includes error handling for:
- Missing files
- API connection issues
- Authentication failures
- Rate limiting
- Invalid responses

## Security Notes

- Never commit your `.env` file to version control
- Keep your API keys secure
- The `.gitignore` file is configured to exclude sensitive files
- Rotate API keys regularly

## Troubleshooting

**Issue**: "Warning: Please configure your Azure credentials"
- **Solution**: Create a `.env` file with your actual Azure credentials

**Issue**: "Directory 'sample_documents' not found"
- **Solution**: Run `python generate_samples.py` to create sample documents

**Issue**: API connection errors
- **Solution**: Verify your endpoint URL and API key are correct
- **Solution**: Check that your Azure Foundry service is active and accessible

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is provided as-is for demonstration purposes.

## Support

For Azure Foundry Content Understanding service support, please refer to the [Azure documentation](https://azure.microsoft.com/) or contact Azure support.