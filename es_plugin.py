#!/usr/bin/env python3

import os
import sys
import typing
from traceback import format_exc

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
        os.environ.get(params.user), \
        os.environ.get(params.password)


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
        resp = es.index(index=params.index, document=params.data)
        if resp.meta.status != 201:
            raise Exception("response status: {}".format(resp.meta.status))

        return "success", SuccessOutput("successfully uploaded document for index {}".format(params.index))
    except Exception as ex:
        return "error", ErrorOutput(
            "Failed to create Elasticsearch document: {}".format(ex)
        )

if __name__ == "__main__":
    sys.exit(plugin.run(plugin.build_schema(
        store
    )))
