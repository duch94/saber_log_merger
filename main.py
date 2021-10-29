import json
from typing import TextIO
from pathlib import Path

import click
from loguru import logger
from tqdm import tqdm

NEWLINE = "\n"


@click.command()
@click.argument("log1_path", type=click.Path(exists=True))
@click.argument("log2_path", type=click.Path(exists=True))
@click.option("--output", "-o", type=click.Path(exists=False))
@click.option("--verbose", "-v", is_flag=True, default=False)
def main(log1_path: Path, log2_path: Path, output: Path, verbose: bool):
    if output is None:
        output = f"{Path(log1_path).stem}_{Path(log2_path).stem}.jsonl"
    with open(log1_path, "r") as log1, open(log2_path, "r") as log2, open(output, "w") as out:
        if verbose:
            logger.info("Initializing progressbar")
            progressbar = make_progressbar(log1, log2)
        line1 = log1.readline()
        line2 = log2.readline()
        while line1 and line2:
            row1 = json.loads(line1)
            row2 = json.loads(line2)
            if row1["timestamp"] < row2["timestamp"]:
                out.writelines(json.dumps(row1) + NEWLINE)
                line1 = log1.readline()
            else:
                out.writelines(json.dumps(row2) + NEWLINE)
                line2 = log2.readline()
            if verbose:
                progressbar.update(1)
    logger.info("Log files have been merged")


def make_progressbar(file1: TextIO, file2: TextIO) -> tqdm:
    num_lines_1 = sum(1 for _ in file1)
    logger.info("File 1 contains {} lines", num_lines_1)
    num_lines_2 = sum(1 for _ in file2)
    logger.info("File 2 contains {} lines", num_lines_2)
    counter = num_lines_1 + num_lines_2
    file1.seek(0, 0)
    file2.seek(0, 0)
    logger.info("Progressbar created")
    return tqdm(range(counter))


if __name__ == "__main__":
    main()
