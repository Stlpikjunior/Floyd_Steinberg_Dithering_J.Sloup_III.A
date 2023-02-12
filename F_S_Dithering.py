from PIL import Image

obr = Image.open('Wald.png')
pixels = obr.load()
width = obr.size[0]
height = obr.size[1]
for y in range(height - 1):
    for x in range(1, width - 1):
        listfrac = [(7 / 16), (1 / 16), (5 / 16), (3 / 16)]
        listcoord = [[[x + 1], [y]], [[x + 1], [y + 1]], [[x], [y + 1]], [[x - 1], [y + 1]]]
        r = pixels[x, y][0]
        g = pixels[x, y][1]
        b = pixels[x, y][2]
        col = []

        if r <= 127:
            rerr = r - 0
            r = 0
        elif r > 127:
            rerr = r - 255
            r = 255
        if g <= 127:
            gerr = g - 0
            g = 0
        elif g > 127:
            gerr = g - 255
            g = 255
        if b <= 127:
            berr = b
            b = 0
        elif b > 127:
            berr = b - 255
            b = 255
        col.append(r)
        col.append(g)
        col.append(b)
        pixels[x, y] = (r, g, b)

        for s in range(4):  # both the coord and the fractions
            a = int(str(listcoord[s][0]).strip('[]'))
            b = int(str(listcoord[s][1]).strip('[]'))
            oldcol = pixels[a, b]
            newr = oldcol[0] + round(rerr * listfrac[s])
            newg = oldcol[1] + round(gerr * listfrac[s])
            newb = oldcol[2] + round(berr * listfrac[s])
            pixels[a, b] = (newr, newg, newb)

obr.save('fin_product.png')
print('Im done')
