# GPT Image 3 API — Python Client and Image Generation Examples

[![Powered by MuAPI](https://img.shields.io/badge/Powered%20by-MuAPI-6366f1?style=flat-square)](https://muapi.ai)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Python 3.9+](https://img.shields.io/badge/python-3.9+-blue.svg)](https://www.python.org/)

Generate and edit images with GPT Image through MuAPI. This repository includes a reusable Python client, text-to-image and image-edit examples, and cURL requests. MuAPI uses an asynchronous submit-and-poll workflow: generation calls return a request ID, and a separate result request returns the finished image.

The examples use the GPT Image 2 routes currently documented in the MuAPI catalog.

## Related Projects

- [GPT Image 3 API on MuAPI](https://muapi.ai/gpt-image-3)
- [GPT Image API](https://muapi.ai/gpt-image) — live family models, API details, and pricing.
- [MuAPI API reference](https://muapi.ai/docs/api-reference)
- [MuAPI API keys](https://muapi.ai/access-keys)
- [Nano Banana 3 API](https://github.com/Anil-matcha/Nano-Banana-3-API) — related image generation and editing examples.
- [Awesome AI Image Models](https://github.com/Anil-matcha/awesome-ai-image-models) — compare image models and API providers.
- [Open Generative AI](https://github.com/Anil-matcha/Open-Generative-AI) — generative-media tools and workflows.

## Features

- GPT Image 2 text-to-image generation.
- GPT Image 2 instruction-based image editing with up to 16 reference images.
- Aspect ratio, output resolution, and quality controls.
- A reusable Python client with request submission, task polling, and error handling.
- Copy-paste cURL examples for both API workflows.

## Installation

```bash
git clone https://github.com/Anil-matcha/GPT-Image-3-API.git
cd GPT-Image-3-API
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
export MUAPI_API_KEY="your_muapi_api_key"
```

The examples require Python 3.9+ and `requests`. You can also copy `.env.example` to `.env` and load it with your preferred environment-variable tool.

## Text-to-image

Run the included example:

```bash
python -m examples.generate
```

Or call the Python client directly:

```python
from gpt_image_api import GPTImageAPI

api = GPTImageAPI()  # Reads MUAPI_API_KEY from the environment
job = api.generate(
    prompt="A minimalist travel poster of a red tram in Lisbon at sunset",
    aspect_ratio="16:9",
    resolution="2K",
    quality="high",
)

result = api.wait_for_completion(job["request_id"])
print(result)
```

## Image editing

Pass one or more public source-image URLs and an instruction describing the edit. Up to 16 images can be included in `images_list`.

To run the included edit example, set a public input image URL:

```bash
export MUAPI_INPUT_IMAGE_URL="https://example.com/product.jpg"
python -m examples.edit
```

```python
from gpt_image_api import GPTImageAPI

api = GPTImageAPI()
job = api.edit(
    prompt="Keep the product and composition; replace the background with a warm studio set",
    images_list=["https://example.com/product.jpg"],
    aspect_ratio="4:3",
    resolution="2K",
    quality="high",
)
result = api.wait_for_completion(job["request_id"])
print(result)
```

For local files, first upload the image using MuAPI's [file upload endpoint](https://muapi.ai/docs/api-reference), then pass the returned URL in `images_list`.

## cURL

Text-to-image:

```bash
curl -X POST "https://api.muapi.ai/api/v1/gpt-image-2-text-to-image" \
  -H "x-api-key: ${MUAPI_API_KEY}" \
  -H "Content-Type: application/json" \
  -d '{
    "prompt": "A minimalist travel poster of a red tram in Lisbon at sunset",
    "aspect_ratio": "16:9",
    "resolution": "2K",
    "quality": "high"
  }'
```

Image edit:

```bash
curl -X POST "https://api.muapi.ai/api/v1/gpt-image-2-image-to-image" \
  -H "x-api-key: ${MUAPI_API_KEY}" \
  -H "Content-Type: application/json" \
  -d '{
    "prompt": "Keep the product and composition; replace the background with a warm studio set",
    "images_list": ["https://example.com/product.jpg"],
    "aspect_ratio": "4:3",
    "resolution": "2K",
    "quality": "high"
  }'
```

Each submission returns a `request_id`. Poll for the final status and output:

```bash
curl "https://api.muapi.ai/api/v1/predictions/REQUEST_ID/result" \
  -H "x-api-key: ${MUAPI_API_KEY}"
```

## API reference

Base URL: `https://api.muapi.ai/api/v1`

| Workflow | Method and route | Required fields |
| --- | --- | --- |
| Text-to-image | `POST /gpt-image-2-text-to-image` | `prompt` |
| Image edit | `POST /gpt-image-2-image-to-image` | `prompt`, `images_list` |
| Poll for result | `GET /predictions/{request_id}/result` | Path parameter `request_id` |

Every request uses the `x-api-key` header. Image generation and editing calls accept JSON and return a request ID for polling.

### Request parameters

| Field | Generation | Editing | Values and limits |
| --- | --- | --- | --- |
| `prompt` | Required | Required | Text instruction; maximum 20,000 characters |
| `images_list` | — | Required | Array of 1–16 publicly accessible image URLs |
| `aspect_ratio` | Optional | Optional | Generation: `auto`, `1:1`, `16:9`, `9:16`, `4:3`, `3:4`, `3:2`, `2:3`, `5:4`, `4:5`. Editing: `auto`, `1:1`, `16:9`, `9:16`, `4:3`, `3:4`. Default `auto`. |
| `resolution` | Optional | Optional | `1K`, `2K`, `4K`; default `2K` |
| `quality` | Optional | Optional | `low`, `medium`, `high`; default `high` |

**Resolution constraints:** `auto` aspect ratio only supports 1K. A 1:1 output cannot be converted to 4K. Choose a supported aspect ratio and resolution pair or the task may fail validation.

See the [GPT Image API page](https://muapi.ai/gpt-image) for live route availability and current pricing.

## Asynchronous workflow

1. Submit a generation or edit request with your MuAPI API key.
2. Store the `request_id` from the response.
3. Poll `/api/v1/predictions/{request_id}/result`, or call `wait_for_completion` in the Python client.
4. When status is `completed`, read the image URL from the result. If it is `failed`, inspect the returned error details.

For production applications, poll from a worker or use MuAPI webhooks where available instead of holding a browser request open.

## Errors and practical notes

- HTTP errors from rejected submission or polling requests are raised by `requests.raise_for_status()`.
- A successful submission response means the task was accepted; keep polling until it reaches a terminal status.
- Input images must be reachable by MuAPI. Upload local images before submitting an edit job.
- Keep `MUAPI_API_KEY` in an environment variable or secret store; never commit credentials.
- Check the live [GPT Image API page](https://muapi.ai/gpt-image) for current route availability, parameter constraints, and pricing.

## License

MIT. See [LICENSE](LICENSE).
