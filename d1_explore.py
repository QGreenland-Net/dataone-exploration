from d1_client.d1client import DataONEClient

def list_node_descriptions(client: DataONEClient) -> list[str]:
    """Return a human readable string about each node."""
    node_list = client.listNodes().content()
    return [n.description for n in node_list]


def explore_search(client: DataONEClient, query: str):
    # Docs says "SOLR", but that 404s and "solr" doesn't!
    return client.search(queryType="solr", query=query)


if __name__ == "__main__":
    client = DataONEClient()

    print(f"Some DataONE nodes: {list_node_descriptions(client)[:3]}")

    # Based on example: https://opc.dataone.org/api
    # results = explore_search(client, query="?q=title:soil").content()
    results = explore_search(client, query="?q=title:soil")
    breakpoint()
    ...
