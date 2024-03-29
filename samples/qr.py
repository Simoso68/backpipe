# THIS SCRIPT REQUIRES THE 'qrcode' and 'cairosvg' modules.
import qrcode
import qrcode.image.svg
import cairosvg
import backpipe

server = backpipe.BackPipe()

@server.any
def answer(r: backpipe.Request):
    txt = r.path[1:]
    svg = qrcode.make(txt, image_factory=qrcode.image.svg.SvgImage).to_string()
    return (200, cairosvg.svg2png(svg))

server.run()