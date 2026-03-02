import argparse
import sys
import time
import subprocess
import shutil
from importlib.metadata import distributions, PackageNotFoundError

# =============================
# Timer Decorator
# =============================
def timed_check(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        return result, end - start
    return wrapper


# =============================
# Python Version Check
# =============================
@timed_check
def check_python_version(verbose=False):
    version = sys.version_info
    if verbose:
        print(f"Using Python: {version.major}.{version.minor}.{version.micro}")
        print(f"Interpreter path: {sys.executable}")

    if version.major >= 3 and version.minor >= 8:
        return True
    else:
        print("[ERROR] Python 3.8 or higher is required")
        return False


# =============================
# Package Check
# =============================
REQUIRED_PACKAGES = ["pylint", "black"]

@timed_check
def check_packages(verbose=False, fix=False):
    installed = {dist.metadata["Name"].lower() for dist in distributions()}
    missing = []

    for pkg in REQUIRED_PACKAGES:
        if pkg.lower() in installed:
            if verbose:
                print(f"[OK] {pkg} installed")
        else:
            print(f"[MISSING] {pkg}")
            missing.append(pkg)

    # Auto-fix if requested
    if missing and fix:
        print("Installing missing packages...")
        for pkg in missing:
            subprocess.check_call([sys.executable, "-m", "pip", "install", pkg])

        # Re-check after install
        installed = {dist.metadata["Name"].lower() for dist in distributions()}
        missing = [pkg for pkg in REQUIRED_PACKAGES if pkg.lower() not in installed]

    return len(missing) == 0


# =============================
# Disk Space Check
# =============================
@timed_check
def check_disk_space(verbose=False):
    total, used, free = shutil.disk_usage("/")
    free_gb = free / (1024 ** 3)

    if verbose:
        print(f"Free disk space: {free_gb:.2f} GB")

    if free_gb < 1:
        print("[WARNING] Less than 1 GB disk space available")
        return False

    return True


# =============================
# Main
# =============================
def main():
    parser = argparse.ArgumentParser(description="Environment Onboarding Script")
    parser.add_argument("--verbose", action="store_true", help="Show detailed output")
    parser.add_argument("--fix", action="store_true", help="Install missing packages automatically")
    args = parser.parse_args()

    print("Starting onboarding checks...\n")
    total_start = time.time()

    checks = [
        ("Python Version", check_python_version, {"verbose": args.verbose}),
        ("Packages", check_packages, {"verbose": args.verbose, "fix": args.fix}),
        ("Disk Space", check_disk_space, {"verbose": args.verbose})
    ]

    results = []

    for name, func, kwargs in checks:
        success, duration = func(**kwargs)
        results.append((name, success))
        print(f"{name}: {'PASS' if success else 'FAIL'} ({duration:.2f}s)")

    total_time = time.time() - total_start

    print("\n--- Summary ---")
    for name, success in results:
        print(f"{name}: {'PASS' if success else 'FAIL'}")

    print(f"\nTotal execution time: {total_time:.2f} seconds")


if __name__ == "__main__":
    main()