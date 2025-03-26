param serverfarms_saurabh_dasgupta_asp_7636_name string = 'saurabh_dasgupta_asp_7636'

resource serverfarms_saurabh_dasgupta_asp_7636_name_resource 'Microsoft.Web/serverfarms@2024-04-01' = {
  name: serverfarms_saurabh_dasgupta_asp_7636_name
  location: 'UK South'
  sku: {
    name: 'F1'
    tier: 'Free'
    size: 'F1'
    family: 'F'
    capacity: 1
  }
  kind: 'linux'
  properties: {
    perSiteScaling: false
    elasticScaleEnabled: false
    maximumElasticWorkerCount: 1
    isSpot: false
    reserved: true
    isXenon: false
    hyperV: false
    targetWorkerCount: 0
    targetWorkerSizeId: 0
    zoneRedundant: false
  }
}
