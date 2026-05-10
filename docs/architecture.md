# Architecture & Design

`dev-utility-lab` is built using a modern modular WSGI architecture deployed securely over Docker.

## High-Level Pipeline

```
[ NGINX/Frontend ] -> [ Gunicorn WSGI (4 Workers) ] -> [ Flask App (dashboard/app.py) ]
                                                                |
                                             +------------------+------------------+
                                             |                                     |
                                 [ Production Config Loader ]            [ Tool Dispatcher ]
                                             |                                     |
                                        (.env parsing)                [ Python dev_utils Lib ]
```

## Caching Strategy
We employ functional `lru_cache` natively mapping JSON-stringified payloads dynamically over tool executions, skipping recalculations strictly for deterministic components (math, string). Random generators bypass caching natively.
