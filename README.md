An exploration of the DataONE API.

:construction: We're just messing around here, please don't expect anything here to be
correct, re-usable, or even useful :)


## Terms

See the
[glossary](https://releases.dataone.org/online/api-documentation-v2.0.1/glossary.html#term-member-node)
for a full listing.

* Node: An element of the DataONE federated architecture.
* [Member Nodes](https://releases.dataone.org/online/api-documentation-v2.0.1/glossary.html#term-member-node): 
  A node that users (or Coordinating Nodes) can publish data to or read data from.
* [Coordinating Nodes](https://releases.dataone.org/online/api-documentation-v2.0.1/glossary.html#term-coordinating-node):
  A node that provides a unifying abstraction over Member Nodes by storing metadata (not
  just in the usual sense, but also DataONE-specific things like "which member node has
  this data?"), enabling search, and doing other system housekeeping things. Content on
  Coordinating Nodes is replicated across all nodes.


## Interfaces

* [DataONE APIs](https://releases.dataone.org/online/api-documentation-v2.0.1/apis/index.html)

### REST API

* [REST Interface Overview](https://releases.dataone.org/online/api-documentation-v2.0.1/apis/rest_comms.html): 
  A general description.
* [Coordinating Node APIs](https://releases.dataone.org/online/api-documentation-v2.0.1/apis/CN_APIs.html)
* [Member Node APIs](https://releases.dataone.org/online/api-documentation-v2.0.1/apis/MN_APIs.html)


### Python Client library

* [Official docs](https://dataone-python.readthedocs.io/en/latest/d1_client/index.html)

> :warning: BEWARE of a second copy of the docs at pythonhosted.org; they are
> significantly less useful than the ReadTheDocs site above.


#### Questions

* `d1baseclient` doesn't have `listQueryEngines`. Do we need to use `cnclient` to do
  `listQueryEngines`?


## Ideas

* An end-to-end tutorial for the Python client. I couldn't find something like this, so
  I had some immediate questions:
    * How do I import this? Because the pypi upload has a `.` in its name, you can't
      import the package by the same name it was installed. `help()` to the rescue
      (`modules` command)!
