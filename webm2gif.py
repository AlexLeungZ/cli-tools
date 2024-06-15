from argparse import ArgumentDefaultsHelpFormatter, ArgumentParser, Namespace
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path

from moviepy.editor import VideoFileClip


class Args(Namespace):
    path: str


def get_args() -> Args:
    parser = ArgumentParser(
        formatter_class=ArgumentDefaultsHelpFormatter,
        description="Tools for converting webm to gif",
    )

    path = ["-p", "--path"]
    parser.add_argument(*path, dest="path", required=True, help="path of the directory")

    return parser.parse_args(namespace=Args())


def webm2gif(file: Path):
    clip = VideoFileClip(str(file))
    clip.write_gif(file.with_suffix(".gif"), program="ffmpeg")


def main():
    args = get_args()
    with ThreadPoolExecutor() as executor:
        executor.map(webm2gif, Path(args.path).rglob("*.webm"))


if __name__ == "__main__":
    main()
