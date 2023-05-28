. $PSScriptRoot/commonvariables.ps1


# YOU WERE HERE
# BRING IN ALL ARM TEMPLATES , 
# PUT THE TEMPLATE+PARAMETER FILES IN THEIR RESPSECTIVE SUB-FOLDERS

<#
Deploy resource group
#>
Write-Host "Going to create the resource group: '$Global:ResourceGroup' with the location: '$Global:Location' "
& az group create --location $Global:Location --name $Global:ResourceGroup `
    --tags department=$Global:TagDepartment owner=$Global:TagOwner costcenter=$Global:TagCostCenter
RaiseCliError -message "Failed to create the resource group $Global:ResourceGroup"



Write-Host "Going to deploy. to be done"
Write-Host "Displaying environment variables"
Write-Host "-------------------"
dir env:
Write-Host "-------------------"
Write-Host "Displaying directory structure"
Get-ChildItem -Recurse -Path $env:PIPELINE_WORKSPACE  | Select-Object -Property FullName
Write-Host "-------------------"
