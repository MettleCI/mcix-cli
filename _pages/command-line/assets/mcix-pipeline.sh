#!/usr/bin/env bash

# DataStage NextGen CI/CD pipeline example using the MCIX CLI
# See http://cli.mettleci.io/ for more details on the MCIX CLI and its capabilities.

set -euo pipefail

# The location of your DataStage instance
# This tutorial uses the same instance for both source and target environments
export CP4D_URL="https://dataplatform.cloud.ibm.com/"  # DataStage as-a-service on IBM Cloud (or your on-premises CP4D URL)
export CP4D_USERNAME="myname@MyOrg.com"                # DataStage credentials
export CP4D_API_KEY="my-api-key"                       # DataStage credentials
``
# Project names (see 'Environments and DataStage project naming')
export SOURCE_PROJECT="mcix-cli-demo"                  # The location of your development (source) project
export TARGET_PROJECT="mcix-cli-demo_CI"               # Demo will deploy to a 'CI' environment

# Local working folders
export EXPORT_DIR="./exported-assets"                  # Exported assets
export OVERLAY_DIR="./overlaid-assets"                 # Overlaid assets
export REPORT_DIR="./reports"                          # JUnit report outputs

mkdir -p "$EXPORT_DIR"
mkdir -p "$OVERLAY_DIR"
mkdir -p "$REPORT_DIR"

echo "Exporting DataStage assets..."
mcix datastage export \
  -url         "$CP4D_URL" \
  -project     "$SOURCE_PROJECT" \
  -user        "$CP4D_USERNAME" \
  -api-key     "$CP4D_API_KEY" \
  -export-path "$EXPORT_DIR"

echo "Applying overlays..."
mcix overlay apply \
  -input-dir   "$EXPORT_DIR" \
  -overlay-dir "./overlays/test" \
  -output-dir  "$OVERLAY_DIR"

echo "Importing DataStage assets..."
mcix datastage import \
  -url         "$CP4D_URL" \
  -project     "$TARGET_PROJECT" \
  -user        "$CP4D_USERNAME" \
  -api-key     "$CP4D_API_KEY" \
  -input-dir   "$OVERLAY_DIR"

# This is included for completeness, and future use, but the asset analysis
# tests cannot be run until they are fully supported in IBM DataStage.
#
# echo "Running asset analysis tests..."
# mcix asset-analysis test \
#   -url          "$CP4D_URL" \
#   -project      "$TARGET_PROJECT" \
#   -user.        "$CP4D_USERNAME" \
#   -api-key      "$CP4D_API_KEY" \
#   -rules-dir    "./asset-analysis-rules" \
#   -junit-output "$REPORT_DIR/asset-analysis-results.xml"

echo "Running unit tests..."
mcix unit-test execute \
  -url          "$CP4D_URL" \
  -project      "$TARGET_PROJECT" \
  -user        "$CP4D_USERNAME" \
  -api-key      "$CP4D_API_KEY" \
  -junit-output "$REPORT_DIR/unit-test-results.xml"

echo "Pipeline completed successfully."
echo "Asset analysis report: $REPORT_DIR/asset-analysis-results.xml"
echo "Unit test report:      $REPORT_DIR/unit-test-results.xml"