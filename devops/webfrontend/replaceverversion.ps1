param([Parameter(Mandatory)][string]$version, [Parameter(Mandatory)][string]$file)
$ErrorActionPreference="Stop"
Set-StrictMode -Version "latest"

Write-Host "Begin-Replace the version in the file:$file using the version: $version"
$version | Out-File -FilePath $file
Write-Host "End-Replace the version in the file:$file using the version: $version"
Write-Host "Displaying the contents"
Get-Content -Path $file -Raw
