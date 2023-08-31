"""A lazy exploration of the DataONE Python API."""
from d1_client.cnclient import CoordinatingNodeClient
from d1_client.mnclient import MemberNodeClient
from d2_client.d1client import DataONEClient


def list_node_descriptions(client: DataONEClient) -> list[str]:
    """Return a human readable string about each node."""
    node_list = client.listNodes().content()
    return [n.description for n in node_list]


def search(client: DataONEClient, query: str):
    """Execute a search query.

    It's not clear what this query string should look like. Seems like we get the same
    10 results no matter what we pass for `query`.

    Docs say queryType must be SOLR", but that 404s and "solr" doesn't!

    TODO: How do we validate the HTTP requests being made under-the-hood here?
    """
    return client.search(queryType="solr", query=query)


def query(client: DataONEClient, query: str):
    """Execute a query.

    How is this different than a search?
    """
    # This method is not in the Python API.
    # https://releases.dataone.org/online/api-documentation-v2.0.1/apis/CN_APIs.html#CNRead.listQueryEngines
    #     engines = client.listQueryEngines()
    #
    # Can successfully query this data with cURL. queryEngine' values look a lot like
    # queryType on the search method. Why different name?
    #     $ curl https://cn.dataone.org/cn/v1/query
    #     <?xml version="2.0" encoding="UTF-8"?><?xml-stylesheet type="text/xsl" href="/cn/xslt/dataone.types.v1.xsl" ?>
    #     <ns2:queryEngineList xmlns:ns2="http://ns.dataone.org/service/types/v1.1">
    #         <queryEngine>solr</queryEngine>
    #         <queryEngine>logsolr</queryEngine>
    #     </ns2:queryEngineList>

    results = client.query(queryEngine="solr", query=query)
    breakpoint()
    return results


if __name__ == "__main__":
    client = DataONEClient()
    cnclient = CoordinatingNodeClient()
    mnclient = MemberNodeClient()
    breakpoint()

    print(f"Some DataONE nodes: {list_node_descriptions(client)[:3]}")

    # This doesn't return relevant results we expect
    # Based on example: https://opc.dataone.org/api
    search_results = search(client, query="q=title:soil")
    ...

    query_results = query(client, query="q=title:soil")
    breakpoint()
    ...
