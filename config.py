PORT = 443

# name -> secret (32 hex chars)
# head -c 16 /dev/urandom | xxd -ps
USERS = {
    "tg": "00000000000000000000000000000001",
    "tg": "db61346b48f57ea2ff3710e833a1c0d0",
}

MODES = {
    # Classic mode, easy to detect
    "classic": False,

    # Makes the proxy harder to detect
    # Can be incompatible with very old clients
    "secure": True,

    # Makes the proxy even more hard to detect
    # Can be incompatible with old clients
    "tls": True
}

# The domain for TLS mode, bad clients are proxied there
# Use random existing domain, proxy checks it on start
# TLS_DOMAIN = "www.google.com"

# Tag for advertising, obtainable from @MTProxybot
# AD_TAG = "3c09c680b76ee91a4c25ad51f742267d"
