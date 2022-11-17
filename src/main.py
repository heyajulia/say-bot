import subprocess

import mastodon
from bs4 import BeautifulSoup


def strip_html(text: str) -> str:
    return BeautifulSoup(text, "html.parser").text


def text_to_wav(text: str) -> bytes:
    process = subprocess.run(
        ["text2wave"],
        input=text.encode(),
        stdout=subprocess.PIPE,
        check=True,
        timeout=1.0,
    )

    return process.stdout


def main() -> None:
    mastodon_client = mastodon.Mastodon(api_base_url="https://mastodon.lol")
    status = mastodon_client.status(109357872779540083)
    text_html = status["content"]
    text = strip_html(text_html)
    wav_data = text_to_wav(text)

    with open("post.wav", "wb+") as f:
        f.write(wav_data)


if __name__ == "__main__":
    main()
