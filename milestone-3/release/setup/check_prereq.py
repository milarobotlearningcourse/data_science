#!/usr/bin/env python3
"""Check that the prerequisites for the assignment are met.

Only uses the Python standard library.
"""

import shutil
import subprocess
import sys

PROJECT_REGION = "us-central1"
REPO_NAME = "m3-images"
COURSE_CODES = ["ift3700", "ift6758b", "ift6758a"]
REQUIRED_SERVICES = {
    "Cloud Run": "run.googleapis.com",
    "Cloud Build": "cloudbuild.googleapis.com",
    "Artifact Registry": "artifactregistry.googleapis.com",
    "Secret Manager": "secretmanager.googleapis.com",
}


def fail(message: str) -> None:
    print(message)
    sys.exit(1)


def run_gcloud(gcloud: str, *args: str) -> subprocess.CompletedProcess:
    return subprocess.run(
        [gcloud, *args],
        capture_output=True,
        text=True,
    )


def select_course_code() -> str:
    print("Select your course code:")
    for i, code in enumerate(COURSE_CODES, start=1):
        print(f"  {i}) {code}")
    while True:
        choice = input(f"Enter a number (1-{len(COURSE_CODES)}): ").strip()
        if choice.isdigit() and 1 <= int(choice) <= len(COURSE_CODES):
            return COURSE_CODES[int(choice) - 1]
        print("Invalid selection, please try again.")


def main() -> None:
    course_code = select_course_code()
    team_id = input("Enter your team ID: ").strip()

    # Check if gcloud is installed
    print("Checking if gcloud is installed...")
    gcloud = shutil.which("gcloud")
    if gcloud is None:
        fail("gcloud is not installed. Please install gcloud before running this script.")

    # Check that the project is set to m3-COURSE_CODE-TEAM_ID
    project_id = f"m3-{course_code}-{team_id}"
    print(f"Checking if the project is set to {project_id}...")
    result = run_gcloud(gcloud, "config", "get-value", "project")
    project_name = result.stdout.strip()
    if project_name != project_id:
        fail(
            f"Project is not set to {project_id}. "
            f"Please set the project to {project_id} before running this script."
        )

    # Check that the required services are enabled
    result = run_gcloud(
        gcloud, "services", "list", "--enabled", "--format=value(config.name)"
    )
    enabled_services = set(result.stdout.split())
    for label, service in REQUIRED_SERVICES.items():
        print(f"Checking if {label} is enabled...")
        if service not in enabled_services:
            fail(f"{label} is not enabled. Please enable {label} before running this script.")

    # Check that a Docker registry exists with the expected setup
    repo_path = f"{PROJECT_REGION}-docker.pkg.dev/{project_id}/{REPO_NAME}"
    print("Checking if a Docker registry exists with the following setup:")
    print(f" - Location: {PROJECT_REGION}")
    print(f" - Repository: {REPO_NAME}")
    result = run_gcloud(
        gcloud,
        "artifacts",
        "repositories",
        "describe",
        REPO_NAME,
        f"--project={project_id}",
        f"--location={PROJECT_REGION}",
    )
    if result.returncode == 0:
        print(f"Repository {repo_path} exists")
    else:
        fail(f"Repository {repo_path} does not exist")

    # Everything probably worked, so we can exit with a success message and status.
    print("All prerequisites are met. You can proceed with the assignment.")
    sys.exit(0)


if __name__ == "__main__":
    main()
