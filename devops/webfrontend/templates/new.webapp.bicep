param sites_sau00123_name string = 'sau00123'
param serverfarms_saurabh_dasgupta_asp_7636_externalid string = '/subscriptions/635a2074-cc31-43ac-bebe-2bcd67e1abfe/resourceGroups/rg-python-webapp-dev-uks/providers/Microsoft.Web/serverfarms/saurabh_dasgupta_asp_7636'

resource sites_sau00123_name_resource 'Microsoft.Web/sites@2024-04-01' = {
  name: sites_sau00123_name
  location: 'UK South'
  kind: 'app,linux'
  properties: {
    enabled: true
    hostNameSslStates: [
      {
        name: '${sites_sau00123_name}.azurewebsites.net'
        sslState: 'Disabled'
        hostType: 'Standard'
      }
      {
        name: '${sites_sau00123_name}.scm.azurewebsites.net'
        sslState: 'Disabled'
        hostType: 'Repository'
      }
    ]
    serverFarmId: serverfarms_saurabh_dasgupta_asp_7636_externalid
    reserved: true
    isXenon: false
    hyperV: false
    dnsConfiguration: {}
    vnetRouteAllEnabled: false
    vnetImagePullEnabled: false
    vnetContentShareEnabled: false
    siteConfig: {
      numberOfWorkers: 1
      linuxFxVersion: 'PYTHON|3.10'
      acrUseManagedIdentityCreds: false
      alwaysOn: false
      http20Enabled: true
      functionAppScaleLimit: 0
      minimumElasticInstanceCount: 1
    }
    scmSiteAlsoStopped: false
    clientAffinityEnabled: true
    clientCertEnabled: false
    clientCertMode: 'Required'
    hostNamesDisabled: false
    ipMode: 'IPv4'
    vnetBackupRestoreEnabled: false
    customDomainVerificationId: '85CFBE3C419174E53D3F4F4EFCE4ABD0E363F4096DD33290351AA8E63A0956D0'
    containerSize: 0
    dailyMemoryTimeQuota: 0
    httpsOnly: true
    endToEndEncryptionEnabled: false
    redundancyMode: 'None'
    storageAccountRequired: false
    keyVaultReferenceIdentity: 'SystemAssigned'
  }
}

resource sites_sau00123_name_ftp 'Microsoft.Web/sites/basicPublishingCredentialsPolicies@2024-04-01' = {
  parent: sites_sau00123_name_resource
  name: 'ftp'
  location: 'UK South'
  properties: {
    allow: true
  }
}

resource sites_sau00123_name_scm 'Microsoft.Web/sites/basicPublishingCredentialsPolicies@2024-04-01' = {
  parent: sites_sau00123_name_resource
  name: 'scm'
  location: 'UK South'
  properties: {
    allow: true
  }
}

resource sites_sau00123_name_web 'Microsoft.Web/sites/config@2024-04-01' = {
  parent: sites_sau00123_name_resource
  name: 'web'
  location: 'UK South'
  properties: {
    numberOfWorkers: 1
    defaultDocuments: [
      'Default.htm'
      'Default.html'
      'Default.asp'
      'index.htm'
      'index.html'
      'iisstart.htm'
      'default.aspx'
      'index.php'
      'hostingstart.html'
    ]
    netFrameworkVersion: 'v4.0'
    linuxFxVersion: 'PYTHON|3.10'
    requestTracingEnabled: false
    remoteDebuggingEnabled: false
    remoteDebuggingVersion: 'VS2022'
    httpLoggingEnabled: true
    acrUseManagedIdentityCreds: false
    logsDirectorySizeLimit: 100
    detailedErrorLoggingEnabled: false
    publishingUsername: '$sau00123'
    scmType: 'None'
    use32BitWorkerProcess: true
    webSocketsEnabled: false
    alwaysOn: false
    managedPipelineMode: 'Integrated'
    virtualApplications: [
      {
        virtualPath: '/'
        physicalPath: 'site\\wwwroot'
        preloadEnabled: false
      }
    ]
    loadBalancing: 'LeastRequests'
    experiments: {
      rampUpRules: []
    }
    autoHealEnabled: false
    vnetRouteAllEnabled: false
    vnetPrivatePortsCount: 0
    localMySqlEnabled: false
    ipSecurityRestrictions: [
      {
        ipAddress: 'Any'
        action: 'Allow'
        priority: 2147483647
        name: 'Allow all'
        description: 'Allow all access'
      }
    ]
    scmIpSecurityRestrictions: [
      {
        ipAddress: 'Any'
        action: 'Allow'
        priority: 2147483647
        name: 'Allow all'
        description: 'Allow all access'
      }
    ]
    scmIpSecurityRestrictionsUseMain: false
    http20Enabled: true
    minTlsVersion: '1.2'
    scmMinTlsVersion: '1.2'
    ftpsState: 'FtpsOnly'
    preWarmedInstanceCount: 0
    elasticWebAppScaleLimit: 0
    functionsRuntimeScaleMonitoringEnabled: false
    minimumElasticInstanceCount: 1
    azureStorageAccounts: {}
  }
}

resource sites_sau00123_name_870daf9b_2d7d_47a0_a258_397ee476e392 'Microsoft.Web/sites/deployments@2024-04-01' = {
  parent: sites_sau00123_name_resource
  name: '870daf9b-2d7d-47a0-a258-397ee476e392'
  location: 'UK South'
  properties: {
    status: 4
    author_email: 'N/A'
    author: 'N/A'
    deployer: 'Push-Deployer'
    message: 'Created via a push deployment'
    start_time: '2025-03-24T22:53:04.083322Z'
    end_time: '2025-03-24T22:53:20.2730733Z'
    active: false
  }
}

resource sites_sau00123_name_b6f06f5a_abd7_436d_9277_85f376575735 'Microsoft.Web/sites/deployments@2024-04-01' = {
  parent: sites_sau00123_name_resource
  name: 'b6f06f5a-abd7-436d-9277-85f376575735'
  location: 'UK South'
  properties: {
    status: 4
    author_email: 'N/A'
    author: 'N/A'
    deployer: 'Push-Deployer'
    message: 'Created via a push deployment'
    start_time: '2025-03-24T22:58:14.1233648Z'
    end_time: '2025-03-24T22:59:47.1122778Z'
    active: true
  }
}

resource sites_sau00123_name_sites_sau00123_name_azurewebsites_net 'Microsoft.Web/sites/hostNameBindings@2024-04-01' = {
  parent: sites_sau00123_name_resource
  name: '${sites_sau00123_name}.azurewebsites.net'
  location: 'UK South'
  properties: {
    siteName: 'sau00123'
    hostNameType: 'Verified'
  }
}
