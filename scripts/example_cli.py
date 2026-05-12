import argparse
def main():
    """Example CLI Tool"""
    parser = argparse.ArgumentParser(description="Lab Utility")
    parser.add_argument("--verbose", action="store_true")
    args = parser.parse_args()
    if args.verbose:
        print("Verbose mode on")
if __name__ == "__main__":
    main()
