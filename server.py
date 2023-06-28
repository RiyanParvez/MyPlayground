from pyngrok import ngrok

ngrok.set_auth_token("2RVZIbb69PvJzDNNup9hRkNfE0Z_4tkXXg4BiYRSFCoAnDLCK")
ngrok_tunnel = ngrok.connect(5432)
