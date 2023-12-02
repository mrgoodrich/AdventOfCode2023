import argparse
import os.path
import time
import traceback
from datetime import datetime, timedelta, timezone
from importlib import import_module, reload
from aocd import submit


def run(func, filename="filename"):
    try:
        with open(filename) as f:
            try:
                start = time.monotonic_ns()
                result = func(f)
                print(result, end="\t")
                end = time.monotonic_ns()
                print(f"[{(end-start) / 10**6:.3f} ms]")
                return result
            except:
                traceback.print_exc()
    except FileNotFoundError:
        print()


if __name__ == "__main__":
    now = datetime.now(timezone(timedelta(hours=-5)))
    parser = argparse.ArgumentParser(description="Run Advent of Code solutions.")
    parser.add_argument("--year", "-y", type=int, help="The year to run.", default=now.year)
    parser.add_argument("--day", "-d", type=int, help="The day to run.", default=now.day)
    parser.add_argument("--extra", "-e", help="Choose a different solution to run.")
    parser.add_argument("--sampleonly", "-s", action='store_true', help="Flag to only run sample.")
    parser.add_argument("--secondsample", "-ss", action='store_true', help="Flag to use sample2.")
    parser.add_argument("--submit1", "-sub1", action='store_true', help="Submit solution one")
    parser.add_argument("--submit2", "-sub2", action='store_true', help="Submit solution one")
    args = parser.parse_args()

    input_paths = {
        "sample": f"input/{args.year}/day{args.day:02}_sample.txt",
        "input": f"input/{args.year}/day{args.day:02}.txt",
    }

    if (args.secondsample):
        newsample = {
            "sample": f"input/{args.year}/day{args.day:02}_sample2.txt"
        }
        input_paths.update(newsample)
        print(input_paths)

    if not os.path.exists(input_paths["input"]):
        try:
            from aocd import get_data
        except ImportError:
            print("Error retrieving inputs with aocd")
            pass
        else:
            data = get_data(day=args.day, year=args.year)
            with open(input_paths["input"], "w") as f:
                f.write(data)

    module_name = f"py.{args.year}.day{args.day:02}"
    if args.extra:
        module_name += f"_{args.extra}"

    print(f"{module_name}")

    module = import_module(module_name)

    for i in ("p1", "p2"):
        if not hasattr(module, i):
            continue
        print(f"--- {i} ---")
        print("sample:", end="\t")
        run(getattr(module, i), input_paths["sample"])

        if not args.sampleonly:
            reload(module)
            print("input:", end="\t")
            my_answer = run(getattr(module, i), input_paths["input"])

            if args.submit1 and i == "p1":
                submit(my_answer, part="a", day=args.day, year=args.year)
            if args.submit2 and i == "p2":
                submit(my_answer, part="b", day=args.day, year=args.year)
