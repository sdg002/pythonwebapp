param([Parameter(Mandatory)][string]$version, [Parameter(Mandatory)][string]$file)
$ErrorActionPreference="Stop"
Set-StrictMode -Version "latest"

Write-Host "Begin-Replace the version in the file:$file using the version: $version"
$version | Out-File -FilePath $file -Encoding utf8
Write-Host "End-Replace the version in the file:$file using the version: $version"

