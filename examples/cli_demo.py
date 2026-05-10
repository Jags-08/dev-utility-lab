import subprocess

def cli_task() -> None:
    print("Running CLI command programmatically...")
    result = subprocess.run(["dev-utils", "factorial", "6"], capture_output=True, text=True)
    print(f"CLI Output: {result.stdout.strip()}")

if __name__ == "__main__":
    cli_task()
