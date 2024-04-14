# Need to enable_https manually by uncommenting it in the source code (backpipe/app.py)
import backpipe

server = backpipe.BackPipe(port=3000)

server.enable_https("cert.pem", "key.pem")

server.run()