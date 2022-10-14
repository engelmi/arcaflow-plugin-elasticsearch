#!/usr/bin/env python3

import hashlib
import json
import os
import sys
import typing

from elasticsearch import Elasticsearch

from arcaflow_plugin_sdk import plugin
from es_schema import (
    ErrorOutput,
    SuccessOutput,
    StoreDocumentRequest
)


def getEnvironmentVariables(params: StoreDocumentRequest) -> tuple[str, str, str]:
    """
    :return: a tuple [url, user, password] containing the extracted values 
    from the environment variables. 
    """
    return os.environ.get(params.url), \
        os.environ.get(params.username), \
        os.environ.get(params.password)

def gen_id(params: StoreDocumentRequest) -> str:
    """
    :return: a str representing the SHA256 hash for the store document request.
    """
    sha256 = hashlib.sha256()
    data_raw = json.dumps(params.data)
    sha256.update(data_raw)
    return sha256.hexdigest()

@plugin.step(
    id="elasticsearch",
    name="Elasticsearch",
    description="Load data into elasticsearch instance",
    outputs={"success": SuccessOutput, "error": ErrorOutput},
)
def store(
    params: StoreDocumentRequest
) -> typing.Tuple[str, typing.Union[SuccessOutput, ErrorOutput]]:
    """
    :return: the string identifying which output it is, as well the output structure
    """

    url, user, password = getEnvironmentVariables(params)
    
    try:
        es = Elasticsearch(hosts=url, basic_auth=[user, password])
        data_id = get_id(params.data)
        resp = es.index(index=params.index, id=data_id, document=params.data)
        if resp.meta.status != 201:
            raise Exception(f"response status: {resp.meta.status}")

        return "success", SuccessOutput(f"successfully uploaded document for index {params.index}")
    except Exception as ex:
        return "error", ErrorOutput(
            f"Failed to create Elasticsearch document: {ex}"
        )

if __name__ == "__main__":
    sys.exit(plugin.run(plugin.build_schema(
        store
    )))
