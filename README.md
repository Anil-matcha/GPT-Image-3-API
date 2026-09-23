# GPT Image 3 API — Python Client and Image Generation Examples

[![Powered by MuAPI](https://img.shields.io/badge/Powered%20by-MuAPI-6366f1?style=flat-square)](https://muapi.ai)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Python 3.9+](https://img.shields.io/badge/python-3.9+-blue.svg)](https://www.python.org/)

Python and cURL examples for image generation and editing with GPT Image through MuAPI. Submit a task, poll its request ID, and retrieve the resulting image using one API key.

The runnable examples use the GPT Image 2 routes listed below.

## Related Projects

- [GPT Image 3 API on MuAPI](https://muapi.ai/gpt-image-3)
- [GPT Image API](https://muapi.ai/gpt-image) — current family endpoints and model details.
- [MuAPI](https://muapi.ai) — unified API for image, video, and audio generation.
- [MuAPI API reference](https://muapi.ai/docs/api-reference)
- [Create a MuAPI API key](https://muapi.ai/access-keys)
- [Nano Banana 3 API](https://github.com/Anil-matcha/Nano-Banana-3-API) — related image generation examples.
- [Awesome AI Image Models](https://github.com/Anil-matcha/awesome-ai-image-models) — compare image models and API options.
- [Open Generative AI](https://github.com/Anil-matcha/Open-Generative-AI) — generative-media tools and workflows.

## Installation

```bash
git clone https://github.com/Anil-matcha/GPT-Image-3-API.git
cd GPT-Image-3-API
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
export MUAPI_API_KEY="your_muapi_api_key"
```

## Text-to-image

```bash
python examples/generate.py
```

The example calls the documented GPT Image 2 route with a prompt, aspect ratio, resolution, and quality, then polls the returned request ID until the image is ready.

## API endpoints

| Workflow | MuAPI endpoint |
| --- | --- |
| Text-to-image (GPT Image 2) | `POST /api/v1/gpt-image-2-text-to-image` |
| Image editing (GPT Image 2) | `POST /api/v1/gpt-image-2-image-to-image` |
| Result polling | `GET /api/v1/predictions/{request_id}/result` |

The base URL is `https://api.muapi.ai`. The live [GPT Image API page](https://muapi.ai/gpt-image) documents supported request fields and current availability.

## License

MIT. See [LICENSE](LICENSE).
