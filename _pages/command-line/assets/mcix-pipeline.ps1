# DataStage NextGen CI/CD pipeline example using the MCIX CLI
# See http://cli.mettleci.io/ for more details on the MCIX CLI and its capabilities.

$ErrorActionPreference = "Stop"
$PSNativeCommandUseErrorActionPreference = $true

# The location of your DataStage instance
# This tutorial uses the same instance for both source and target environments
$CP4D_URL        = "https://dataplatform.cloud.ibm.com/"  # DataStage as-a-service on IBM Cloud (or your on-premises CP4D URL)
$CP4D_USERNAME   = "myname@MyOrg.com"                     # DataStage credentials
$CP4D_API_KEY    = "my-api-key"                           # DataStage credentials

# Project names (see 'Environments and DataStage project naming')
$SOURCE_PROJECT  = "mcix-cli-demo"                        # The location of your development (source) project
$TARGET_PROJECT  = "mcix-cli-demo_CI"                     # Demo will deploy to a 'CI' environment

# Local working folders
$EXPORT_DIR      = "./exported-assets"                    # Exported assets
$OVERLAY_DIR     = "./overlaid-assets"                    # Overlaid assets
$REPORT_DIR      = "./reports"                            # JUnit report outputs

New-Item -ItemType Directory -Force -Path $EXPORT_DIR  | Out-Null
New-Item -ItemType Directory -Force -Path $OVERLAY_DIR | Out-Null
New-Item -ItemType Directory -Force -Path $REPORT_DIR  | Out-Null

Write-Host "Exporting DataStage assets..."
mcix datastage export `
  --url $SOURCE_CP4D_URL `
  --project $SOURCE_PROJECT `
  --user $CP4D_USERNAME `
  --api-key $CP4D_API_KEY `
  --output-dir $EXPORT_DIR

Write-Host "Applying overlays..."
mcix overlay apply `
  --input-dir $EXPORT_DIR `
  --overlay-dir ".\overlays\test" `
  --output-dir $OVERLAY_DIR

Write-Host "Importing DataStage assets..."
mcix datastage import `
  --url $TARGET_CP4D_URL `
  --project $TARGET_PROJECT `
  --user $CP4D_USERNAME `
  --api-key $CP4D_API_KEY `
  --input-dir $OVERLAY_DIR

Write-Host "Running asset analysis tests..."
mcix asset-analysis test `
  --url $TARGET_CP4D_URL `
  --project $TARGET_PROJECT `
  --user $CP4D_USERNAME `
  --api-key $CP4D_API_KEY `
  --rules-dir ".\asset-analysis-rules" `
  --junit-output "$REPORT_DIR\asset-analysis-results.xml"

Write-Host "Running unit tests..."
mcix unit-test execute `
  --url $TARGET_CP4D_URL `
  --project $TARGET_PROJECT `
  --user $CP4D_USERNAME `
  --api-key $CP4D_API_KEY `
  --junit-output "$REPORT_DIR\unit-test-results.xml"

Write-Host "Pipeline completed successfully."
Write-Host "Asset analysis report: $REPORT_DIR\asset-analysis-results.xml"
Write-Host "Unit test report:      $REPORT_DIR\unit-test-results.xml"