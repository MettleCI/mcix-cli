# The location of your DataStage instance
# This tutorial uses the same instance for both source and target environments
export CP4D_URL="https://cpd-dm.apps.stabledev1.dm-dev-cpd.mettleci.cloud/"  # DataStage as-a-service on IBM Cloud (or your on-premises CP4D URL)
export CP4D_USERNAME="john"                # DataStage credentials
export CP4D_API_KEY="Jyfb66orQ37TziwInhhnZvHuqJaKwqUUZIGgVAhh"                       # DataStage credentials
``
# Project names (see 'Environments and DataStage project naming')
export SOURCE_PROJECT="electromart"                  # The location of your development (source) project
export TARGET_PROJECT="mcix-cli-demo_CI"               # Demo will deploy to a 'CI' environment

# Local working folders
export EXPORT_DIR="./datastage"                  # Exported assets
export OVERLAY_DIR="./overlaid-assets"                 # Overlaid assets
export REPORT_DIR="./reports"                          # JUnit report outputs

