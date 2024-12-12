# try simple code with one paper
from docling.document_converter import DocumentConverter

# Try with local data
source = "2024-nissan-leaf-owner-manual.pdf"  # document per local path or URL
converter = DocumentConverter()
result = converter.convert(source)
print(result.document.export_to_markdown())
# output: ## Docling Technical Report [...]"
