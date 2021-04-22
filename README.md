# turnio-webhooks-hmacs-replit

An example Turn.io webhook integration on Replit demonstrating how HMAC signatures can be verified. This will return with a 403 status code if the received HMAC signature does not match the calculated signature, 200 otherwise.

For this to work you need to set a Turn webhook secret as a secret named `SECRET` in Replit.

[![Run on Repl.it](https://repl.it/badge/github/turnhub/turnio-webhooks-hmacs-replit)](https://repl.it/github/turnhub/turnio-webhooks-hmacs-replit)
