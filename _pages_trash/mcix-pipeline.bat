@echo off
setlocal enabledelayedexpansion

set "SOURCE_CP4D_URL=https://source-cpd.example.com"
set "SOURCE_PROJECT=Development"

set "TARGET_CP4D_URL=https://target-cpd.example.com"
set "TARGET_PROJECT=Test"

set "CP4D_USERNAME=john@example.com"
set "CP4D_API_KEY=your-api-key"

set "EXPORT_DIR=.\exported-assets"
set "OVERLAY_DIR=.\overlaid-assets"
set "REPORT_DIR=.\reports"

if not exist "%EXPORT_DIR%" mkdir "%EXPORT_DIR%"
if not exist "%OVERLAY_DIR%" mkdir "%OVERLAY_DIR%"
if not exist "%REPORT_DIR%" mkdir "%REPORT_DIR%"

echo Exporting DataStage assets...
mcix datastage export ^
  --url "%SOURCE_CP4D_URL%" ^
  --project "%SOURCE_PROJECT%" ^
  --username "%CP4D_USERNAME%" ^
  --api-key "%CP4D_API_KEY%" ^
  --output-dir "%EXPORT_DIR%"

if errorlevel 1 exit /b %errorlevel%

echo Applying overlays...
mcix overlay apply ^
  --input-dir "%EXPORT_DIR%" ^
  --overlay-dir ".\overlays\test" ^
  --output-dir "%OVERLAY_DIR%"

if errorlevel 1 exit /b %errorlevel%

echo Importing DataStage assets...
mcix datastage import ^
  --url "%TARGET_CP4D_URL%" ^
  --project "%TARGET_PROJECT%" ^
  --username "%CP4D_USERNAME%" ^
  --api-key "%CP4D_API_KEY%" ^
  --input-dir "%OVERLAY_DIR%"

if errorlevel 1 exit /b %errorlevel%

echo Running asset analysis tests...
mcix asset-analysis test ^
  --url "%TARGET_CP4D_URL%" ^
  --project "%TARGET_PROJECT%" ^
  --username "%CP4D_USERNAME%" ^
  --api-key "%CP4D_API_KEY%" ^
  --rules-dir ".\asset-analysis-rules" ^
  --junit-output "%REPORT_DIR%\asset-analysis-results.xml"

if errorlevel 1 exit /b %errorlevel%

echo Running unit tests...
mcix unit-test execute ^
  --url "%TARGET_CP4D_URL%" ^
  --project "%TARGET_PROJECT%" ^
  --username "%CP4D_USERNAME%" ^
  --api-key "%CP4D_API_KEY%" ^
  --junit-output "%REPORT_DIR%\unit-test-results.xml"

if errorlevel 1 exit /b %errorlevel%

echo Pipeline completed successfully.
echo Asset analysis report: %REPORT_DIR%\asset-analysis-results.xml
echo Unit test report:      %REPORT_DIR%\unit-test-results.xml

endlocal