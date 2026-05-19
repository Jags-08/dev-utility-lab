from dev_utility_sdk import TopologyAwareClient
# Quickstart integration path
client = TopologyAwareClient(region="EU-CENTRAL")
print(client.ping())
