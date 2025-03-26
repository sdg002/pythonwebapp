. $PSScriptRoot/commonvariables.ps1

Write-Host "hello"
Write-Host "$Global:AppServicePlan"

#az webapp create -g $Global:ResourceGroup --plan $Global:AppServicePlan --name "sau00123" --runtime "PYTHON:3.11" --verbose
$SourceFolder = "webfrontend"
$SourceCodeLocation = Join-Path -Path $PSScriptRoot -ChildPath "../../$SourceFolder"
write-Host $SourceCodeLocation
$SourceCodeLocation = Resolve-Path -Path $SourceCodeLocation
write-Host $SourceCodeLocation
Push-Location -Path $SourceCodeLocation
#Step-1 Ran the following and created the Plan
#az webapp up --resource-group $Global:ResourceGroup --runtime "PYTHON:3.11" --name "sau00123" --location "uksouth" --verbose --sku F1

#Step-2 Ran the following and created the WebApp , ensure you are on the right path
az webapp up --name "sau00123"  --verbose --plan saurabh_dasgupta_asp_7636 --resource-group $Global:ResourceGroup
Pop-Location


