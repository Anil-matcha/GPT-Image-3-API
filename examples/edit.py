"""Edit an image with GPT Image 2."""

import os

from gpt_image_api import GPTImageAPI


def main():
    image_url = os.environ["MUAPI_INPUT_IMAGE_URL"]
    api = GPTImageAPI()
    job = api.edit(
        prompt="Keep the product and composition; replace the background with a warm studio set",
        images_list=[image_url],
        aspect_ratio="4:3",
        resolution="2K",
        quality="high",
    )
    print(api.wait_for_completion(job["request_id"]))


if __name__ == "__main__":
    main()
