import argparse

def main():
    parser = argparse.ArgumentParser(description="Simple Hello world program")
    parser.add_argument(
        "--name",
        type=str,
        help="Your name to personalize the greeting",
        default="World"
    )
    args = parser.parse_args()
    print(f"Hello, {args.name}!")
if __name__ == "__main__":
    main()    