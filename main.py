# try simple code with one paper
from docling.document_converter import DocumentConverter
from docling.chunking import HybridChunker
from transformers import AutoTokenizer

import os 
from dotenv import load_dotenv, dotenv_values

import tiktoken

from openai import OpenAI

load_dotenv()

EMBED_MODEL_ID = "sentence-transformers/all-MiniLM-L6-v2"
OPENAI_KEY = os.getenv("OPENAI_API_KEY")
MAX_TOKENS = 512

# Try with local data
source = "data/2-403_HDCV Cung cấp thông tin phạm vi ngoài doanh nghiệp.pdf"  # document per local path or URL
converter = DocumentConverter()
result = converter.convert(source)

markdown_content = result.document.export_to_markdown()
output_file_path = "2-403_HDCV Cung cấp thông tin phạm vi ngoài doanh nghiệp.txt"  # Đường dẫn tệp xuất ra
with open(output_file_path, "w", encoding="utf-8") as file:
    file.write(markdown_content)

print(f"Markdown content has been saved to {output_file_path}")
# output: ## Docling Technical Report [...]"

# test hybrid chunking
# DOC_SOURCE = "data/CLIP.pdf"

# # Get docs
# doc = DocumentConverter().convert(source=DOC_SOURCE).document

# # Set tokenizer
# # Initialize the OpenAI API client
# client = OpenAI(api_key=OPENAI_KEY)

# tokenizer = AutoTokenizer.from_pretrained(EMBED_MODEL_ID)


# chunker = HybridChunker(
#     tokenizer=tokenizer,  # can also just pass model name instead of tokenizer instance
#     max_tokens=MAX_TOKENS,  # optional, by default derived from `tokenizer`
#     # merge_peers=True,  # optional, defaults to True
# )
# chunk_iter = chunker.chunk(dl_doc=doc)
# chunks = list(chunk_iter)

# for i, chunk in enumerate(chunks):
#     print(f"=== {i} ===")
#     txt_tokens = len(tokenizer.tokenize(chunk.text, max_length=None))
#     print(f"chunk.text ({txt_tokens} tokens):\n{repr(chunk.text)}")

#     ser_txt = chunker.serialize(chunk=chunk)
#     ser_tokens = len(tokenizer.tokenize(ser_txt, max_length=None))
#     print(f"chunker.serialize(chunk) ({ser_tokens} tokens):\n{repr(ser_txt)}")

#     print()
