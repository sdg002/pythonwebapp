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
$armTemplateFile=Join-Path -Path $PSScriptRoot -ChildPath "templates/appserviceplan.arm.template.json"
$armParameterFile=Join-Path -Path $PSScriptRoot -ChildPath "templates/appserviceplan.arm.parameters.json"
Write-Host "Going to create App Service Plan $Global:AppServicePlan using ARM template $armTemplateFile"
& az deployment group create --resource-group $Global:ResourceGroup `
    --template-file $armTemplateFile `
    --parameters  @$armParameterFile `
    name=$Global:AppServicePlan `
    --verbose

RaiseCliError -message "Failed to create app service plan $Global:AppServicePlan"

<#
Deploy Web app
#>
$armTemplateFile=Join-Path -Path $PSScriptRoot -ChildPath "templates/webapp.arm.template.json"
$armParameterFile=Join-Path -Path $PSScriptRoot -ChildPath "templates/webapp.arm.parameters.json"
Write-Host "Going to create a web app using ARM template $armTemplateFile"
& az deployment group create --resource-group $Global:ResourceGroup --template-file $armTemplateFile `
    --parameters @$armParameterFile  `
    name=$Global:WebAppName hostingPlanName=$Global:AppServicePlan `
    environment=$Global:environment `
    --verbose

RaiseCliError -message "Failed to deploy web app $Global:WebAppName"

<#
Deploy the Python code
#>
Write-Host "Going to deploy upload Python code to the web app $Global:WebAppName"
$SourceFolder="webfrontend"
$SourceCodeLocaiton = Join-Path -Path $PSScriptRoot -ChildPath "../../$SourceFolder"

$DotAzureFolder=Join-Path -Path $SourceCodeLocaiton -ChildPath ".azure"  #This is a cache folder created by Azure Cli
if (Test-Path -Path $DotAzureFolder){
    Remove-Item -Path $DotAzureFolder -Recurse -Force -Verbose
}

Write-Host "The Python code will be deployed from the location $SourceCodeLocaiton"
Push-Location -Path $SourceCodeLocaiton
az webapp up --name $Global:WebAppName
Pop-Location

Write-Host "Going to deploy. to be done"
Write-Host "Displaying environment variables"
Write-Host "-------------------"
dir env:
Write-Host "-------------------"
Write-Host "Displaying directory structure"
Get-ChildItem -Recurse -Path $env:PIPELINE_WORKSPACE  | Select-Object -Property FullName
Write-Host "-------------------"


