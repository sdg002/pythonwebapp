Set-StrictMode -Version "latest"
$ErrorActionPreference="Stop"

Set-StrictMode -Version "latest"
$ErrorActionPreference="Stop"
$Global:environment="dev"
$Global:ResourceGroup="rg-python-webapp-$Global:environment-uks"
$Global:Location="uksouth"


$Global:TagDepartment="personal"
$Global:TagCostCenter="mycostcenter"
$Global:TagOwner="saurabhdasgupta@cool.com"
$Global:AppServicePlan="asp-saupythonflask001-$Global:environment"
$Global:WebAppName="app-saupythonflask001-$Global:environment"

<#
This function should be called after every invocation of Azure CLI to check for success
#>
function RaiseCliError($message){
    if ($LASTEXITCODE -eq 0){
        return
    }
    Write-Error -Message $message
}