#!/bin/bash
REGION="us-central1"
PROJECT_ID="" # FILL ME IN


# This makes sure that we are uploading our code from the proper path.
# Don't change this line.
SCRIPT_DIR=$( cd -- "$( dirname -- "${BASH_SOURCE[0]}" )" &> /dev/null && pwd )

REPO_NAME="" # FILL ME IN
REGISTRY="us-central1-docker.pkg.dev"
IMAGE_NAME="nhl-streamlit-app"
SERVING_IMAGE_NAME="nhl-serving-app" # IFT6758 only

# It's not expected to know bash scripting to the level below.
# The following is known as substitutions in cloud build.

REPO_URI="${REGISTRY}/${PROJECT_ID}/${REPO_NAME}"

# IFT6758 only: replace the --substitutions line below with
#   --substitutions=_IMAGE_URI="${REPO_URI}/${IMAGE_NAME}",_SERVING_IMAGE_URI="${REPO_URI}/${SERVING_IMAGE_NAME}" \
gcloud builds submit \
    --region=${REGION} \
    --config="${SCRIPT_DIR}/cloudbuild.yaml" \
    --substitutions=_IMAGE_URI="${REPO_URI}/${IMAGE_NAME}" \
    ${SCRIPT_DIR}/../
