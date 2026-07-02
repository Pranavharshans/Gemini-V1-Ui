# Gemini-V1-Ui

Streamlit web interface for Google Gemini Pro text generation. Provides a clean UI for prompting Gemini without using the terminal.

## Setup

1. Install dependencies:
   ```bash
   pip install streamlit google-generativeai
   ```

2. Add your Gemini API key in `GeminiV1-UI.py`:
   ```python
   genai.configure(api_key='YOUR_API_KEY')
   ```

## Usage

```bash
streamlit run GeminiV1-UI.py
```

Enter a prompt in the text field and click **Generate**. The response appears on the page.

## Comparison

| Feature | Gemini-V1 | Gemini-V2 | Gemini-V1-Ui |
|---------|-----------|-----------|--------------|
| Interface | CLI | CLI | Web (Streamlit) |
| Chat history | No | Yes | No |
| Output format | Textwrap (80 cols) | Markdown | Plain text |

## Dependencies

- `streamlit`
- `google-generativeai`
