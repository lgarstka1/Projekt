@description('Lokalizacja zasobów')
param location string

@description('Prefix nazwy projektu')
param projectName string

var acrName = 'acr${projectName}${uniqueString(resourceGroup().id)}'
var storageName = 'st${projectName}${uniqueString(resourceGroup().id)}'

resource acr 'Microsoft.ContainerRegistry/registries@2023-01-01-preview' = {
  name: acrName
  location: location
  sku: {
    name: 'Basic'
  }
  properties: {
    adminUserEnabled: true
  }
}
