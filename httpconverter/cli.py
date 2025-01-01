import argparse
from httpconverter.main import HTTPConverter

def main():
    parser = argparse.ArgumentParser(description="Convert HTTP-like files into Python requests code.")
    parser.add_argument("--file", required=True, help="Path to the input file (e.g., filename.xml).")
    parser.add_argument("--output", required=True, help="Path to the output Python file.")
    parser.add_argument("--use_oop", action="store_true", help="Use OOP for function generation.")
    parser.add_argument("--force_dicts", action="store_true", help="Force arguments and headers to be dictionaries.")

    args = parser.parse_args()

    # Initialize HTTPConverter
    converter = HTTPConverter(file=args.file)

    # Extract requests
    converter.extract(use_oop=args.use_oop, filename=args.output, force_dicts=args.force_dicts)
    print(f"File converted and saved to {args.output}")

if __name__ == "__main__":
    main()
