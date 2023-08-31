An exploration of the DataONE API.

:construction: We're just messing around here, please don't expect anything here to be
correct or re-usable :)


## Client library

* [Official docs](https://pythonhosted.org/DataONE_ClientLib/index.html)


### Questions

* `d1baseclient` doesn't have `listQueryEngines`. Do we need to use `cnclient` to do
  `listQueryEngines`?


## Ideas

* An end-to-end tutorial for the Python client. I couldn't find something like this, so
  I had some immediate questions:
    * How do I import this? Because the pypi upload has a `.` in its name, you can't
      import the package by the same name it was installed. `help()` to the rescue
      (`modules` command)!
