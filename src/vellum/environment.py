# This file was auto-generated by Fern from our API Definition.

from __future__ import annotations


class VellumApiEnvironment:
    PRODUCTION: VellumApiEnvironment

    def __init__(self, *, predict: str, document: str):
        self.predict = predict
        self.document = document


VellumApiEnvironment.PRODUCTION = VellumApiEnvironment(
    predict="https://predict.vellum.ai", document="https://documents.vellum.ai"
)