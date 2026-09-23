"""Generate an image through MuAPI's GPT Image endpoint."""

from gpt_image_api import GPTImageAPI


def main():
    api = GPTImageAPI()
    job = api.generate(
        prompt="A minimalist travel poster of a red tram in Lisbon at sunset",
        aspect_ratio="16:9",
        resolution="1K",
        quality="medium",
    )
    request_id = job["request_id"]
    print(f"Submitted request: {request_id}")
    print(api.wait_for_completion(request_id))


if __name__ == "__main__":
    main()
