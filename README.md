# myJSONStore
A wrapper for the popular json-store-client library - a client for jsonstore.io

This leverages the core mechanics of the jsonstore.io source to bypass the (unintentional) data upload limit and decentralize the keys in which data is stored.

## usage

### example 1: from a script
	from jsonstore import Client
	import os
	data = os.urandom(4096)
	k, c = Client().store(data)
	Client().retrieve(k, c) == data # true

### example 2: as a script
	python -m jsonstore -h

