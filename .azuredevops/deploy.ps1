. $PSScriptRoot/commonvariables.ps1


# YOU WERE HERE
# BRING IN ALL ARM TEMPLATES , 
# PUT THE TEMPLATE+PARAMETER FILES IN THEIR RESPSECTIVE SUB-FOLDERS

<#
Deploy resource group
#>
Write-Host "Going to create the resource group: '$Global:ResourceGroup' with the location: '$Global:Location' "
& az group create --location $Global:Location --name $Global:ResourceGroup `
    --tags department=$Global:TagDepartment owner=$Global:TagOwner costcenter=$Global:TagCostCenter location=$Global:Location
RaiseCliError -message "Failed to create the resource group $Global:ResourceGroup"


<#
Deploy App Service Plan
#>
$bicepTemplateFile = Join-Path -Path $PSScriptRoot -ChildPath "templates/appserviceplan.bicep"
Write-Host "Going to create App Service Plan $Global:AppServicePlan using bicep template $bicepTemplateFile"
& az deployment group create --resource-group $Global:ResourceGroup `
    --template-file $bicepTemplateFile `
    --parameters `
    name=$Global:AppServicePlan `
    --verbose
RaiseCliError -message "Failed to create app service plan $Global:AppServicePlan"

<#
Deploy Web app
#>
$bicepTemplateFile = Join-Path -Path $PSScriptRoot -ChildPath "templates/webapp.bicep"
Write-Host "Going to create a web app using template $bicepTemplateFile"
& az deployment group create --resource-group $Global:ResourceGroup --template-file $bicepTemplateFile `
    --parameters `
    name=$Global:WebAppName hostingPlanName=$Global:AppServicePlan `
    environment=$Global:environment `
    --verbose

RaiseCliError -message "Failed to deploy web app $Global:WebAppName"

<#
Deploy the Python code
#>
Write-Host "Going to deploy upload Python code to the web app $Global:WebAppName"
$SourceFolder = "src"
$SourceCodeLocation = Join-Path -Path $PSScriptRoot -ChildPath "../$SourceFolder"
$SourceCodeLocation = Resolve-Path -Path $SourceCodeLocation

$DotAzureFolder = Join-Path -Path $SourceCodeLocation -ChildPath ".azure"  #This is a cache folder created by Azure Cli created on local desktops
if (Test-Path -Path $DotAzureFolder) {
    Remove-Item -Path $DotAzureFolder -Recurse -Force -Verbose
}

Write-Host "The Python code will be deployed from the location $SourceCodeLocation"
Push-Location -Path $SourceCodeLocation
az webapp up --name $Global:WebAppName --runtime "PYTHON:3.10"
Pop-Location

Write-Host "Deployment-done"
Write-Host "-------------------"


