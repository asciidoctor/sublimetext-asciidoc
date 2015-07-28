#!/bin/bash

# Exit if any statement returns a non-true return value.
set -e

# Go to the project's root directory.
cd "$(dirname "$0")/.."

echo '==> Installing development dependencies...'
pip install -r requirements-dev.txt | sed -n '/Requirement already satisfied/!p'

exit ${PIPESTATUS[0]}  # exit status of pip install
