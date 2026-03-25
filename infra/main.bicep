targetScope = 'subscription'

@description('Nazwa grupy zasobów')
param rgName string = 'DevOps-Projekt'

@description('Lokalizacja zasobów')
param location string = 'westeurope'

@description('Prefix dla nazw zasobów')
param projectName string = 'projekt'

resource rg 'Microsoft.Resources/resourceGroups@2022-09-01' = {
  name: rgName
  location: location
}

module resources 'resources.bicep' = {
  name: 'deploy-resources'
  scope: rg
  params: {
    location: location
    projectName: projectName
  }
}
