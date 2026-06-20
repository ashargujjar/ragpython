# Custom PDF Q&A Bot using RAG (LangChain & FAISS)

A lightweight Retrieval-Augmented Generation (RAG) pipeline built using Python and LangChain. This application reads content from a local PDF file, processes it into semantic chunks, stores it in a local high-performance vector database (FAISS), and allows you to ask natural language questions against the document's content using OpenAI's `gpt-4o-mini`.

---

## Features

* **PDF Parsing**: Automatically extracts and parses text content page-by-page from local PDF documents.
* **Smart Text Splitting**: Uses chunk overlapping techniques to ensure no context is lost across chunk boundaries.
* **Local Vector Storage**: Leverages Meta's FAISS library to index and retrieve document snippets completely locally in milliseconds.
* **Modern LangChain (LCEL)**: Built using the optimized LangChain Expression Language for clean and reliable pipeline execution.
* **Secure Environment Management**: Uses environment variables to safeguard sensitive API credentials.

---

##  Tech Stack & Dependencies

* **Language:** Python 3.11+
* **Framework:** LangChain (Core, Community, OpenAi, Text-Splitters)
* **Vector Store:** FAISS (CPU variant)
* **LLM Provider:** OpenAI (`gpt-4o-mini` & `text-embedding-3-small`)

---

##  Prerequisites & Installation

### 1. Clone the repository
\`\`\`bash
git clone <your-github-repo-url>
cd <your-repo-folder-name>
\`\`\`

**Output:**
<img width="1212" height="571" alt="Terminal Output" src="https://github.com/user-attachments/assets/6490aa87-4ec2-48e7-aab1-2e82e2ddcfd6" />
