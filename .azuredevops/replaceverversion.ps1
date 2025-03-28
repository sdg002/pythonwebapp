<#
Replace the pattern in a specific Python file with the specified version number.
#>
param([Parameter(Mandatory)][string]$version, [Parameter(Mandatory)][string]$file)
$ErrorActionPreference="Stop"
Set-StrictMode -Version "latest"

$content = Get-Content -Path $file

# Replace the pattern with the new string
$pattern =  "0.0.0"
$replacement = $version
$newContent = $content -replace $pattern, $replacement

# Write the updated content back to the file
Set-Content -Path $file -Value $newContent
