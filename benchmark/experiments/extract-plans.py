from pathlib import Path
import re
import tqdm

PATTERN = re.compile(r"""
\[.*?\] \ SYMBA: \ Printing \ plan \ to \ stdout \ [.][.][.] \n
(?: ;;.*\n)*?
( [(](?: .|\n)*? )
\[.*?\] \ SYMBA: \ END
""",
re.VERBOSE
)

def handle_file(fpath):
    with open(fpath) as f:
        bigstring = f.read()  # I've seen at most 2 GB (for l20), the RAM should handle it
    progressbar = tqdm.tqdm(total = len(bigstring), unit="chars")
    found_plans = 0
    m = re.search(PATTERN, bigstring)
    with open(fpath.parent / "plans.txt", "w") as f:
        f.write("="*32 + "\n")
        while m is not None:
            f.write(m.group(1))
            f.write("="*32 + "\n")
            progressbar.update(m.end())
            found_plans += 1
            bigstring = bigstring[m.end():]
            m = re.search(PATTERN, bigstring)
    print("Found", found_plans, "plans.")


def extract_plans(directory):
    if not isinstance(directory, Path):
        directory = Path(directory)
    for fpath in directory.rglob("stdout.txt"):
        print("Handling", fpath)
        handle_file(fpath)

if __name__ == "__main__":
    extract_plans(Path(__file__).parent.parent.parent / "cpddl-REAL-l20")
