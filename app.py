#!/usr/bin/env python3

from aws_cdk import core

from url_shortener.url_shortener_stack import UrlShortenerStack, TrafficStack


app = core.App()
UrlShortenerStack(app, "url-shortener")

# cdk deploy test-traffic
TrafficStack(app, "test-traffic")

app.synth()

# https://www.youtube.com/watch?v=ZWCvNFUN-sU&t=2901s