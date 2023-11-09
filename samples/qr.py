# THIS SCRIPT REQUIRES THE 'qrcode' module.
import qrcode
import qrcode.image.svg
import backpipe

server = backpipe.BackPipe(port=8000)

@server.post
def answer(r: backpipe.Request):
    try:
        txt = r.headers["text"]
        response = qrcode.make(txt, image_factory=qrcode.image.svg.SvgImage).to_string()
    except KeyError:
        return (400, "text header is required.")
    return (200, response)

server.run()