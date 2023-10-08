import subprocess
import sys
from pathlib import Path

HERE = Path(__file__).parent
SRC = HERE / "src"
COV_FAIL_UNDER = 82

OR_JOIN = " or ".join
# mostly to avoid external assets
M_SKIPS = ["external", "samples"]
K_SKIPS = [
    # mostly extneral assets
    "ASurveyofImageClassificationBasedTechniques",
    "encrypt_stream_dictionary",
    "escapedcode_followed_by_int",
    "image_similarity",
    "iss1710",
    "multi_language",
    "old_habibi",
    "pdfa",
    # py312:  a bytes-like object is required, not 'str'
    "merging_many_temporary_files",
]

PYTEST_ARGS = [
    sys.executable,
    "pytest",
    "-vv",
    "--color=yes",
    "-m",
    f"not ({OR_JOIN(M_SKIPS)})",
    "-k",
    f"not ({OR_JOIN(K_SKIPS)})",
    "--cov=pypdf",
    "--cov-branch",
    "--cov-report=term-missing:skip-covered",
    "--no-cov-on-fail",
    f"--cov-fail-under={COV_FAIL_UNDER}"
]

if __name__ == "__main__":
    print(">>> ", "\t".join(PYTEST_ARGS), flush=True)
    sys.exit(subprocess.call(PYTEST_ARGS, cwd=str(SRC)))
