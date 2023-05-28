Set-StrictMode -Version "latest"
$ErrorActionPreference="Stop"

Write-Host "Going to deploy. to be done"
Write-Host "Displaying environment variables"
Write-Host "-------------------"
dir env:
Write-Host "-------------------"
Write-Host "Displaying directory structure"
Get-ChildItem -Recurse -Path $env:PIPELINE_WORKSPACE  | Select-Object -Property FullName
Write-Host "-------------------"
