import importlib
import os
import platform
import subprocess
import sys
from datetime import datetime



MIN_PYTHON_MAJOR = 3
MIN_PYTHON_MINOR = 10
REQUIRED_PACKAGES = ["pylint", "black"]
TEST_URL = "https://httpbin.org/get"
REPORT_FILE = "setup_report.txt"




def check_python_version():
    
    major = sys.version_info.major
    minor = sys.version_info.minor
    version_str = f"{major}.{minor}.{sys.version_info.micro}"

    if major > MIN_PYTHON_MAJOR or (
        major == MIN_PYTHON_MAJOR and minor >= MIN_PYTHON_MINOR
    ):
        return True, f"Python {version_str}"

    print(
        f"  ⚠  WARNING: Python {version_str} detected — "
        f"{MIN_PYTHON_MAJOR}.{MIN_PYTHON_MINOR}+ is required."
    )
    return False, f"Python {version_str} (need ≥ {MIN_PYTHON_MAJOR}.{MIN_PYTHON_MINOR})"


def check_virtual_environment():
    """Return (passed, message) confirming execution inside a venv."""
    in_venv = (
        sys.prefix != sys.base_prefix
        or os.environ.get("VIRTUAL_ENV") is not None
        or os.environ.get("CONDA_DEFAULT_ENV") is not None
    )
    if not in_venv:
        print("  ✗  ERROR: Not running inside a virtual environment.")
    return in_venv, "Inside virtual environment" if in_venv else "No virtual environment"


def list_installed_packages():
    
    result = subprocess.run(
        [sys.executable, "-m", "pip", "list", "--format=columns"],
        capture_output=True,
        text=True,
        check=False,
    )
    packages = result.stdout.strip().splitlines()
    print(f"\n  {'Package':<35} {'Version'}")
    print(f"  {'-'*35} {'-'*10}")
    for line in packages[2:]:  # skip header rows
        print(f"  {line}")
    return True, f"{len(packages) - 2} packages found"


def check_dev_tools():
    
    results = {}
    for pkg in REQUIRED_PACKAGES:
        try:
            mod = importlib.import_module(pkg)
            version = getattr(mod, "__version__", "unknown")
            results[pkg] = f"✓ {pkg} {version}"
        except Exception as exc:
            results[pkg] = f"✗ {pkg} ERROR: {exc}"

    for pkg, msg in results.items():
        print(f"  {msg}")

    all_ok = all("NOT FOUND" not in v for v in results.values())
    summary = ", ".join(
        f"{p} ({'ok' if 'NOT FOUND' not in m else 'missing'})"
        for p, m in results.items()
    )
    return all_ok, summary


def check_internet_connectivity():
    
    try:
        import requests  # pylint: disable=import-outside-toplevel

        response = requests.get(TEST_URL, timeout=5)
        if response.status_code == 200:
            return True, f"HTTP {response.status_code} from {TEST_URL}"
        return False, f"Unexpected HTTP {response.status_code}"
    except ImportError:
        return False, "'requests' package not installed"
    except Exception as exc:  # pylint: disable=broad-except
        return False, f"Connection failed: {exc}"




def run_all_checks():
    
    checks = []

    print("\n" + "=" * 60)
    print("  NEW DEVELOPER ONBOARDING CHECK")
    print("=" * 60)

    sections = [
        ("Python Version (≥ 3.10)", check_python_version),
        ("Virtual Environment", check_virtual_environment),
        ("Installed Packages", list_installed_packages),
        ("Dev Tools (pylint, black)", check_dev_tools),
        ("Internet Connectivity", check_internet_connectivity),
    ]

    for label, fn in sections:
        print(f"\n[{label}]")
        passed, detail = fn()
        status = "PASS" if passed else "FAIL"
        print(f"  → {status}: {detail}")
        checks.append((label, passed, detail))

    return checks


def generate_report(checks):
    """Write a plain-text summary report and return the file path."""
    lines = [
        "=" * 60,
        "  ONBOARDING SETUP REPORT",
        f"  Generated : {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}",
        f"  Host      : {platform.node()}",
        f"  OS        : {platform.system()} {platform.release()}",
        f"  Python    : {platform.python_version()}",
        "=" * 60,
        "",
    ]

    passed_count = 0
    for label, passed, detail in checks:
        status = "PASS" if passed else "FAIL"
        if passed:
            passed_count += 1
        lines.append(f"  [{status:4s}]  {label}")
        lines.append(f"          {detail}")
        lines.append("")

    total = len(checks)
    lines += [
        "-" * 60,
        f"  Result : {passed_count}/{total} checks passed",
        "  Status : " + ("READY TO CODE!" if passed_count == total else "✗ ACTION REQUIRED"),
        "=" * 60,
    ]

    report_text = "\n".join(lines)

    with open(REPORT_FILE, "w", encoding="utf-8") as fh:
        fh.write(report_text)

    return report_text




def main():
    """Run all onboarding checks and save the report."""
    checks = run_all_checks()

    print("\n" + "=" * 60)
    print("SUMMARY REPORT")
    print("=" * 60)
    report_text = generate_report(checks)
    print(report_text)

    print(f"\n  Full report saved to: {os.path.abspath(REPORT_FILE)}\n")


if __name__ == "__main__":
    main()



